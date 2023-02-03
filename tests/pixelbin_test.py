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
        self.urls_to_obj = [
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:600,w:800)",
                    "filePath": "W2.jpeg",
                    "options": {},
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
                    "options": {},
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
                    "options": {},
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
                    "options": {},
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
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)",
                    "filePath": "W2.jpeg",
                    "options": {},
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "200"},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                            "values": [
                                {"key": "a", "value": "100"},
                                {"key": "b", "value": "2.1"},
                                {"key": "c", "value": "test"},
                            ]
                        },
                    ]
                }
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:200,w:100)~p:preset1",
                    "filePath": "W2.jpeg",
                    "options": {},
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "200"},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                        },
                    ]
                }
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1()/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:200,w:100)~p:preset1()",
                    "filePath": "W2.jpeg",
                    "options": {},
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "200"},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                        },
                    ]
                }
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1(a:12/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
                    "filePath": "W2.jpeg",
                    "options": {},
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "200"},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                            "values": [{"key": "a", "value": "12"}]
                        },
                    ]
                }
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/feel/erase.bg(shadow:true)~t.merge(m:underlay,i:eU44YkFJOHlVMmZrWVRDOUNTRm1D,b:screen,r:true)/MZZKB3e1hT48o0NYJ2Kxh.jpeg?dpr=2.0&f_auto=True",
                "obj": {
                    "version": "v2",
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "filePath": "MZZKB3e1hT48o0NYJ2Kxh.jpeg",
                    "pattern": "erase.bg(shadow:true)~t.merge(m:underlay,i:eU44YkFJOHlVMmZrWVRDOUNTRm1D,b:screen,r:true)",
                    "cloudName": "feel",
                    "options": {
                        "dpr": 2.0,
                        "f_auto": True,
                    },
                    "zone": None,
                    "transformations": [
                        {
                            "values": [
                                {
                                    "key": "shadow",
                                    "value": "true",
                                },
                            ],
                            "plugin": "erase",
                            "name": "bg",
                        },
                        {
                            "values": [
                                {
                                    "key": "m",
                                    "value": "underlay",
                                },
                                {
                                    "key": "i",
                                    "value": "eU44YkFJOHlVMmZrWVRDOUNTRm1D",
                                },
                                {
                                    "key": "b",
                                    "value": "screen",
                                },
                                {
                                    "key": "r",
                                    "value": "true",
                                },
                            ],
                            "plugin": "t",
                            "name": "merge",
                        },
                    ]
                }
            }
        ]
        self.obj_to_urls = [
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:600,w:800)",
                    "filePath": "W2.jpeg",
                    "options": {},
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
                    "options": {},
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
                    "options": {},
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
                    "options": {},
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
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)",
                    "filePath": "W2.jpeg",
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "200"},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                            "values": [
                                {"key": "a", "value": "100"},
                                {"key": "b", "value": "2.1"},
                                {"key": "c", "value": "test"},
                            ]
                        },
                    ]
                }
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:200,w:100)~p:preset1",
                    "filePath": "W2.jpeg",
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "200"},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                        },
                    ]
                }
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1(a:12)/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
                    "filePath": "W2.jpeg",
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "200"},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                            "values": [{"key": "a", "value": "12"}]
                        },
                    ]
                }
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
                    "filePath": "W2.jpeg",
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": "200"},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                            "values": []
                        },
                    ]
                },
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:,w:100)~p:preset1/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:,w:100)~p:preset1(a:12",
                    "filePath": "W2.jpeg",
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"key": "h", "value": ""},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                            "values": []
                        },
                    ]
                },
                "error": "value not specified for 'h' in 'resize'"
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
                    "filePath": "W2.jpeg",
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {"value": ""},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                            "values": []
                        },
                    ]
                },
                "error": "key not specified in 'resize'"
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
                "obj": {
                    "version": "v2",
                    "cloudName": "broken-butterfly-3b12f1",
                    "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
                    "filePath": "W2.jpeg",
                    "zone": None,
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "transformations": [
                        {
                            "plugin": "t",
                            "name": "resize",
                            "values": [
                                {},
                                {"key": "w", "value": "100"}
                            ],
                        },
                        {
                            "plugin": "p",
                            "name": "preset1",
                            "values": []
                        },
                    ]
                },
                "error": "key not specified in 'resize'"
            },
            {
                "url": "https://cdn.pixelbinx0.de/v2/feel/erase.bg(shadow:true)~t.merge(m:underlay,i:eU44YkFJOHlVMmZrWVRDOUNTRm1D,b:screen,r:true)/MZZKB3e1hT48o0NYJ2Kxh.jpeg?dpr=2.0&f_auto=True",
                "obj": {
                    "version": "v2",
                    "baseUrl": "https://cdn.pixelbinx0.de",
                    "filePath": "MZZKB3e1hT48o0NYJ2Kxh.jpeg",
                    "pattern": "erase.bg(shadow:true)~t.merge(m:underlay,i:eU44YkFJOHlVMmZrWVRDOUNTRm1D,b:screen,r:true)",
                    "cloudName": "feel",
                    "options": {
                        "dpr": 2.0,
                        "f_auto": True,
                    },
                    "zone": None,
                    "transformations": [
                        {
                            "values": [
                                {
                                    "key": "shadow",
                                    "value": "true",
                                },
                            ],
                            "plugin": "erase",
                            "name": "bg",
                        },
                        {
                            "values": [
                                {
                                    "key": "m",
                                    "value": "underlay",
                                },
                                {
                                    "key": "i",
                                    "value": "eU44YkFJOHlVMmZrWVRDOUNTRm1D",
                                },
                                {
                                    "key": "b",
                                    "value": "screen",
                                },
                                {
                                    "key": "r",
                                    "value": "true",
                                },
                            ],
                            "plugin": "t",
                            "name": "merge",
                        },
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
        tags = ["tag1", "tag2"]
        file = open("1.jpeg", "rb")
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
        self.assertEqual(resp["tags"],tags)

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
        self.assertEqual(resp["tags"],tags)

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
        tags=["updated-tag1", "updated-tag2"]
        resp = self.pixelbinClient.assets.updateFile(
            fileId=f"{self.folder_name}/1",
            name=f"{self.folder_name}_",
            path=self.folder_name,
            access="private",
            isActive=True,
            tags=tags,
            metadata={"key": "value"}
        )
        self.assertEqual(resp["tags"],tags)

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

    def test_getFolderDetails(self):
        resp = self.pixelbinClient.assets.getFolderDetails(
            path="",
            name=self.folder_name
        )
    
    def test_getFolderDetails(self):
        resp = self.pixelbinClient.assets.getFolderDetails(
            path="",
            name=self.folder_name
        )

    def test_getFolderAncestors(self):
        resp = self.pixelbinClient.assets.createFolder(name="test", path="nested/folder")
        result = self.pixelbinClient.assets.getFolderAncestors(_id=resp["_id"])

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
    
    def test_addCredentials(self):
        resp = self.pixelbinClient.assets.addCredentials(
        credentials={"apiKey": "dummy_key_replace_with_real"},
        pluginId="remove")
    
    def test_updateCredentials(self):
        resp = self.pixelbinClient.assets.updateCredentials(
        credentials={"apiKey": "dummy_key_replace_with_real"},
        pluginId="remove")

    def test_deleteCredentials(self):
        resp = self.pixelbinClient.assets.deleteCredentials(
        pluginId="remove")

    def test_addPreset(self):
        resp = self.pixelbinClient.assets.addPreset(
        presetName="p1",
        transformation="t.flip()~t.flop()",
        params={"w":{"type":"integer","default":200},"h":{"type":"integer","default":400}})

    def test_getPresets(self):
        resp = self.pixelbinClient.assets.getPresets()
    
    def test_updatePresets(self):
        resp = self.pixelbinClient.assets.updatePreset(
        presetName="p1",
        archived=True)
    
    def test_getPreset(self):
        resp = self.pixelbinClient.assets.getPreset(
        presetName="p1")

    def test_deletePreset(self):
        resp = self.pixelbinClient.assets.deletePreset(
        presetName="p1")

    def test_getDefaultAssetForPlayground(self):
        resp = self.pixelbinClient.assets.getDefaultAssetForPlayground()

    def test_url_to_obj(self):
        from pixelbin.utils.url import url_to_obj
        for case in self.urls_to_obj:
            url = case["url"]
            expected_obj = case["obj"]
            obj = url_to_obj(url)
            self.assertDictEqual(obj, expected_obj)

    def test_obj_to_url(self):
        from pixelbin.utils.url import obj_to_url
        for case in self.obj_to_urls:
            obj = case["obj"]
            expected_url = case["url"]
            try :
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
            "options": { "dpr": 5.5, "f_auto": True },
            "transformations": [{}],
        };
        with self.assertRaises(PixelbinIllegalQueryParameterError):
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
            "options": { "dpr": 2.5, "f_auto": "abc" },
            "transformations": [{}],
        };
        with self.assertRaises(PixelbinIllegalQueryParameterError):
            obj_to_url(obj)

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
