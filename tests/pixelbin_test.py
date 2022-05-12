import sys
import ujson
import unittest
from unittest import mock

sys.path.append(__file__.replace("/tests/pixelbin_test.py", ""))

CONFIG = {"domain": "https://api.testdomain.com", "apiSecret": "test-api-secret"}


def mocked_requests_get(*args, **kwargs):
    return {"status_code": 200}


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

    def check_condition(self, resp):
        if resp["status_code"] != 200:
            print(resp)
        self.assertEqual(resp["status_code"], 200)

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
        self.check_condition(resp)

    def test_fileUpload_case1(self):
        file = open("1.jpeg", "rb")
        resp = self.pixelbinClient.assets.fileUpload(file=file)
        self.check_condition(resp)

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
        self.check_condition(resp)

    def test_listFiles_case1(self):
        resp = self.pixelbinClient.assets.listFiles()
        self.check_condition(resp)

    def test_listFiles_case2(self):
        resp = self.pixelbinClient.assets.listFiles(
            name="1",
            path=self.folder_name,
            format="jpeg",
            tags=["tag1", "tag2"],
            onlyFiles=False,
            onlyFolders=False,
            pageNo=1,
            pageSize=10,
            sort="name",
        )
        self.check_condition(resp)
        return resp

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
        self.check_condition(resp)

    def test_createSignedUrl_case1(self):
        resp = self.pixelbinClient.assets.createSignedUrl()
        self.check_condition(resp)

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
        self.check_condition(resp)

    def test_updateFile_case1(self):
        resp = self.pixelbinClient.assets.updateFile(fileId="1", name=f"1_")
        self.check_condition(resp)

    def test_updateFile_case2(self):
        resp = self.pixelbinClient.assets.updateFile(
            fileId=f"{self.folder_name}/1",
            name=f"{self.folder_name}_",
            path=self.folder_name,
            access="private",
            isActive=False,
            tags=["tag1", "tag2"],
            metadata={"key": "value"},
        )
        self.check_condition(resp)


    def test_getFileByFileId(self):
        resp = self.pixelbinClient.assets.getFileByFileId(fileId=f"{self.folder_name}/2")
        self.check_condition(resp)

    def test_deleteFile(self):
        resp = self.pixelbinClient.assets.deleteFile(fileId="1_")
        self.check_condition(resp)


    def test_updateFolder(self):
        resp = self.pixelbinClient.assets.updateFolder(
            folderId=self.folder_name, isActive=False
        )
        self.check_condition(resp)

    def test_deleteFolder(self):
        resp = self.pixelbinClient.assets.listFiles()
        self.check_condition(resp)
        data = ujson.loads(resp["text"])
        items = data["items"]
        id = None
        for ele in items:
            if ele["type"] == "folder" and ele["name"] == self.folder_name:
                id = ele["_id"]
                break
        if id is not None:
            resp = self.pixelbinClient.assets.deleteFolder(_id=id)
            self.check_condition(resp)

    def test_getModules(self):
        resp = self.pixelbinClient.assets.getModules()
        self.check_condition(resp)

    def test_getModule(self):
        resp = self.pixelbinClient.assets.getModule(identifier="t")
        self.check_condition(resp)


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
