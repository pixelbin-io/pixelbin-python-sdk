import sys
import ujson
import unittest
from unittest import mock


sys.path.append(__file__.replace("/tests/pixelbin_test.py", ""))

CONFIG = {"domain": "https://api.testdomain.com", "apiSecret": "test-api-secret"}


def mocked_requests_get(*args, **kwargs):
    return {"status_code": 200, "content": '{"items":[]}'}


class TestPixelBin(unittest.TestCase):
    def setUp(self):
        self.config = CONFIG

        from pixelbin import PixelbinConfig, PixelbinClient

        self.pixelbinConfig = PixelbinConfig(config=self.config)
        self.pixelbinClient = PixelbinClient(config=self.pixelbinConfig)
        self.patcher = mock.patch(
            "pixelbin.common.aiohttp_helper.AiohttpHelper.request",
            side_effect=mocked_requests_get,
        )
        self.mock_response = None
        self.run_patcher()
        self.create_data()

    def create_data(self):
        self.folder_name = "testdir"
        self.folder_path = "/"
        self.urls_and_obj = [
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:600,w:800)",
                    "filePath": "W2.jpeg",
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "600"},
                                {"key": "w", "value": "800"}
                            ]
                        }
                    ]
                }
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/z-slug/t.resize(h:600,w:800)/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:600,w:800)",
                    "filePath": "W2.jpeg",
                    "zone": 'z-slug',
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "600"},
                                {"key": "w", "value": "800"}
                            ]
                        }
                    ]
                }
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)~t.rotate(a:-249)/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:600,w:800)~t.rotate(a:-249)",
                    "filePath": "W2.jpeg",
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "600"},
                                {"key": "w", "value": "800"}
                            ]
                        },
                        {
                            "plugin": "t",
                            "name": "rotate",
                            "values": [{"key": "a", "value": "-249"}]
                        }
                    ]
                }
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)~t.rotate(a:-249)~t.flip()~t.trim(t:217)/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:600,w:800)~t.rotate(a:-249)~t.flip()~t.trim(t:217)",
                    "filePath": "W2.jpeg",
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "600"},
                                {"key": "w", "value": "800"}
                            ],
                        },
                        {
                            "plugin": "t",
                            "name": "rotate",
                            "values": [{"key": "a", "value": "-249"}]
                        },
                        {"plugin": "t", "name": "flip"},
                        {
                            "plugin": "t",
                            "name": "trim",
                            "values": [{"key": "t", "value": "217"}]
                        }
                    ]
                }
            }
        ]

    def run_patcher(self):
        if (
            "testdomain" in self.pixelbinClient.config.domain
            or "test-api-secret" in self.pixelbinClient.config.apiSecret
        ):
            self.mock_response = self.patcher.start()

    def test_pixelbin_config_and_client(self):
        self.assertEqual(self.pixelbinConfig.domain, self.config["domain"])
        self.assertEqual(self.pixelbinConfig.apiSecret, self.config["apiSecret"])

        from pixelbin.platform.PixelbinClient import Assets, Organization

        self.assertEqual(self.pixelbinClient.config, self.pixelbinConfig)
        self.assertIsInstance(self.pixelbinClient.assets, Assets)
        self.assertIsInstance(self.pixelbinClient.organization, Organization)

    def test_createFolder(self):
        resp = self.pixelbinClient.assets.createFolder(
            name=self.folder_name, path=self.folder_path
        )

    def test_fileUpload_case1(self):
        file = open("1.jpeg", "rb")
        resp = self.pixelbinClient.assets.fileUpload(file=file)

    def test_fileUpload_case2(self):
        file = open("1.jpeg", "rb")
        resp = self.pixelbinClient.assets.fileUpload(
            file=file,
            path=self.folder_name,
            name="1",
            access="public-read",
            tags=["tag1", "tag2"],
            metadata={},
            overwrite=False,
            filenameOverride=True,
        )

    def test_listFiles_case1(self):
        resp = self.pixelbinClient.assets.listFiles()

    def test_listFiles_case2(self):
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

    def test_urlUpload(self):
        resp = self.pixelbinClient.assets.urlUpload(
            url="https://www.fetchfind.com/blog/wp-content/uploads/2017/08/cat-2734999_1920-5-common-cat-sounds.jpg",
            path=self.folder_name,
            name="2",
            access="public-read",
            tags=["cat", "animal"],
            metadata={},
            overwrite=False,
            filenameOverride=True,
        )

    def test_createSignedUrl_case1(self):
        resp = self.pixelbinClient.assets.createSignedUrl()

    def test_createSignedUrl_case2(self):
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

    def test_updateFile_case1(self):
        resp = self.pixelbinClient.assets.updateFile(fileId="1", name=f"1_")

    def test_updateFile_case2(self):
        resp = self.pixelbinClient.assets.updateFile(
            fileId=f"{self.folder_name}/1",
            name=f"{self.folder_name}_",
            path=self.folder_name,
            access="private",
            isActive=True,
            tags=["tag1", "tag2"],
            metadata={"key": "value"}
        )

    def test_getFileByFileId(self):
        resp = self.pixelbinClient.assets.getFileByFileId(
            fileId=f"{self.folder_name}/2"
        )

    def test_deleteFile(self):
        resp = self.pixelbinClient.assets.deleteFile(fileId="1_")

    def test_updateFolder(self):
        resp = self.pixelbinClient.assets.updateFolder(
            folderId=f"{self.folder_name}", isActive=True
        )

    def test_deleteFolder(self):
        resp = self.pixelbinClient.assets.listFiles()
        items = resp["items"]
        id = None
        for ele in items:
            if ele["type"] == "folder" and ele["name"] == self.folder_name:
                id = ele["_id"]
                break
        if id is not None:
            resp = self.pixelbinClient.assets.deleteFolder(_id=id)

    def test_getModules(self):
        resp = self.pixelbinClient.assets.getModules()

    def test_getModule(self):
        resp = self.pixelbinClient.assets.getModule(identifier="t")

    def test_url_to_obj(self):
        from pixelbin.utils.url import url_to_obj
        for case in self.urls_and_obj:
            url = case["url"]
            expected_obj = case["obj"]
            obj = url_to_obj(url)
            self.assertDictEqual(obj, expected_obj)

    def test_obj_to_url(self):
        from pixelbin.utils.url import obj_to_url
        for case in self.urls_and_obj:
            obj = case["obj"]
            expected_url = case["url"]
            url = obj_to_url(obj)
            self.assertEqual(url, expected_url)


class SequentialTestLoader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        test_names = super().getTestCaseNames(testCaseClass)
        testcase_methods = list(testCaseClass.__dict__.keys())
        test_names.sort(key=testcase_methods.index)
        return test_names


def set_domain_and_apisecerts_from_args():
    import argparse

    parser = argparse.ArgumentParser(description="Argument for testing")
    parser.add_argument(
        "--domain",
        type=str,
        help="pixelbin domain to hit",
        required=False,
        default=CONFIG["domain"],
    )
    parser.add_argument(
        "--apiSecret",
        type=str,
        help="api secret key for pixelbin",
        required=False,
        default=CONFIG["apiSecret"],
    )

    args = parser.parse_args()
    argv = sys.argv
    for k, v in args._get_kwargs():
        key = f"--{k}"
        if key in argv:
            argv.remove(key)
            argv.remove(v)
            CONFIG[k] = v
    argv.append("-v")


if __name__ == "__main__":
    set_domain_and_apisecerts_from_args()
    unittest.main(testLoader=SequentialTestLoader())
