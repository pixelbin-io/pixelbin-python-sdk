from urllib.parse import urlparse
import re
from ..common.exceptions import (
    PixelbinInvalidUrlError,
    PixelbinIllegalArgumentError,
    PixelbinIllegalQueryParameterError,
)

OPERTATION_SEPARATOR = "~"
PARAMETER_SEPARATOR = ","
VERSION2_REGEX = r"^v[1-2]$"
PIXELBIN_DOMAIN_REGEX = {
    "URL_WITHOUT_ZONE": r"\/([a-zA-Z0-9_-]*)\/(.+)\/(.*)",
    "URL_WITH_ZONE": r"^\/([a-zA-Z0-9_-]*)\/([a-zA-Z0-9_-]{6})\/(.+)\/(.*)$",
    "URL_WITH_WORKER_AND_ZONE": r"^\/([a-zA-Z0-9_-]*)\/([a-zA-Z0-9_-]{6})\/wrkr\/(.*)$",
    "URL_WITH_WORKER": r"^\/([a-zA-Z0-9_-]*)\/wrkr\/(.*)$",
}
CUSTOM_DOMAIN_REGEX = {
    "URL_WITHOUT_ZONE": r"\/(.+)\/(.*)",
    "URL_WITH_ZONE": r"\/([a-zA-Z0-9_-]{6})\/(.+)\/(.*)$",
    "URL_WITH_WORKER_AND_ZONE": r"\/([a-zA-Z0-9_-]{6})\/wrkr\/(.*)$",
    "URL_WITH_WORKER": r"\/wrkr\/(.*)$",
}
ZONE_SLUG = r"([a-zA-Z0-9_-]{6})"
BASE_URL = "https://cdn.pixelbin.io"
ALLOWED_OPTIONAL_PARAMS = ["dpr", "f_auto"]


def url_to_obj(url: str, opts: dict = {"is_custom_domain": False}):
    return get_obj_from_url(url, opts=opts)


def obj_to_url(obj: dict):
    return get_url_from_obj(obj)


def get_url_parts(pixelbinUrl, opts={"is_custom_domain": False}):
    parse_url = urlparse(pixelbinUrl)
    urlDetails = {
        "protocol": parse_url.scheme,
        "host": parse_url.hostname,
        "search": parse_url.query,
        "version": "v1",
        "cloudName": None,
        "worker": False,
        "workerPath": "",
    }
    parts = parse_url.path.split("/")

    if opts["is_custom_domain"]:
        # parsing custom domains url
        if re.search(VERSION2_REGEX, parts[1]):
            urlDetails["version"] = parts[1]
            del parts[1]
        else:
            raise PixelbinInvalidUrlError(
                "Invalid pixelbin url. Please make sure the url is correct."
            )

        if re.search(CUSTOM_DOMAIN_REGEX["URL_WITH_WORKER_AND_ZONE"], "/".join(parts)):
            urlDetails["zoneSlug"] = parts[1]
            del parts[1]
            urlDetails["pattern"] = ""
            urlDetails["filePath"] = ""
            urlDetails["worker"] = True
            urlDetails["workerPath"] = "/".join(parts[2:])
        elif re.search(CUSTOM_DOMAIN_REGEX["URL_WITH_WORKER"], "/".join(parts)):
            urlDetails["pattern"] = ""
            urlDetails["filePath"] = ""
            urlDetails["worker"] = True
            urlDetails["workerPath"] = "/".join(parts[2:])
        elif re.search(CUSTOM_DOMAIN_REGEX["URL_WITH_ZONE"], "/".join(parts)):
            urlDetails["zoneSlug"] = parts[1]
            del parts[1]
            urlDetails["pattern"] = parts[1]
            del parts[1]
            urlDetails["filePath"] = "/".join(parts[1:])
        elif re.search(CUSTOM_DOMAIN_REGEX["URL_WITHOUT_ZONE"], "/".join(parts)):
            urlDetails["pattern"] = parts[1]
            del parts[1]
            urlDetails["filePath"] = "/".join(parts[1:])
    else:
        if re.search(VERSION2_REGEX, parts[1]) is not None:
            urlDetails["version"] = parts[1]
            del parts[1]

        if len(parts[1]) < 3:
            raise PixelbinInvalidUrlError(
                "Invalid pixelbin url. Please make sure the url is correct."
            )

        if re.search(
            PIXELBIN_DOMAIN_REGEX["URL_WITH_WORKER_AND_ZONE"], "/".join(parts)
        ):
            urlDetails["cloudName"] = parts[1]
            del parts[1]
            urlDetails["zoneSlug"] = parts[1]
            del parts[1]
            urlDetails["pattern"] = ""
            urlDetails["filePath"] = ""
            urlDetails["worker"] = True
            urlDetails["workerPath"] = "/".join(parts[2:])
        elif re.search(PIXELBIN_DOMAIN_REGEX["URL_WITH_WORKER"], "/".join(parts)):
            urlDetails["cloudName"] = parts[1]
            del parts[1]
            urlDetails["pattern"] = ""
            urlDetails["filePath"] = ""
            urlDetails["worker"] = True
            urlDetails["workerPath"] = "/".join(parts[2:])
        elif re.search(PIXELBIN_DOMAIN_REGEX["URL_WITH_ZONE"], "/".join(parts)):
            urlDetails["cloudName"] = parts[1]
            del parts[1]
            urlDetails["zoneSlug"] = parts[1]
            del parts[1]
            urlDetails["pattern"] = parts[1]
            del parts[1]
            urlDetails["filePath"] = "/".join(parts[1:])
        elif re.search(PIXELBIN_DOMAIN_REGEX["URL_WITHOUT_ZONE"], "/".join(parts)):
            urlDetails["cloudName"] = parts[1]
            del parts[1]
            urlDetails["pattern"] = parts[1]
            del parts[1]
            urlDetails["filePath"] = "/".join(parts[1:])
        else:
            raise PixelbinInvalidUrlError(
                "Invalid pixelbin url. Please make sure the url is correct."
            )

    return urlDetails


def get_parts_from_url(url, opts={"is_custom_domain": False}):
    parts = get_url_parts(url, opts=opts)
    queryObj = processQueryParams(parts)

    return {
        "baseUrl": f"{parts['protocol']}://{parts['host']}",
        "version": parts["version"],
        "cloudName": parts["cloudName"],
        "zone": parts["zoneSlug"] if "zoneSlug" in parts else None,
        "pattern": parts["pattern"],
        "filePath": parts["filePath"],
        "worker": parts["worker"],
        "workerPath": parts["workerPath"],
        "options": queryObj,
    }


def remove_leading_dash(str):
    if len(str) > 0 and str[0] == "-":
        return str[1:]
    return str


def get_params_list(dSplit, prefix):
    return remove_leading_dash(
        dSplit.split("(")[1].replace(")", "").replace(prefix, "")
    ).split(",")


def get_params_object(paramsList):
    params = {}
    for item in paramsList:
        if ":" in item:
            param, val = item.split(":")
            if param:
                params[param] = val

    if len(params) > 0:
        return params
    return 0


# previously txtToOptions
def get_operation_details_from_operation(dSplit):
    # Figure Out Module
    fullFnName = dSplit.split("(")[0]

    pluginId = None
    operationName = None
    if dSplit.startswith("p:"):
        pluginId = fullFnName.split(":")[0]
        operationName = fullFnName.split(":")[1]
    else:
        pluginId = fullFnName.split(".")[0]
        operationName = fullFnName.split(".")[1]

    values = None
    if pluginId == "p":
        if "(" in dSplit:
            values = get_params_object(get_params_list(dSplit, ""))
    else:
        values = get_params_object(get_params_list(dSplit, ""))

    # plugin, name = dSplit.split("(")[0].split(".")
    transformation = {"plugin": pluginId, "name": operationName}
    if values:
        transformation["values"] = values
    return transformation


import itertools


def get_transformation_details_from_pattern(pattern, url, flatten=False):
    if pattern == "original":
        return []

    dSplit = pattern.split(OPERTATION_SEPARATOR)

    def mapfunc(x: str):
        # if x.startswith("p:"):
        #     _, presetString = x.split(":")
        #     x = f"p.apply(n:{presetString})"
        result = get_operation_details_from_operation(x)
        name = result["name"]
        plugin = result["plugin"]
        values = result["values"] if "values" in result else None

        if values and len(values) > 0:

            def mapkeyvalue(x: str):
                return {"key": x, "value": values[x]}

            values = list(map(mapkeyvalue, values))
            return {"plugin": plugin, "name": name, "values": values}

        return {"plugin": plugin, "name": name}

    opts = list(itertools.chain(list(map(mapfunc, dSplit))))

    if flatten:
        opts = itertools.chain(opts)
    return opts


def get_obj_from_url(url, flatten=False, opts={"is_custom_domain": False}):
    parts = get_parts_from_url(url, opts=opts)
    try:
        parts["transformations"] = (
            get_transformation_details_from_pattern(parts["pattern"], url, flatten)
            if parts["pattern"]
            else []
        )
    except Exception as e:
        raise PixelbinInvalidUrlError(
            f"Error Processing url. Please check the url is correct, {e}"
        )
    return parts


def get_url_from_obj(obj: dict):
    if "baseUrl" not in obj:
        obj["baseUrl"] = BASE_URL

    if not obj.get("isCustomDomain") and not obj.get("cloudName"):
        raise PixelbinIllegalArgumentError("key cloudName should be defined")
    if obj.get("isCustomDomain") and obj.get("cloudName"):
        raise PixelbinIllegalArgumentError(
            "key cloudName is not valid for custom domains"
        )
    if not obj.get("worker") and not obj.get("filePath"):
        raise PixelbinIllegalArgumentError("key filePath should be defined")
    if obj.get("worker") and not isinstance(obj.get("workerPath"), str):
        raise PixelbinIllegalArgumentError("key workerPath should be defined")
    if obj.get("worker"):
        obj["pattern"] = "wrkr"
    else:
        pattern_value = get_pattern_from_transformations(obj["transformations"])
        obj["pattern"] = pattern_value if pattern_value is not None else "original"

    if ("version" not in obj) or re.search(VERSION2_REGEX, obj["version"]) is None:
        obj["version"] = "v2"
    if (
        ("zone" not in obj)
        or (obj["zone"] is None)
        or (re.search(ZONE_SLUG, obj["zone"]) is None)
    ):
        obj["zone"] = ""
    urlKeySorted = ["baseUrl", "version", "cloudName", "zone", "pattern"]
    if obj.get("worker"):
        urlKeySorted.append("workerPath")
    else:
        urlKeySorted.append("filePath")
    urlArr = []
    for key in urlKeySorted:
        if key in obj and obj[key]:
            urlArr.append(obj[key])

    queryArr = []
    if "options" in obj and len(obj["options"]) > 0:
        if obj["options"].get("dpr") is not None:
            dpr = parseDPR(obj["options"]["dpr"])
            queryArr.append(f"dpr={dpr}")
        if obj["options"].get("f_auto") is not None:
            validateFAuto(obj["options"]["f_auto"])
            f_auto = "true" if obj["options"]["f_auto"] else "false"
            queryArr.append(f"f_auto={f_auto}")

    urlStr = "/".join(urlArr)
    if len(queryArr) > 0:
        urlStr += "?" + "&".join(queryArr)
    return urlStr


def get_pattern_from_transformations(transformationList):
    if len(transformationList) == 0:
        return None

    def mapfunc(o):
        if "name" in o:
            o["values"] = o["values"] if "values" in o else []
            paramlist = []
            for items in o["values"]:
                if "key" not in items or not items["key"]:
                    raise PixelbinIllegalArgumentError(
                        f"key not specified in '{o['name']}'"
                    )
                if "value" not in items or not items["value"]:
                    raise PixelbinIllegalArgumentError(
                        f"value not specified for '{items['key']}' in '{o['name']}'"
                    )
                paramlist.append(f"{items['key']}:{items['value']}")
            paramstr = f"{PARAMETER_SEPARATOR}".join(paramlist)

            if o["plugin"] == "p":
                return f"p:{o['name']}({paramstr})" if paramstr else f"p:{o['name']}"
            return f"{o['plugin']}.{o['name']}({paramstr})"
        return None

    transformationList = list(map(mapfunc, transformationList))
    transformationList = list(filter(lambda ele: ele, transformationList))
    return f"{OPERTATION_SEPARATOR}".join(transformationList)


def parseDPR(dpr):
    if dpr == "auto":
        return dpr
    dpr = float(dpr)
    if dpr < 0.1 or dpr > 5.0:
        raise PixelbinIllegalQueryParameterError(
            "DPR value should be numeric and should be between 0.1 to 5.0"
        )
    return dpr


def validateFAuto(f_auto):
    if not isinstance(f_auto, bool):
        raise PixelbinIllegalQueryParameterError("F_auto value should be boolean")


def parseFAuto(f_auto):
    if f_auto == "true":
        return True
    if f_auto == "false":
        return False
    raise PixelbinIllegalQueryParameterError("F_auto value should be boolean")


def processQueryParams(urlParts):
    queryParams = urlParts["search"].split("&")
    queryObj = {}
    for params in queryParams:
        queryElements = params.split("=")
        if len(queryElements) == 2:
            query, value = queryElements
            if query == "dpr":
                queryObj["dpr"] = parseDPR(value)
            elif query == "f_auto":
                queryObj["f_auto"] = parseFAuto(value)

    return queryObj
