import json
import ujson
import sys
import unittest
from unittest import mock
from pixelbin.common.exceptions import (
    PixelbinInvalidCredentialError,
    PixelbinServerResponseError,
    PixelbinIllegalArgumentError,
)
from pixelbin.common.aiohttp_helper import AiohttpHelper
from aiohttp import FormData
from test_utils import URLS_TO_OBJ, OBJ_TO_URL, MOCK_RESPONSE, SIGN_URL_CASES
import base64
from urllib import parse


sys.path.append(__file__.replace("/tests/pixelbin_test.py", ""))

CONFIG = {
    "host": "api.pixelbin.io",
    "domain": "https://api.pixelbin.io",
    "apiSecret": "token",
}

BEARER_TOKEN = (
    "Bearer " + base64.b64encode(bytes(CONFIG["apiSecret"], "utf-8")).decode()
)


class TestPixelBin(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

        self.config = CONFIG
        from pixelbin import PixelbinConfig, PixelbinClient

        self.pixelbinConfig = PixelbinConfig(config=self.config)
        self.pixelbinClient = PixelbinClient(config=self.pixelbinConfig)
        self.create_data()

    def create_data(self):
        self.folder_name = "testdir"
        self.folder_path = "/"
        self.urls_to_obj = URLS_TO_OBJ
        self.obj_to_urls = OBJ_TO_URL
        self.sign_url_cases = SIGN_URL_CASES

    def test_pixelbin_config_and_client(self):
        self.assertEqual(self.pixelbinConfig.domain, self.config["domain"])
        self.assertEqual(self.pixelbinConfig.apiSecret, self.config["apiSecret"])

        from pixelbin.platform.PixelbinClient import Assets, Organization

        self.assertEqual(self.pixelbinClient.config, self.pixelbinConfig)
        self.assertIsInstance(self.pixelbinClient.assets, Assets)
        self.assertIsInstance(self.pixelbinClient.organization, Organization)

    def test_pixelbin_config_token_1(self):
        with self.assertRaises(Exception) as context:
            from pixelbin import PixelbinConfig, PixelbinClient

            config = PixelbinConfig(
                {
                    "domain": "https://api.pixelbin.io",
                }
            )
            PixelbinClient(config)
        self.assertIsInstance(context.exception, PixelbinInvalidCredentialError)
        self.assertTrue("No API Secret Token Present" in str(context.exception))

    def test_pixelbin_config_token_2(self):
        with self.assertRaises(Exception) as context:
            from pixelbin import PixelbinConfig, PixelbinClient

            config = PixelbinConfig(
                {
                    "domain": "https://api.pixelbin.io",
                    "apiSecret": "abc",
                }
            )
            PixelbinClient(config)
        self.assertIsInstance(context.exception, PixelbinInvalidCredentialError)
        self.assertTrue("Invalid API Secret Token" in str(context.exception))

    def test_createFolder(self):
        with mock.patch(
            "pixelbin.common.aiohttp_helper.AiohttpHelper.request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["createFolder"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.createFolder(
                name=self.folder_name, path=self.folder_path
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))
            mock_request.assert_called_with(
                method="post",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/folders",
                params={},
                data={"name": "testdir", "path": "/"},
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                trust_env=False,
            )

    def test_fileUpload_case1(self):
        form_data = FormData()
        with mock.patch.object(
            form_data, "add_field", wraps=form_data.add_field
        ) as spy_add_field:
            with mock.patch.object(
                AiohttpHelper, "_AiohttpHelper__get_formdata"
            ) as mock_get_formdata:
                mock_get_formdata.return_value = form_data
                with mock.patch.object(
                    AiohttpHelper, "_AiohttpHelper__make_request"
                ) as mock_request:
                    mock_response = MOCK_RESPONSE["fileUpload1"]["response"]
                    mock_request.return_value = mock_response
                    file = open("./tests/1.jpeg", "rb")
                    resp = self.pixelbinClient.assets.fileUpload(file=file)

                    formdata = mock_request.call_args.kwargs["data"]
                    self.assertIsInstance(formdata, FormData)
                    spy_add_field.assert_has_calls(
                        calls=[mock.call("file", file)], any_order=True
                    )
                    mock_request.assert_called_with(
                        method="post",
                        url=f"{CONFIG['domain']}/service/platform/assets/v1.0/upload/direct",
                        params={},
                        data=mock.ANY,
                        headers={
                            "host": CONFIG["host"],
                            "Authorization": BEARER_TOKEN,
                        },
                        timeout_allowed=mock.ANY,
                        trust_env=False,
                    )
                    self.assertDictEqual(
                        resp, json.loads(mock_response["content"].decode())
                    )

    def test_fileUpload_case2(self):
        form_data = FormData()
        with mock.patch.object(
            form_data, "add_field", wraps=form_data.add_field
        ) as spy_add_field:
            with mock.patch.object(
                AiohttpHelper, "_AiohttpHelper__get_formdata"
            ) as mock_get_formdata:
                mock_get_formdata.return_value = form_data
                with mock.patch.object(
                    AiohttpHelper, "_AiohttpHelper__make_request"
                ) as mock_request:
                    mock_response = MOCK_RESPONSE["fileUpload2"]["response"]
                    mock_request.return_value = mock_response
                    tags = ["tag1", "tag2"]
                    file = open("./tests/1.jpeg", "rb")
                    resp = self.pixelbinClient.assets.fileUpload(
                        file=file,
                        path=self.folder_name,
                        name="1",
                        access="public-read",
                        tags=tags,
                        metadata={},
                        overwrite=False,
                        filenameOverride=True,
                    )

                    formdata = mock_request.call_args.kwargs["data"]
                    self.assertIsInstance(formdata, FormData)
                    spy_add_field.assert_has_calls(
                        calls=[
                            mock.call("file", file),
                            mock.call("path", "testdir"),
                            mock.call("name", "1"),
                            mock.call("access", "public-read"),
                            mock.call("tags", "tag1"),
                            mock.call("tags", "tag2"),
                            mock.call("metadata", "{}"),
                            mock.call("overwrite", "false"),
                            mock.call("filenameOverride", "true"),
                        ],
                        any_order=True,
                    )
                    mock_request.assert_called_with(
                        method="post",
                        url=f"{CONFIG['domain']}/service/platform/assets/v1.0/upload/direct",
                        params={},
                        data=mock.ANY,
                        headers={
                            "host": CONFIG["host"],
                            "Authorization": BEARER_TOKEN,
                        },
                        timeout_allowed=mock.ANY,
                        trust_env=False,
                    )
                    self.assertDictEqual(
                        resp, json.loads(mock_response["content"].decode())
                    )

    def test_fileUpload_access(self):
        with self.assertRaises(Exception) as context:
            tags = ["tag1", "tag2"]
            file = open("./tests/1.jpeg", "rb")
            resp = self.pixelbinClient.assets.fileUpload(
                file=file,
                path=self.folder_name,
                name="1",
                access="public",
                tags=tags,
                metadata={},
                overwrite=False,
                filenameOverride=True,
            )
        self.assertTrue(
            "Must be one of: public-read, private." in str(context.exception)
        )

    def test_getFileById(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getFileById"]["response"]
            _id = "9d331030-b695-475e-9d4a-a660696d5fa5"
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.getFileById(_id=_id)
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/files/id/{_id}",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_list_files_case1(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["listFiles1"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.listFiles()
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/listFiles",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_listFiles_case2(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["listFiles2"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.listFiles(
                name="1",
                path=self.folder_name,
                format="jpeg",
                tags=["tag1", "tag2"],
                onlyFiles=True,
                onlyFolders=False,
                pageNo=1,
                pageSize=10,
                sort="name",
            )
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/listFiles",
                params={
                    "name": "1",
                    "path": "testdir",
                    "format": "jpeg",
                    "tags[0]": "tag1",
                    "tags[1]": "tag2",
                    "onlyFiles": "true",
                    "pageNo": 1,
                    "pageSize": 10,
                    "sort": "name",
                },
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_urlUpload(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["urlUpload"]["response"]
            mock_request.return_value = mock_response
            tags = ["cat", "animal"]
            resp = self.pixelbinClient.assets.urlUpload(
                url="https://www.fetchfind.com/blog/wp-content/uploads/2017/08/cat-2734999_1920-5-common-cat-sounds.jpg",
                path=self.folder_name,
                name="2",
                access="public-read",
                tags=tags,
                metadata={},
                overwrite=False,
                filenameOverride=True,
            )
            mock_data = ujson.dumps(
                {
                    "url": "https://www.fetchfind.com/blog/wp-content/uploads/2017/08/cat-2734999_1920-5-common-cat-sounds.jpg",
                    "path": self.folder_name,
                    "name": "2",
                    "access": "public-read",
                    "tags": ["cat", "animal"],
                    "metadata": {},
                    "overwrite": False,
                    "filenameOverride": True,
                },
                escape_forward_slashes=False,
            )
            mock_request.assert_called_with(
                method="post",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/upload/url",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_createSignedUrl_case1(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["createSignedURL1"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.createSignedUrl()
            mock_request.assert_called_with(
                method="post",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/upload/signed-url",
                params={},
                data={},
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_createSignedUrl_case2(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["createSignedURL2"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.createSignedUrl(
                name="1",
                path=self.folder_name,
                format="jpeg",
                access="public-read",
                tags=["tag1", "tag2"],
                metadata={},
                overwrite=False,
                filenameOverride=True,
            )
            mock_data = ujson.dumps(
                {
                    "name": "1",
                    "path": "testdir",
                    "format": "jpeg",
                    "access": "public-read",
                    "tags": ["tag1", "tag2"],
                    "metadata": {},
                    "overwrite": False,
                    "filenameOverride": True,
                },
                escape_forward_slashes=False,
            )
            mock_request.assert_called_with(
                method="post",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/upload/signed-url",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_createSignedUrlV2_case1(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["createSignedURLV2_1"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.createSignedUrlV2()
            mock_request.assert_called_with(
                method="post",
                url=f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url",
                params={},
                data={},
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_createSignedUrlV2_case2(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["createSignedURL2"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.createSignedUrlV2(
                name="1",
                path=self.folder_name,
                format="jpeg",
                access="public-read",
                tags=["tag1", "tag2"],
                metadata={},
                overwrite=False,
                filenameOverride=True,
            )
            mock_data = ujson.dumps(
                {
                    "name": "1",
                    "path": "testdir",
                    "format": "jpeg",
                    "access": "public-read",
                    "tags": ["tag1", "tag2"],
                    "metadata": {},
                    "overwrite": False,
                    "filenameOverride": True,
                },
                escape_forward_slashes=False,
            )
            mock_request.assert_called_with(
                method="post",
                url=f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_updateFile_case1(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["updateFile1"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.updateFile(fileId="1", name=f"1_")
            mock_data = ujson.dumps(
                {
                    "name": "1_",
                },
                escape_forward_slashes=False,
            )
            mock_request.assert_called_with(
                method="patch",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/files/1",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_updateFile_case2(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["updateFile2"]["response"]
            mock_request.return_value = mock_response
            tags = ["updated-tag1", "updated-tag2"]
            resp = self.pixelbinClient.assets.updateFile(
                fileId=f"{self.folder_name}/1",
                name=f"{self.folder_name}_",
                path=self.folder_name,
                access="private",
                isActive=True,
                tags=tags,
                metadata={"key": "value"},
            )
            mock_data = ujson.dumps(
                {
                    "name": f"{self.folder_name}_",
                    "path": f"{self.folder_name}",
                    "access": "private",
                    "isActive": True,
                    "tags": ["updated-tag1", "updated-tag2"],
                    "metadata": {"key": "value"},
                },
                escape_forward_slashes=False,
            )
            mock_request.assert_called_with(
                method="patch",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/files/{self.folder_name}/1",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_getFileByFileId(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getFileByFileId"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.getFileByFileId(
                fileId=f"{self.folder_name}/2"
            )
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/files/{self.folder_name}/2",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_deleteFile(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["deleteFile"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.deleteFile(fileId="1_")
            mock_request.assert_called_with(
                method="delete",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/files/1_",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_deleteFiles(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["deleteFiles"]["response"]
            mock_request.return_value = mock_response
            _ids = [
                "9d331030-b695-475e-9d4a-a660696d5fa5",
                "aaf3f9c4-18bc-4aa5-8cac-2c45dd8df889",
            ]
            mock_data = ujson.dumps(
                {"ids": _ids},
                escape_forward_slashes=False,
            )
            resp = self.pixelbinClient.assets.deleteFiles(ids=_ids)
            mock_request.assert_called_with(
                method="post",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/files/delete",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertEqual(resp, json.loads(mock_response["content"].decode()))

    def test_updateFolder(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["updateFolder"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.updateFolder(
                folderId=f"{self.folder_name}", isActive=True
            )
            mock_data = ujson.dumps(
                {"isActive": True},
                escape_forward_slashes=False,
            )
            mock_request.assert_called_with(
                method="patch",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/folders/testdir",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_getFolderDetails(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getFolderDetails"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.getFolderDetails(
                path="", name=self.folder_name
            )
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/folders",
                params={"name": "testdir"},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_getFolderAncestors(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            folder_id = "4a08fc27-e8ee-4e2d-9438-85c1ba07423e"
            mock_response = MOCK_RESPONSE["getFolderAncestors"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.getFolderAncestors(_id=folder_id)
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/folders/{folder_id}/ancestors",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_deleteFolder(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            folder_id = "b89b2fbb-c520-444a-98a4-f3c20276c0a3"
            mock_response = MOCK_RESPONSE["deleteFolder"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.deleteFolder(_id=folder_id)
            mock_request.assert_called_with(
                method="delete",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/folders/{folder_id}",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_getModules(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getModules"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.getModules()
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/playground/plugins",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_getModule(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getModule"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.getModule(identifier="erase")
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/playground/plugins/erase",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_addCredentials(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            apiKey = MOCK_RESPONSE["updateCredentials"]["apiKey"]
            mock_response = MOCK_RESPONSE["addCredentials"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.addCredentials(
                credentials={"apiKey": apiKey}, pluginId="remove"
            )
            mock_data = ujson.dumps(
                {
                    "credentials": {"apiKey": f"{apiKey}"},
                    "pluginId": "remove",
                },
                escape_forward_slashes=False,
            )
            mock_request.assert_called_with(
                method="post",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/credentials",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_updateCredentials(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            apiKey = MOCK_RESPONSE["updateCredentials"]["apiKey"]
            mock_response = MOCK_RESPONSE["updateCredentials"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.updateCredentials(
                credentials={"apiKey": apiKey}, pluginId="remove"
            )
            mock_data = ujson.dumps(
                {
                    "credentials": {"apiKey": f"{apiKey}"},
                },
                escape_forward_slashes=False,
            )
            mock_request.assert_called_with(
                method="patch",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/credentials/remove",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_deleteCredentials(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["deleteCredentials"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.deleteCredentials(pluginId="remove")
            mock_request.assert_called_with(
                method="delete",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/credentials/remove",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_addPreset(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["addPreset"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.addPreset(
                presetName="p1",
                transformation="t.flip()~t.flop()",
                params={
                    "w": {"type": "integer", "default": 200},
                    "h": {"type": "integer", "default": 400},
                },
            )
            mock_data = ujson.dumps(
                {
                    "presetName": "p1",
                    "transformation": "t.flip()~t.flop()",
                    "params": {
                        "w": {"type": "integer", "default": 200},
                        "h": {"type": "integer", "default": 400},
                    },
                },
                escape_forward_slashes=False,
            )
            mock_request.assert_called_with(
                method="post",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/presets",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_getPresets(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getPresets"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.getPresets()
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/presets",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_updatePresets(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["updatePresets"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.updatePreset(
                presetName="p1", archived=True
            )
            mock_data = ujson.dumps(
                {
                    "archived": True,
                },
                escape_forward_slashes=False,
            )
            mock_request.assert_called_with(
                method="patch",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/presets/p1",
                params={},
                data=mock_data,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                    "Content-Type": "application/json",
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_getPreset(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getPreset"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.getPreset(presetName="p1")
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/presets/p1",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_deletePreset(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["deletePreset"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.deletePreset(presetName="p1")
            mock_request.assert_called_with(
                method="delete",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/presets/p1",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_getDefaultAssetForPlayground(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getDefaultAssetForPlayground"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.assets.getDefaultAssetForPlayground()
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/playground/default",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_getAppOrgDetails(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getAppOrgDetails"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.organization.getAppOrgDetails()
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/organization/v1.0/apps/info",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertEqual(resp, json.loads(mock_response["content"].decode()))

    def test_getTransformationContext(self):
        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getTransformationContext"]["response"]
            mock_request.return_value = mock_response
            resp = self.pixelbinClient.transformation.getTransformationContext(
                # provide link of your image
                url="/v2/still-band-3297fc/original/test.webp"
            )
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/transformation/context",
                params={"url": "/v2/still-band-3297fc/original/test.webp"},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=False,
            )
            self.assertEqual(resp, json.loads(mock_response["content"].decode()))

    def test_url_to_obj(self):
        from pixelbin.utils.url import url_to_obj

        for case in self.urls_to_obj:
            url = case["url"]
            opts = case["opts"]
            expected_obj = case["obj"]
            try:
                obj = url_to_obj(url, opts=opts)
                self.assertDictEqual(obj, expected_obj)
            except Exception as err:
                self.assertEqual(err.args[0], case["error"])

    def test_obj_to_url(self):
        from pixelbin.utils.url import obj_to_url

        for case in self.obj_to_urls:
            obj = case["obj"]
            expected_url = case["url"]
            try:
                url = obj_to_url(obj)
                self.assertEqual(url, expected_url)
            except Exception as err:
                self.assertEqual(err.args[0], case["error"])

    def test_failure_for_option_dpr_queryParam(self):
        from pixelbin.common.exceptions import PixelbinIllegalQueryParameterError
        from pixelbin.utils.url import obj_to_url

        obj = {
            "baseUrl": "https://cdn.pixelbin.io",
            "filePath": "__playground/playground-default.jpeg",
            "version": "v2",
            "zone": "z-slug",
            "cloudName": "red-scene-95b6ea",
            "options": {"dpr": 5.5},
            "transformations": [{}],
        }
        with self.assertRaises(
            PixelbinIllegalQueryParameterError,
            msg="DPR value should be numeric and should be between 0.1 to 5.0",
        ):
            obj_to_url(obj)

    def test_failure_for_option_fauto_queryParam(self):
        from pixelbin.common.exceptions import PixelbinIllegalQueryParameterError
        from pixelbin.utils.url import obj_to_url

        obj = {
            "baseUrl": "https://cdn.pixelbin.io",
            "filePath": "__playground/playground-default.jpeg",
            "version": "v2",
            "zone": "z-slug",
            "cloudName": "red-scene-95b6ea",
            "options": {"f_auto": "abc"},
            "transformations": [{}],
        }
        with self.assertRaises(
            PixelbinIllegalQueryParameterError, msg="F_auto value should be boolean"
        ):
            obj_to_url(obj)

    def test_should_sign_url(self):
        from pixelbin.utils.security import sign_url

        for case in self.sign_url_cases:
            args = case["input"]
            try:
                signed_url = sign_url(
                    url=args["url"],
                    expiry_seconds=args["expiry_seconds"],
                    access_key=args["access_key"],
                    token=args["token"],
                )
                parsed_url = parse.urlparse(signed_url)
                parsed_qs = parse.parse_qs(parsed_url.query)
                self.assertTrue("pbs" in parsed_qs)
                self.assertTrue("pbe" in parsed_qs)
                self.assertTrue("pbt" in parsed_qs)
            except Exception as err:
                self.assertEqual(err.args[0], case["error"])

    def test_should_pass_trust_env_true(self):
        from pixelbin import PixelbinConfig, PixelbinClient

        TEST_CONFIG = {
            "host": "api.pixelbin.io",
            "domain": "https://api.pixelbin.io",
            "apiSecret": "token",
            "options": {"httpClientOptions": {"trust_env": True}},
        }
        pixelbinConfig = PixelbinConfig(config=TEST_CONFIG)
        pixelbinClient = PixelbinClient(config=pixelbinConfig)

        with mock.patch.object(
            AiohttpHelper, "_AiohttpHelper__make_request"
        ) as mock_request:
            mock_response = MOCK_RESPONSE["getPresets"]["response"]
            mock_request.return_value = mock_response
            resp = pixelbinClient.assets.getPresets()
            mock_request.assert_called_with(
                method="get",
                url=f"{CONFIG['domain']}/service/platform/assets/v1.0/presets",
                params={},
                data=None,
                headers={
                    "host": CONFIG["host"],
                    "Authorization": BEARER_TOKEN,
                },
                timeout_allowed=mock.ANY,
                trust_env=True,
            )
            self.assertDictEqual(resp, json.loads(mock_response["content"].decode()))

    def test_uploader_upload_buffer(self):
        def make_request_side_effect(**kwargs):
            method = kwargs.get("method")
            if method == "put":
                return MOCK_RESPONSE["multipartUploadChunkUpload"]["response"]
            elif method == "post":
                if (
                    kwargs.get("url")
                    == f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url"
                ):
                    return MOCK_RESPONSE["createSignedURLV2_1"]["response"]
                else:
                    return MOCK_RESPONSE["multipartUploadCompleteUpload"]["response"]
            else:
                raise Exception("Invalid request")

        form_data = FormData()
        with mock.patch.object(
            form_data, "add_field", wraps=form_data.add_field
        ) as spy_add_field:
            with mock.patch.object(
                AiohttpHelper, "_AiohttpHelper__get_formdata"
            ) as mock_get_formdata:
                mock_get_formdata.return_value = form_data
                with mock.patch.object(
                    AiohttpHelper, "_AiohttpHelper__make_request"
                ) as mock_request:
                    mock_response = MOCK_RESPONSE["multipartUploadCompleteUpload"][
                        "response"
                    ]
                    mock_request.side_effect = make_request_side_effect
                    file = open("./tests/1.jpeg", "rb")
                    file = file.read()
                    self.assertEqual(len(file), 11732)
                    chunk1 = file[: 6 * 1024]
                    chunk2 = file[6 * 1024 :]

                    resp = self.pixelbinClient.uploader.upload(
                        file=file, uploadOptions={"chunkSize": 6 * 1024}
                    )

                    spy_add_field.assert_has_calls(
                        calls=[
                            mock.call("file", chunk1),
                            mock.call(
                                "x-pixb-meta-assetdata",
                                '{"orgId":3308,"type":"file","name":"asset-8WhaVptV2.jpeg","path":"","fileId":"asset-8WhaVptV2.jpeg","format":"jpeg","s3Bucket":"erase-erase-erasebg-assets","s3Key":"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg","access":"public-read","tags":[],"metadata":{"source":"signedUrl","publicUploadId":"376a20ef-cf61-469d-a90f-c35177cc1dd6"},"overwrite":false,"filenameOverride":false}',
                            ),
                            mock.call("file", chunk2),
                            mock.call(
                                "x-pixb-meta-assetdata",
                                '{"orgId":3308,"type":"file","name":"asset-8WhaVptV2.jpeg","path":"","fileId":"asset-8WhaVptV2.jpeg","format":"jpeg","s3Bucket":"erase-erase-erasebg-assets","s3Key":"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg","access":"public-read","tags":[],"metadata":{"source":"signedUrl","publicUploadId":"376a20ef-cf61-469d-a90f-c35177cc1dd6"},"overwrite":false,"filenameOverride":false}',
                            ),
                        ]
                    )

                    self.assertEqual(
                        mock_request.call_args_list,
                        [
                            mock.call(
                                method="post",
                                url=f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url",
                                params={},
                                data={},
                                headers={
                                    "host": CONFIG["host"],
                                    "Authorization": BEARER_TOKEN,
                                },
                                timeout_allowed=mock.ANY,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=1",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=2",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                            mock.call(
                                method="post",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6",
                                params={},
                                data='{"parts":[1,2],"x-pixb-meta-assetdata":"{\\"orgId\\":3308,\\"type\\":\\"file\\",\\"name\\":\\"asset-8WhaVptV2.jpeg\\",\\"path\\":\\"\\",\\"fileId\\":\\"asset-8WhaVptV2.jpeg\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erase-erasebg-assets\\",\\"s3Key\\":\\"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[],\\"metadata\\":{\\"source\\":\\"signedUrl\\",\\"publicUploadId\\":\\"376a20ef-cf61-469d-a90f-c35177cc1dd6\\"},\\"overwrite\\":false,\\"filenameOverride\\":false}"}',
                                headers={"Content-Type": "application/json"},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                        ],
                    )
                    self.assertDictEqual(
                        resp, json.loads(mock_response["content"].decode())
                    )

    def test_uploader_upload_stream(self):
        def make_request_side_effect(**kwargs):
            method = kwargs.get("method")
            if method == "put":
                return MOCK_RESPONSE["multipartUploadChunkUpload"]["response"]
            elif method == "post":
                if (
                    kwargs.get("url")
                    == f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url"
                ):
                    return MOCK_RESPONSE["createSignedURLV2_1"]["response"]
                else:
                    return MOCK_RESPONSE["multipartUploadCompleteUpload"]["response"]
            else:
                raise Exception("Invalid request")

        form_data = FormData()
        with mock.patch.object(
            form_data, "add_field", wraps=form_data.add_field
        ) as spy_add_field:
            with mock.patch.object(
                AiohttpHelper, "_AiohttpHelper__get_formdata"
            ) as mock_get_formdata:
                mock_get_formdata.return_value = form_data
                with mock.patch.object(
                    AiohttpHelper, "_AiohttpHelper__make_request"
                ) as mock_request:
                    mock_response = MOCK_RESPONSE["multipartUploadCompleteUpload"][
                        "response"
                    ]
                    mock_request.side_effect = make_request_side_effect

                    file = open("./tests/1.jpeg", "rb")
                    file = file.read()
                    self.assertEqual(len(file), 11732)
                    chunk1 = file[: 6 * 1024]
                    chunk2 = file[6 * 1024 :]

                    resp = self.pixelbinClient.uploader.upload(
                        file=open("./tests/1.jpeg", "rb"),
                        uploadOptions={"chunkSize": 6 * 1024},
                    )

                    spy_add_field.assert_has_calls(
                        calls=[
                            mock.call("file", chunk1),
                            mock.call(
                                "x-pixb-meta-assetdata",
                                '{"orgId":3308,"type":"file","name":"asset-8WhaVptV2.jpeg","path":"","fileId":"asset-8WhaVptV2.jpeg","format":"jpeg","s3Bucket":"erase-erase-erasebg-assets","s3Key":"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg","access":"public-read","tags":[],"metadata":{"source":"signedUrl","publicUploadId":"376a20ef-cf61-469d-a90f-c35177cc1dd6"},"overwrite":false,"filenameOverride":false}',
                            ),
                            mock.call("file", chunk2),
                            mock.call(
                                "x-pixb-meta-assetdata",
                                '{"orgId":3308,"type":"file","name":"asset-8WhaVptV2.jpeg","path":"","fileId":"asset-8WhaVptV2.jpeg","format":"jpeg","s3Bucket":"erase-erase-erasebg-assets","s3Key":"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg","access":"public-read","tags":[],"metadata":{"source":"signedUrl","publicUploadId":"376a20ef-cf61-469d-a90f-c35177cc1dd6"},"overwrite":false,"filenameOverride":false}',
                            ),
                        ]
                    )

                    self.assertEqual(
                        mock_request.call_args_list,
                        [
                            mock.call(
                                method="post",
                                url=f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url",
                                params={},
                                data={},
                                headers={
                                    "host": CONFIG["host"],
                                    "Authorization": BEARER_TOKEN,
                                },
                                timeout_allowed=mock.ANY,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=1",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=2",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                            mock.call(
                                method="post",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6",
                                params={},
                                data='{"parts":[1,2],"x-pixb-meta-assetdata":"{\\"orgId\\":3308,\\"type\\":\\"file\\",\\"name\\":\\"asset-8WhaVptV2.jpeg\\",\\"path\\":\\"\\",\\"fileId\\":\\"asset-8WhaVptV2.jpeg\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erase-erasebg-assets\\",\\"s3Key\\":\\"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[],\\"metadata\\":{\\"source\\":\\"signedUrl\\",\\"publicUploadId\\":\\"376a20ef-cf61-469d-a90f-c35177cc1dd6\\"},\\"overwrite\\":false,\\"filenameOverride\\":false}"}',
                                headers={"Content-Type": "application/json"},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                        ],
                    )
                    self.assertDictEqual(
                        resp, json.loads(mock_response["content"].decode())
                    )

    def test_uploader_upload_dont_retry_on_4xx(self):
        def make_request_side_effect(**kwargs):
            method = kwargs.get("method")
            if method == "put":
                return MOCK_RESPONSE["multipartUploadChunkUploadFailed"]["response"]
            elif method == "post":
                if (
                    kwargs.get("url")
                    == f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url"
                ):
                    return MOCK_RESPONSE["createSignedURLV2_1"]["response"]
            else:
                raise Exception("Invalid request")

        form_data = FormData()
        with mock.patch.object(
            form_data, "add_field", wraps=form_data.add_field
        ) as spy_add_field:
            with mock.patch.object(
                AiohttpHelper, "_AiohttpHelper__get_formdata"
            ) as mock_get_formdata:
                mock_get_formdata.return_value = form_data
                with mock.patch.object(
                    AiohttpHelper, "_AiohttpHelper__make_request"
                ) as mock_request:
                    mock_response = MOCK_RESPONSE["multipartUploadChunkUploadFailed"][
                        "response"
                    ]
                    mock_request.side_effect = make_request_side_effect
                    file = open("./tests/1.jpeg", "rb")
                    file = file.read()
                    self.assertEqual(len(file), 11732)
                    chunk1 = file[: 6 * 1024]
                    chunk2 = file[6 * 1024 :]

                    try:
                        self.pixelbinClient.uploader.upload(
                            file=file, uploadOptions={"chunkSize": 6 * 1024}
                        )
                        raise Exception("Request should have failed")
                    except PixelbinServerResponseError as e:
                        self.assertEqual(e.status_code, mock_response["status_code"])

                    spy_add_field.assert_has_calls(
                        calls=[
                            mock.call("file", chunk1),
                            mock.call(
                                "x-pixb-meta-assetdata",
                                '{"orgId":3308,"type":"file","name":"asset-8WhaVptV2.jpeg","path":"","fileId":"asset-8WhaVptV2.jpeg","format":"jpeg","s3Bucket":"erase-erase-erasebg-assets","s3Key":"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg","access":"public-read","tags":[],"metadata":{"source":"signedUrl","publicUploadId":"376a20ef-cf61-469d-a90f-c35177cc1dd6"},"overwrite":false,"filenameOverride":false}',
                            ),
                            mock.call("file", chunk2),
                            mock.call(
                                "x-pixb-meta-assetdata",
                                '{"orgId":3308,"type":"file","name":"asset-8WhaVptV2.jpeg","path":"","fileId":"asset-8WhaVptV2.jpeg","format":"jpeg","s3Bucket":"erase-erase-erasebg-assets","s3Key":"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg","access":"public-read","tags":[],"metadata":{"source":"signedUrl","publicUploadId":"376a20ef-cf61-469d-a90f-c35177cc1dd6"},"overwrite":false,"filenameOverride":false}',
                            ),
                        ]
                    )

                    self.assertEqual(
                        mock_request.call_args_list,
                        [
                            mock.call(
                                method="post",
                                url=f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url",
                                params={},
                                data={},
                                headers={
                                    "host": CONFIG["host"],
                                    "Authorization": BEARER_TOKEN,
                                },
                                timeout_allowed=mock.ANY,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=1",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=2",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                        ],
                    )

    def test_uploader_upload_retry(self):
        put_request_count = 0

        def make_request_side_effect(**kwargs):
            method = kwargs.get("method")
            if method == "put":
                nonlocal put_request_count
                if put_request_count == 0:
                    put_request_count += 1
                    return MOCK_RESPONSE["multipartUploadChunkUploadFailed2"][
                        "response"
                    ]
                return MOCK_RESPONSE["multipartUploadChunkUpload"]["response"]
            elif method == "post":
                if (
                    kwargs.get("url")
                    == f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url"
                ):
                    return MOCK_RESPONSE["createSignedURLV2_1"]["response"]
                else:
                    return MOCK_RESPONSE["multipartUploadCompleteUpload"]["response"]
            else:
                raise Exception("Invalid request")

        form_data = FormData()
        with mock.patch.object(
            form_data, "add_field", wraps=form_data.add_field
        ) as spy_add_field:
            with mock.patch.object(
                AiohttpHelper, "_AiohttpHelper__get_formdata"
            ) as mock_get_formdata:
                mock_get_formdata.return_value = form_data
                with mock.patch.object(
                    AiohttpHelper, "_AiohttpHelper__make_request"
                ) as mock_request:
                    mock_response = MOCK_RESPONSE["multipartUploadCompleteUpload"][
                        "response"
                    ]
                    mock_request.side_effect = make_request_side_effect
                    file = open("./tests/1.jpeg", "rb")
                    file = file.read()
                    self.assertEqual(len(file), 11732)
                    chunk1 = file[: 6 * 1024]
                    chunk2 = file[6 * 1024 :]

                    resp = self.pixelbinClient.uploader.upload(
                        file=file,
                        uploadOptions={
                            "chunkSize": 6 * 1024,
                            "maxRetries": 1,
                            "exponentialFactor": 1,
                        },
                    )

                    spy_add_field.assert_has_calls(
                        calls=[
                            mock.call("file", chunk1),
                            mock.call(
                                "x-pixb-meta-assetdata",
                                '{"orgId":3308,"type":"file","name":"asset-8WhaVptV2.jpeg","path":"","fileId":"asset-8WhaVptV2.jpeg","format":"jpeg","s3Bucket":"erase-erase-erasebg-assets","s3Key":"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg","access":"public-read","tags":[],"metadata":{"source":"signedUrl","publicUploadId":"376a20ef-cf61-469d-a90f-c35177cc1dd6"},"overwrite":false,"filenameOverride":false}',
                            ),
                            mock.call("file", chunk2),
                            mock.call(
                                "x-pixb-meta-assetdata",
                                '{"orgId":3308,"type":"file","name":"asset-8WhaVptV2.jpeg","path":"","fileId":"asset-8WhaVptV2.jpeg","format":"jpeg","s3Bucket":"erase-erase-erasebg-assets","s3Key":"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg","access":"public-read","tags":[],"metadata":{"source":"signedUrl","publicUploadId":"376a20ef-cf61-469d-a90f-c35177cc1dd6"},"overwrite":false,"filenameOverride":false}',
                            ),
                        ]
                    )

                    self.assertEqual(
                        mock_request.call_args_list,
                        [
                            mock.call(
                                method="post",
                                url=f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url",
                                params={},
                                data={},
                                headers={
                                    "host": CONFIG["host"],
                                    "Authorization": BEARER_TOKEN,
                                },
                                timeout_allowed=mock.ANY,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=1",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=2",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=1",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                            mock.call(
                                method="post",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6",
                                params={},
                                data='{"parts":[1,2],"x-pixb-meta-assetdata":"{\\"orgId\\":3308,\\"type\\":\\"file\\",\\"name\\":\\"asset-8WhaVptV2.jpeg\\",\\"path\\":\\"\\",\\"fileId\\":\\"asset-8WhaVptV2.jpeg\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erase-erasebg-assets\\",\\"s3Key\\":\\"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[],\\"metadata\\":{\\"source\\":\\"signedUrl\\",\\"publicUploadId\\":\\"376a20ef-cf61-469d-a90f-c35177cc1dd6\\"},\\"overwrite\\":false,\\"filenameOverride\\":false}"}',
                                headers={"Content-Type": "application/json"},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                        ],
                    )
                    self.assertDictEqual(
                        resp, json.loads(mock_response["content"].decode())
                    )

    def test_uploader_upload_0_maxRetries(self):

        def make_request_side_effect(**kwargs):
            method = kwargs.get("method")
            if method == "put":
                return MOCK_RESPONSE["multipartUploadChunkUploadFailed2"]["response"]
            elif method == "post" and (
                kwargs.get("url")
                == f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url"
            ):
                return MOCK_RESPONSE["createSignedURLV2_1"]["response"]
            else:
                raise Exception("Invalid request")

        form_data = FormData()
        with mock.patch.object(
            form_data, "add_field", wraps=form_data.add_field
        ) as spy_add_field:
            with mock.patch.object(
                AiohttpHelper, "_AiohttpHelper__get_formdata"
            ) as mock_get_formdata:
                mock_get_formdata.return_value = form_data
                with mock.patch.object(
                    AiohttpHelper, "_AiohttpHelper__make_request"
                ) as mock_request:
                    mock_response = MOCK_RESPONSE["multipartUploadChunkUploadFailed2"][
                        "response"
                    ]
                    mock_request.side_effect = make_request_side_effect
                    file = open("./tests/1.jpeg", "rb")
                    file = file.read()
                    self.assertEqual(len(file), 11732)
                    chunk1 = file[: 6 * 1024]
                    chunk2 = file[6 * 1024 :]

                    try:
                        self.pixelbinClient.uploader.upload(
                            file=file,
                            uploadOptions={
                                "chunkSize": 6 * 1024,
                                "maxRetries": 0,
                                "exponentialFactor": 1,
                            },
                        )
                        raise Exception("Request should have failed")
                    except Exception as e:
                        self.assertEqual(e.status_code, mock_response["status_code"])

                    spy_add_field.assert_has_calls(
                        calls=[
                            mock.call("file", chunk1),
                            mock.call(
                                "x-pixb-meta-assetdata",
                                '{"orgId":3308,"type":"file","name":"asset-8WhaVptV2.jpeg","path":"","fileId":"asset-8WhaVptV2.jpeg","format":"jpeg","s3Bucket":"erase-erase-erasebg-assets","s3Key":"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg","access":"public-read","tags":[],"metadata":{"source":"signedUrl","publicUploadId":"376a20ef-cf61-469d-a90f-c35177cc1dd6"},"overwrite":false,"filenameOverride":false}',
                            ),
                            mock.call("file", chunk2),
                            mock.call(
                                "x-pixb-meta-assetdata",
                                '{"orgId":3308,"type":"file","name":"asset-8WhaVptV2.jpeg","path":"","fileId":"asset-8WhaVptV2.jpeg","format":"jpeg","s3Bucket":"erase-erase-erasebg-assets","s3Key":"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg","access":"public-read","tags":[],"metadata":{"source":"signedUrl","publicUploadId":"376a20ef-cf61-469d-a90f-c35177cc1dd6"},"overwrite":false,"filenameOverride":false}',
                            ),
                        ]
                    )

                    self.assertEqual(
                        mock_request.call_args_list,
                        [
                            mock.call(
                                method="post",
                                url=f"{CONFIG['domain']}/service/platform/assets/v2.0/upload/signed-url",
                                params={},
                                data={},
                                headers={
                                    "host": CONFIG["host"],
                                    "Authorization": BEARER_TOKEN,
                                },
                                timeout_allowed=mock.ANY,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=1",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                            mock.call(
                                method="put",
                                url="https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=2",
                                params={},
                                data=mock.ANY,
                                headers={},
                                timeout_allowed=15,
                                trust_env=False,
                            ),
                        ],
                    )

    # Test cases for invalid `chunkSize` values
    def test_invalid_chunk_size_type(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"chunkSize": "invalid"})
        self.assertEqual(str(context.exception), "Invalid chunkSize: Must be a positive integer.")

    def test_invalid_chunk_size_value(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"chunkSize": -1})
        self.assertEqual(str(context.exception), "Invalid chunkSize: Must be a positive integer.")

    def test_invalid_chunk_size_float(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"chunkSize": 10.5})
        self.assertEqual(str(context.exception), "Invalid chunkSize: Must be a positive integer.")

    # Test cases for invalid `maxRetries` values
    def test_invalid_max_retries_type(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"maxRetries": "invalid"})
        self.assertEqual(str(context.exception), "Invalid maxRetries: Must be a non-negative integer.")

    def test_invalid_max_retries_value(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"maxRetries": -1})
        self.assertEqual(str(context.exception), "Invalid maxRetries: Must be a non-negative integer.")

    def test_invalid_max_retries_float(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"maxRetries": 1.5})
        self.assertEqual(str(context.exception), "Invalid maxRetries: Must be a non-negative integer.")

    # Test cases for invalid `concurrency` values
    def test_invalid_concurrency_type(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"concurrency": "invalid"})
        self.assertEqual(str(context.exception), "Invalid concurrency: Must be a positive integer.")

    def test_invalid_concurrency_value(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"concurrency": 0})
        self.assertEqual(str(context.exception), "Invalid concurrency: Must be a positive integer.")

    def test_invalid_concurrency_float(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"concurrency": 2.5})
        self.assertEqual(str(context.exception), "Invalid concurrency: Must be a positive integer.")

    # Test cases for `exponentialFactor` values
    def test_invalid_exponential_factor_type(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"exponentialFactor": "invalid"})
        self.assertEqual(str(context.exception), "Invalid exponentialFactor: Must be a positive number.")

    def test_invalid_exponential_factor_value(self):
        with self.assertRaises(PixelbinIllegalArgumentError) as context:
            self.pixelbinClient.uploader.upload(file="dummy_file", uploadOptions={"exponentialFactor": -1})
        self.assertEqual(str(context.exception), "Invalid exponentialFactor: Must be a positive number.")


class SequentialTestLoader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        test_names = super().getTestCaseNames(testCaseClass)
        testcase_methods = list(testCaseClass.__dict__.keys())
        test_names.sort(key=testcase_methods.index)
        return test_names


if __name__ == "__main__":
    unittest.main(testLoader=SequentialTestLoader())
