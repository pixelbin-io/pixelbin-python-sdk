from ..common.aiohttp_helper import AiohttpHelper
import base64
from .PixelbinConfig import PixelbinConfig
from ..common.utils import add_signature_to_headers, create_url_with_params_and_query_string

class APIClient:
    
    @staticmethod
    async def execute(conf:PixelbinConfig, method:str, url:str, query:dict, body:dict, contentType:str):
        """
        :param conf : configuration details : Type - dict 
        :param method : method name : Type - str
        :param url : url to hit : Type - str
        :param query : query parameters of url : Type - dict
        :param body : body content for url : Type - dict
        """
        token = base64.b64encode(bytes(await conf.getAccessToken(), 'utf-8')).decode()
        headers = {
            'Authorization': f"Bearer {token}",
        }
        if contentType != "" and contentType != "multipart/form-data" and len(body)>0:
            headers["Content-Type"] = contentType
        data = body
        if contentType == "multipart/form-data":
            data = None
            
        if query and method.upper() == "GET":
            get_parmas = {}
            for k, v in query.items():
                v = ",".join(v) if isinstance(v, list) else v
                get_parmas[k] = v
            query = get_parmas

        _, query_string = await create_url_with_params_and_query_string(conf.domain, url, query)

        headers_with_sign = await add_signature_to_headers(
            domain=conf.domain,
            method=method,
            url=url,
            query_string=query_string,
            headers=headers,
            body=data,
            exclude_headers=["Authorization", 'Content-Type']
            )

        headers_with_sign['x-ebg-param'] = base64.b64encode(bytes(headers_with_sign['x-ebg-param'], 'utf-8')).decode()
        return await AiohttpHelper().request(method=method, url=f"{conf.domain}{url}", params=query, data=body, headers=headers_with_sign)
