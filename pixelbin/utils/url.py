
from urllib.parse import urlparse
import re
from ..common.exceptions import PixelbinInvalidUrlError, PixelbinIllegalArgumentError

OPERTATION_SEPARATOR = "~"
PARAMETER_SEPARATOR = ","
VERSION2_REGEX = r"^v[1-2]$"
URL_WITH_ZONE = r"^\/([a-zA-Z0-9_-]*)\/([a-zA-Z0-9_-]{6})\/(.+)\/(.*)$"
URL_WITHOUT_ZONE = r"\/([a-zA-Z0-9_-]*)\/(.+)\/(.*)"
ZONE_SLUG = r"([a-zA-Z0-9_-]{6})"
BASE_URL = "https://cdn.pixelbin.io"


def url_to_obj(url: str):
    return get_obj_from_url(url)

def obj_to_url(obj: dict):
    return get_url_from_obj(obj)


def get_url_parts(pixelbinUrl):
    parse_url = urlparse(pixelbinUrl)
    urlDetails = {
        "protocol":parse_url.scheme,
        "host": parse_url.hostname,
        "version": "v1",
    }
    parts = parse_url.path.split("/");
    if re.search(VERSION2_REGEX, parts[1]) is not None:
        urlDetails["version"] = parts[1]
        del parts[1]

    if len(parts[1]) < 3:
        raise PixelbinInvalidUrlError("Invalid pixelbin url. Please make sure the url is correct.")
    
    if (re.search(URL_WITH_ZONE, "/".join(parts))):
        urlDetails["cloudName"] = parts[1]
        del parts[1]
        urlDetails["zoneSlug"] = parts[1]
        del parts[1]
        urlDetails["pattern"] = parts[1]
        del parts[1]
        urlDetails["filePath"] = "/".join(parts[1:])

    elif (re.search(URL_WITHOUT_ZONE,"/".join(parts))):
        urlDetails["cloudName"] = parts[1]
        del parts[1]
        urlDetails["pattern"] = parts[1]
        del parts[1]
        urlDetails["filePath"] = "/".join(parts[1:])
    else: 
        raise PixelbinInvalidUrlError("Invalid pixelbin url. Please make sure the url is correct.")    
    return urlDetails


def get_parts_from_url(url):
    parts = get_url_parts(url)
    parts["zone"] = None
    if "zoneSlug" in parts:
        parts["zone"] = parts["zoneSlug"]
        parts.pop("zoneSlug")
    parts["baseUrl"] = f"{parts['protocol']}://{parts['host']}"
    parts.pop("protocol")
    parts.pop("host")
    return parts


def remove_leading_dash(str):
    if len(str)> 0 and str[0] == "-":
        return str[1:]
    return str

def get_params_list(dSplit, prefix):
    return remove_leading_dash(dSplit.split("(")[1].replace(")", "").replace(prefix, "")).split(",")


def get_params_object(paramsList):
    params = []
    for item in paramsList:
        if ":" in item:
            param, val = item.split(":")
            if param:
                params.append({
                    "key": param,
                    "value": val
                })

    if len(params) > 0:
        return params
    return 0


def txt_to_options(dSplit):
    #Figure Out Module
    fullFnName = dSplit.split("(")[0]

    pluginId, operationName = fullFnName.split(".")

    if pluginId == "p":
        params = get_params_object(get_params_list(dSplit, ""))
        for p in params:
            if p["key"] == "n":
                return {
                    "plugin": pluginId,
                    "name": p["value"]
                }
        return None

    values = get_params_object(get_params_list(dSplit, "."))
    plugin, name = dSplit.split("(")[0].split(".")
    transformation = {
        "plugin": plugin,
        "name":name
    }
    if values:
        transformation["values"] = values
    return transformation

import itertools

def get_transformations_from_pattern(pattern, url, flatten = False):
    if pattern == "original":
        return []

    dSplit = pattern.split(OPERTATION_SEPARATOR)

    def mapfunc(x:str):
        if x.startswith("p:"):
            _, presetString = x.split(":") 
            x = f"p.apply(n:{presetString})"
        return txt_to_options(x)

    opts = list(itertools.chain(list(map(mapfunc, dSplit))))

    if flatten:
        opts = itertools.chain(opts)
    return opts


def get_obj_from_url(url, flatten=False):
    parts = get_parts_from_url(url)
    try:
        parts["transformations"] = get_transformations_from_pattern(
            parts["pattern"],
            url,
            flatten
        )
    except Exception as e: 
        raise PixelbinInvalidUrlError(f"Error Processing url. Please check the url is correct, {e}")
    return parts


def get_url_from_obj(obj:dict):
    if "baseUrl" not in obj:
        obj["baseUrl"] = BASE_URL
    
    if "cloudName" not in obj:
        raise PixelbinIllegalArgumentError("key cloudName should be defined")
    if "filePath" not in obj:
        raise PixelbinIllegalArgumentError("key filePath should be defined")

    pattern_value = get_pattern_from_transformations(obj["transformations"])
    obj["pattern"] =  pattern_value if pattern_value is not None else "original"
    if ("version" not in obj) or re.search(VERSION2_REGEX, obj["version"]) is None:
        obj["version"]  = "v2"
    if ("zone" not in obj) or (obj["zone"] is None) or (re.search(ZONE_SLUG, obj["zone"]) is None):
        obj["zone"] = ""
    urlKeySorted = ["baseUrl", "version", "cloudName", "zone", "pattern", "filePath"]
    urlArr = []
    for key in urlKeySorted:
        if key in obj and obj[key]:
            urlArr.append(obj[key])
    return "/".join(urlArr)



def get_pattern_from_transformations(transformationList) :
    if len(transformationList)==0:
        return None
    
    def mapfunc(o):
        if "name" in o:
            if o["plugin"] == "p":
                return f"p:{o['name']}"
            else:
                o["values"] = o["values"] if "values" in o else []
                paramlist = []
                for items in o["values"]:
                    if "key" not in items:
                        raise PixelbinIllegalArgumentError("key not specified.")
                    if "value" not in items:
                        raise PixelbinIllegalArgumentError(f"value not specified for {items['key']}")
                    paramlist.append(f"{items['key']}:{items['value']}")
                paramstr = f"{PARAMETER_SEPARATOR}".join(paramlist)
                return f"{o['plugin']}.{o['name']}({paramstr})"
        return None

    transformationList = list(map(mapfunc, transformationList))
    transformationList = list(filter(lambda ele : ele, transformationList))
    return f"{OPERTATION_SEPARATOR}".join(transformationList)

