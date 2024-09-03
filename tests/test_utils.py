MOCK_RESPONSE = {
    "multipartUploadChunkUploadFailed": {
        "response": {
            "url": "https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=60d2622fee6d344e0dd2e121d80718272d08cabb75f7b6e1f4013d05cec57ab7&pbe=1724155708104&pbt=e420dd6c-03eb-42a4-9264-e90db8422215&pbo=733&pbu=9662a4ab-af74-49a7-b804-41a501204a9d&partNumber=1",
            "method": "put",
            "params": {},
            "data": {},
            "external_call_request_time": "2024-08-20 16:48:28.154323+05:30",
            "status_code": 400,
            "text": '{"message":"Missing x-pixb-meta-assetdata field","status":400,"code":"CG-0400","exception":"MissingMultipartMetaError"}',
            "headers": {
                "Date": "Tue, 20 Aug 2024 11:18:28 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "119",
                "Connection": "keep-alive",
                "x-powered-by": "Express",
                "Vary": "Origin",
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Expose-Headers": "Accept-Ranges,Content-Encoding,Content-Length,Content-Range,Range",
                "Etag": 'W/"77-ylONBnthDVzh7F2LhBn/UxRAD0M"',
                "Via": "1.1 google",
                "CF-Cache-Status": "DYNAMIC",
                "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
                "X-Content-Type-Options": "nosniff",
                "Cache-Control": "no-store",
                "Server": "cloudflare",
                "CF-RAY": "8b61fb9a3d36f367-BOM",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"message":"Missing x-pixb-meta-assetdata field","status":400,"code":"CG-0400","exception":"MissingMultipartMetaError"}',
        },
    },
    "multipartUploadChunkUploadFailed2": {
        "response": {
            "url": "https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=60d2622fee6d344e0dd2e121d80718272d08cabb75f7b6e1f4013d05cec57ab7&pbe=1724155708104&pbt=e420dd6c-03eb-42a4-9264-e90db8422215&pbo=733&pbu=9662a4ab-af74-49a7-b804-41a501204a9d&partNumber=1",
            "method": "put",
            "params": {},
            "data": {},
            "external_call_request_time": "2024-08-20 16:48:28.154323+05:30",
            "status_code": 503,
            "text": '{"message":"Internal Server Error","status":503}',
            "headers": {
                "Date": "Tue, 20 Aug 2024 11:18:28 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "119",
                "Connection": "keep-alive",
                "x-powered-by": "Express",
                "Vary": "Origin",
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Expose-Headers": "Accept-Ranges,Content-Encoding,Content-Length,Content-Range,Range",
                "Etag": 'W/"77-ylONBnthDVzh7F2LhBn/UxRAD0M"',
                "Via": "1.1 google",
                "CF-Cache-Status": "DYNAMIC",
                "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
                "X-Content-Type-Options": "nosniff",
                "Cache-Control": "no-store",
                "Server": "cloudflare",
                "CF-RAY": "8b61fb9a3d36f367-BOM",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"message":"Internal Server Error","status":503}',
        },
    },
    "multipartUploadChunkUpload": {
        "response": {
            "url": "https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6&partNumber=1",
            "method": "put",
            "params": {},
            "data": {},
            "external_call_request_time": "2024-08-20 12:52:54.259051+05:30",
            "status_code": 204,
            "text": "",
            "headers": {
                "Date": "Tue, 20 Aug 2024 07:22:54 GMT",
                "Connection": "keep-alive",
                "x-powered-by": "Express",
                "Vary": "Origin",
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Expose-Headers": "Accept-Ranges,Content-Encoding,Content-Length,Content-Range,Range",
                "x-fynd-trace-id": "7fc1df8d32a23a451cc7ebaa1004c35b",
                "Via": "1.1 google",
                "CF-Cache-Status": "DYNAMIC",
                "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
                "X-Content-Type-Options": "nosniff",
                "Cache-Control": "no-store",
                "Server": "cloudflare",
                "CF-RAY": "8b60a289cce53e46-BOM",
            },
            "cookies": {},
            "error_message": "",
            "content": b"",
        },
    },
    "multipartUploadCompleteUpload": {
        "response": {
            "url": "https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6",
            "method": "post",
            "params": {},
            "data": '{"parts":[1,2],"x-pixb-meta-assetdata":"{\\"orgId\\":733,\\"type\\":\\"file\\",\\"name\\":\\"asset-8HqCHyhLQ.jpeg\\",\\"path\\":\\"\\",\\"fileId\\":\\"asset-8HqCHyhLQ.jpeg\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erasebg-assets-ap-south-1\\",\\"s3Key\\":\\"uploads/black-surf-ac93df/original/s3/beb0f286-1dc1-4e6b-a1bd-dd8ef0bc87ca.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[],\\"metadata\\":{\\"source\\":\\"signedUrl\\",\\"publicUploadId\\":\\"a1bba000-718f-4224-a6db-b59c98d7cd81\\"},\\"overwrite\\":false,\\"filenameOverride\\":false}"}',
            "external_call_request_time": "2024-08-20 12:52:54.474284+05:30",
            "status_code": 200,
            "text": '{"orgId":733,"type":"file","name":"asset-8HqCHyhLQ.jpeg","path":"","fileId":"asset-8HqCHyhLQ.jpeg","access":"public-read","tags":[],"metadata":{"source":"direct","publicUploadId":"a1bba000-718f-4224-a6db-b59c98d7cd81"},"format":"webp","assetType":"image","size":11732,"width":400,"height":301,"context":{"steps":[],"req":{"headers":{},"query":{}},"meta":{"format":"webp","size":11732,"width":400,"height":301,"space":"srgb","channels":4,"depth":"uchar","isProgressive":false,"resolutionUnit":"inch","hasProfile":false,"hasAlpha":true,"orientation":1,"extension":"jpeg","contentType":"image/webp","assetType":"image","isImageAsset":true,"isAudioAsset":false,"isVideoAsset":false,"isRawAsset":false,"isTransformationSupported":true}},"isOriginal":true,"_id":"bb20a7cb-fdff-4956-a050-7fff9d8f041c","url":"https://cdn.pixelbin.io/v2/black-surf-ac93df/original/asset-8HqCHyhLQ.jpeg"}',
            "headers": {
                "Date": "Tue, 20 Aug 2024 07:22:55 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Transfer-Encoding": "chunked",
                "Connection": "keep-alive",
                "x-powered-by": "Express",
                "Vary": "Origin",
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Expose-Headers": "Accept-Ranges,Content-Encoding,Content-Length,Content-Range,Range",
                "Etag": 'W/"370-IMpsRoT/H9Xo3mZtH/QOqU8Dl6I"',
                "x-fynd-trace-id": "6c01576a944ddec431510f06c6aa75cf",
                "Via": "1.1 google",
                "CF-Cache-Status": "DYNAMIC",
                "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
                "X-Content-Type-Options": "nosniff",
                "Cache-Control": "no-store",
                "Server": "cloudflare",
                "CF-RAY": "8b60a28b98ed3a3a-BOM",
                "Content-Encoding": "gzip",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"orgId":733,"type":"file","name":"asset-8HqCHyhLQ.jpeg","path":"","fileId":"asset-8HqCHyhLQ.jpeg","access":"public-read","tags":[],"metadata":{"source":"direct","publicUploadId":"a1bba000-718f-4224-a6db-b59c98d7cd81"},"format":"webp","assetType":"image","size":11732,"width":400,"height":301,"context":{"steps":[],"req":{"headers":{},"query":{}},"meta":{"format":"webp","size":11732,"width":400,"height":301,"space":"srgb","channels":4,"depth":"uchar","isProgressive":false,"resolutionUnit":"inch","hasProfile":false,"hasAlpha":true,"orientation":1,"extension":"jpeg","contentType":"image/webp","assetType":"image","isImageAsset":true,"isAudioAsset":false,"isVideoAsset":false,"isRawAsset":false,"isTransformationSupported":true}},"isOriginal":true,"_id":"bb20a7cb-fdff-4956-a050-7fff9d8f041c","url":"https://cdn.pixelbin.io/v2/black-surf-ac93df/original/asset-8HqCHyhLQ.jpeg"}',
        }
    },
    "createFolder": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/folders",
            "method": "post",
            "params": {},
            "data": {"name": "testdir", "path": "/"},
            "external_call_request_time": "2023-03-06 13:23:35.184016+05:30",
            "status_code": 200,
            "text": '{"_id":"1c4ced4e-a408-42c6-82af-a55f2c652ac9","name":"testdir","path":"","isActive":true}',
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "89",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"59-jFA0IErh5el50R5juNsABrhV4cc"',
                "X-Fynd-Trace-Id": "b5ad9068c76cd02332c6d2905bbf1c41",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"1c4ced4e-a408-42c6-82af-a55f2c652ac9","name":"testdir","path":"","isActive":true}',
        }
    },
    "fileUpload1": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/upload/direct",
            "method": "post",
            "params": {},
            "data": {"file": "1.jpeg"},
            "external_call_request_time": "2023-03-06 14:53:46.285504+05:30",
            "status_code": 200,
            "text": '{"orgId":782,"type":"file","name":"1","path":"","fileId":"1","access":"public-read","tags":[],"metadata":{"source":"direct"},"format":"webp","assetType":"image","size":11732,"width":400,"height":301,"context":{"steps":[],"req":{"headers":{},"query":{}},"meta":{"size":11732,"height":301,"width":400,"format":"webp","assetType":"image"}},"_id":"dc3b97a3-cb18-40f7-8d49-3ece7429970a","url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/1.webp"}',
            "headers": {
                "Date": "Mon, 06 Mar 2023 09:23:46 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "455",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"1c7-wo3v551kIdhB8ydZfwzyG8DhG8M"',
                "X-Fynd-Trace-Id": "0254d5256df2298625836107b6dd716a",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"orgId":782,"type":"file","name":"1","path":"","fileId":"1","access":"public-read","tags":[],"metadata":{"source":"direct"},"format":"webp","assetType":"image","size":11732,"width":400,"height":301,"context":{"steps":[],"req":{"headers":{},"query":{}},"meta":{"size":11732,"height":301,"width":400,"format":"webp","assetType":"image"}},"_id":"dc3b97a3-cb18-40f7-8d49-3ece7429970a","url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/1.webp"}',
        }
    },
    "fileUpload2": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/upload/direct",
            "method": "post",
            "params": {},
            "data": {
                "file": "1.jpeg",
                "path": "testdir",
                "name": "1",
                "access": "public-read",
                "tags": ["tag1", "tag2"],
                "metadata": {},
                "overwrite": False,
                "filenameOverride": True,
            },
            "external_call_request_time": "2023-03-06 15:20:16.997462+05:30",
            "status_code": 200,
            "text": '{"orgId":782,"type":"file","name":"1","path":"testdir","fileId":"testdir/1","access":"public-read","tags":["tag1","tag2"],"metadata":{"source":"direct"},"format":"webp","assetType":"image","size":11732,"width":400,"height":301,"context":{"steps":[],"req":{"headers":{},"query":{}},"meta":{"size":11732,"height":301,"width":400,"format":"webp","assetType":"image"}},"_id":"74d4f5ac-e6af-4bfe-af3e-234e833dc74e","url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/testdir/1.webp"}',
            "headers": {
                "Date": "Mon, 06 Mar 2023 09:50:17 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "491",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"1eb-ku52aL6NUijHKHs50qAwtiCvnvU"',
                "X-Fynd-Trace-Id": "29975ebe9bd77d4bfc4c81bfdcf6656d",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"orgId":782,"type":"file","name":"1","path":"testdir","fileId":"testdir/1","access":"public-read","tags":["tag1","tag2"],"metadata":{"source":"direct"},"format":"webp","assetType":"image","size":11732,"width":400,"height":301,"context":{"steps":[],"req":{"headers":{},"query":{}},"meta":{"size":11732,"height":301,"width":400,"format":"webp","assetType":"image"}},"_id":"74d4f5ac-e6af-4bfe-af3e-234e833dc74e","url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/testdir/1.webp"}',
        }
    },
    "getFileById": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/files/id/9d331030-b695-475e-9d4a-a660696d5fa5",
            "method": "get",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-16 16:05:12.661962+05:30",
            "status_code": 200,
            "text": '{"_id":"9d331030-b695-475e-9d4a-a660696d5fa5","name":"2","path":"","fileId":"2","format":"jpeg","assetType":"image","access":"public-read","size":62511,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/dawn-rain-2883/original/2.jpeg","meta":{},"kvStore":[],"height":760,"width":1140,"createdAt":"2023-03-09T13:05:49.420Z","updatedAt":"2023-03-09T13:05:49.420Z"}',
            "headers": {
                "Date": "Thu, 16 Mar 2023 10:35:12 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "404",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"194-Y1TD/EIil5R0khVcEQHB9YY9bPg"',
                "X-Fynd-Trace-Id": "dcbb5be4cef49afe48d72601511d126a",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"9d331030-b695-475e-9d4a-a660696d5fa5","name":"2","path":"","fileId":"2","format":"jpeg","assetType":"image","access":"public-read","size":62511,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/dawn-rain-2883/original/2.jpeg","meta":{},"kvStore":[],"height":760,"width":1140,"createdAt":"2023-03-09T13:05:49.420Z","updatedAt":"2023-03-09T13:05:49.420Z"}',
        }
    },
    "listFiles1": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/listFiles",
            "method": "get",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-06 15:46:07.650606+05:30",
            "status_code": 200,
            "text": '{"items":[{"_id":"24e57515-3b15-48a3-865f-c227488498cf","createdAt":"2023-03-06T10:13:07.315Z","updatedAt":"2023-03-06T10:13:07.315Z","fileId":"1","path":"","name":"1","format":"png","assetType":"image","type":"file","size":155108,"tags":[],"metadata":{"source":"direct"},"access":"public-read","width":500,"height":500,"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/1.png"}],"page":{"type":"number","size":1,"current":1,"hasNext":false,"itemTotal":1}}',
            "headers": {
                "Date": "Mon, 06 Mar 2023 10:16:07 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "470",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"1d6-SLMJpWiySmKWf59RWqqfUvjSO+U"',
                "X-Fynd-Trace-Id": "1a8d4fb219472ab215d794d18aebbb24",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"items":[{"_id":"24e57515-3b15-48a3-865f-c227488498cf","createdAt":"2023-03-06T10:13:07.315Z","updatedAt":"2023-03-06T10:13:07.315Z","fileId":"1","path":"","name":"1","format":"png","assetType":"image","type":"file","size":155108,"tags":[],"metadata":{"source":"direct"},"access":"public-read","width":500,"height":500,"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/1.png"}],"page":{"type":"number","size":1,"current":1,"hasNext":false,"itemTotal":1}}',
        }
    },
    "listFiles2": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/listFiles",
            "method": "get",
            "params": {
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
            "data": None,
            "external_call_request_time": "2023-03-06 16:20:18.141219+05:30",
            "status_code": 200,
            "text": '{"items":[],"page":{}}',
            "headers": {
                "Date": "Mon, 06 Mar 2023 10:50:18 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "22",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"16-JEzDZg3utPw7YhYBijDxOpHORvc"',
                "X-Fynd-Trace-Id": "a41a9b598c87089a55c8bcc194653a6a",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"items":[],"page":{}}',
        }
    },
    "urlUpload": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/upload/url",
            "method": "post",
            "params": {},
            "data": {
                "url": "https://www.fetchfind.com/blog/wp-content/uploads/2017/08/cat-2734999_1920-5-common-cat-sounds.jpg",
                "path": "testdir",
                "name": "2",
                "access": "public-read",
                "tags": ["cat", "animal"],
                "metadata": {},
                "overwrite": False,
                "filenameOverride": True,
            },
            "external_call_request_time": "2023-03-07 10:56:42.007639+05:30",
            "status_code": 200,
            "text": '{"orgId":782,"type":"file","name":"2","path":"testdir","fileId":"testdir/2","access":"public-read","tags":["cat","animal"],"metadata":{"source":"direct"},"format":"jpeg","assetType":"image","size":388253,"width":1920,"height":1440,"context":{"steps":[],"req":{"headers":{},"query":{}},"meta":{"size":388253,"height":1440,"width":1920,"format":"jpeg","assetType":"image"}},"_id":"682770a5-c80f-4413-942c-dbc0c4585559","url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/testdir/2.jpeg"}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 05:26:44 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "498",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"1f2-gGC4rsW9QhNgC2//aqTkrmRlC0A"',
                "X-Fynd-Trace-Id": "558805335695851399cc3e74b867f10e",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"orgId":782,"type":"file","name":"2","path":"testdir","fileId":"testdir/2","access":"public-read","tags":["cat","animal"],"metadata":{"source":"direct"},"format":"jpeg","assetType":"image","size":388253,"width":1920,"height":1440,"context":{"steps":[],"req":{"headers":{},"query":{}},"meta":{"size":388253,"height":1440,"width":1920,"format":"jpeg","assetType":"image"}},"_id":"682770a5-c80f-4413-942c-dbc0c4585559","url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/testdir/2.jpeg"}',
        }
    },
    "createSignedURL1": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/upload/signed-url",
            "method": "post",
            "params": {},
            "data": {},
            "external_call_request_time": "2023-03-07 11:09:42.969110+05:30",
            "status_code": 200,
            "text": '{"s3PresignedUrl":{"url":"https://s3.ap-south-1.amazonaws.com/erase-erasebg-assets-ap-south-1","fields":{"key":"uploads/shrill-bread-710314/original/s10/62be9fe0-9a95-4043-8ca8-5bb6c24fc586.jpeg","x-amz-meta-assetData":"{\\"orgId\\":782,\\"type\\":\\"file\\",\\"name\\":\\"asset-m1vh8lg2W\\",\\"path\\":\\"\\",\\"fileId\\":\\"asset-m1vh8lg2W\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erasebg-assets-ap-south-1\\",\\"s3Key\\":\\"uploads/shrill-bread-710314/original/s10/62be9fe0-9a95-4043-8ca8-5bb6c24fc586.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[],\\"metadata\\":{\\"source\\":\\"signedUrl\\"},\\"overwrite\\":false,\\"filenameOverride\\":false}","x-amz-meta-token":"cd80c99c-0631-4e55-8306-39668c3db67a","bucket":"erase-erasebg-assets-ap-south-1","X-Amz-Algorithm":"AWS4-HMAC-SHA256","X-Amz-Credential":"AKIATGSK32LKLSRL3Q47/20230307/ap-south-1/s3/aws4_request","X-Amz-Date":"20230307T053943Z","Policy":"eyJleHBpcmF0aW9uIjoiMjAyMy0wMy0wN1QwNTo0NDo0M1oiLCJjb25kaXRpb25zIjpbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMCwxNTcyODY0MDBdLHsia2V5IjoidXBsb2Fkcy9zaHJpbGwtYnJlYWQtNzEwMzE0L29yaWdpbmFsL3MxMC82MmJlOWZlMC05YTk1LTQwNDMtOGNhOC01YmI2YzI0ZmM1ODYuanBlZyJ9LHsieC1hbXotbWV0YS1hc3NldERhdGEiOiJ7XCJvcmdJZFwiOjc4MixcInR5cGVcIjpcImZpbGVcIixcIm5hbWVcIjpcImFzc2V0LW0xdmg4bGcyV1wiLFwicGF0aFwiOlwiXCIsXCJmaWxlSWRcIjpcImFzc2V0LW0xdmg4bGcyV1wiLFwiZm9ybWF0XCI6XCJqcGVnXCIsXCJzM0J1Y2tldFwiOlwiZXJhc2UtZXJhc2V4MC1lcmFzZWJnLWFzc2V0cy1hcC1zb3V0aC0xXCIsXCJzM0tleVwiOlwidXBsb2Fkcy9zaHJpbGwtYnJlYWQtNzEwMzE0L29yaWdpbmFsL3MxMC82MmJlOWZlMC05YTk1LTQwNDMtOGNhOC01YmI2YzI0ZmM1ODYuanBlZ1wiLFwiYWNjZXNzXCI6XCJwdWJsaWMtcmVhZFwiLFwidGFnc1wiOltdLFwibWV0YWRhdGFcIjp7XCJzb3VyY2VcIjpcInNpZ25lZFVybFwifSxcIm92ZXJ3cml0ZVwiOmZhbHNlLFwiZmlsZW5hbWVPdmVycmlkZVwiOmZhbHNlfSJ9LHt9LHsieC1hbXotbWV0YS10b2tlbiI6ImNkODBjOTljLTA2MzEtNGU1NS04MzA2LTM5NjY4YzNkYjY3YSJ9LHsiYnVja2V0IjoiZXJhc2UtZXJhc2V4MC1lcmFzZWJnLWFzc2V0cy1hcC1zb3V0aC0xIn0seyJYLUFtei1BbGdvcml0aG0iOiJBV1M0LUhNQUMtU0hBMjU2In0seyJYLUFtei1DcmVkZW50aWFsIjoiQUtJQVRHU0szMkxLTFNSTDNRNDcvMjAyMzAzMDcvYXAtc291dGgtMS9zMy9hd3M0X3JlcXVlc3QifSx7IlgtQW16LURhdGUiOiIyMDIzMDMwN1QwNTM5NDNaIn1dfQ==","X-Amz-Signature":"48f0546a6453d2238d4f2c94d076a5531e67883bf794dfd7fa269a300a0e00da"}}}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 05:39:43 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "2176",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"880-tdTbnE/o5Bv4UqwAgnGdANPvitE"',
                "X-Fynd-Trace-Id": "bf222d03c6d1da16817d4ce132a9bdf2",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"s3PresignedUrl":{"url":"https://s3.ap-south-1.amazonaws.com/erase-erasebg-assets-ap-south-1","fields":{"key":"uploads/shrill-bread-710314/original/s10/62be9fe0-9a95-4043-8ca8-5bb6c24fc586.jpeg","x-amz-meta-assetData":"{\\"orgId\\":782,\\"type\\":\\"file\\",\\"name\\":\\"asset-m1vh8lg2W\\",\\"path\\":\\"\\",\\"fileId\\":\\"asset-m1vh8lg2W\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erasebg-assets-ap-south-1\\",\\"s3Key\\":\\"uploads/shrill-bread-710314/original/s10/62be9fe0-9a95-4043-8ca8-5bb6c24fc586.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[],\\"metadata\\":{\\"source\\":\\"signedUrl\\"},\\"overwrite\\":false,\\"filenameOverride\\":false}","x-amz-meta-token":"cd80c99c-0631-4e55-8306-39668c3db67a","bucket":"erase-erasebg-assets-ap-south-1","X-Amz-Algorithm":"AWS4-HMAC-SHA256","X-Amz-Credential":"AKIATGSK32LKLSRL3Q47/20230307/ap-south-1/s3/aws4_request","X-Amz-Date":"20230307T053943Z","Policy":"eyJleHBpcmF0aW9uIjoiMjAyMy0wMy0wN1QwNTo0NDo0M1oiLCJjb25kaXRpb25zIjpbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMCwxNTcyODY0MDBdLHsia2V5IjoidXBsb2Fkcy9zaHJpbGwtYnJlYWQtNzEwMzE0L29yaWdpbmFsL3MxMC82MmJlOWZlMC05YTk1LTQwNDMtOGNhOC01YmI2YzI0ZmM1ODYuanBlZyJ9LHsieC1hbXotbWV0YS1hc3NldERhdGEiOiJ7XCJvcmdJZFwiOjc4MixcInR5cGVcIjpcImZpbGVcIixcIm5hbWVcIjpcImFzc2V0LW0xdmg4bGcyV1wiLFwicGF0aFwiOlwiXCIsXCJmaWxlSWRcIjpcImFzc2V0LW0xdmg4bGcyV1wiLFwiZm9ybWF0XCI6XCJqcGVnXCIsXCJzM0J1Y2tldFwiOlwiZXJhc2UtZXJhc2V4MC1lcmFzZWJnLWFzc2V0cy1hcC1zb3V0aC0xXCIsXCJzM0tleVwiOlwidXBsb2Fkcy9zaHJpbGwtYnJlYWQtNzEwMzE0L29yaWdpbmFsL3MxMC82MmJlOWZlMC05YTk1LTQwNDMtOGNhOC01YmI2YzI0ZmM1ODYuanBlZ1wiLFwiYWNjZXNzXCI6XCJwdWJsaWMtcmVhZFwiLFwidGFnc1wiOltdLFwibWV0YWRhdGFcIjp7XCJzb3VyY2VcIjpcInNpZ25lZFVybFwifSxcIm92ZXJ3cml0ZVwiOmZhbHNlLFwiZmlsZW5hbWVPdmVycmlkZVwiOmZhbHNlfSJ9LHt9LHsieC1hbXotbWV0YS10b2tlbiI6ImNkODBjOTljLTA2MzEtNGU1NS04MzA2LTM5NjY4YzNkYjY3YSJ9LHsiYnVja2V0IjoiZXJhc2UtZXJhc2V4MC1lcmFzZWJnLWFzc2V0cy1hcC1zb3V0aC0xIn0seyJYLUFtei1BbGdvcml0aG0iOiJBV1M0LUhNQUMtU0hBMjU2In0seyJYLUFtei1DcmVkZW50aWFsIjoiQUtJQVRHU0szMkxLTFNSTDNRNDcvMjAyMzAzMDcvYXAtc291dGgtMS9zMy9hd3M0X3JlcXVlc3QifSx7IlgtQW16LURhdGUiOiIyMDIzMDMwN1QwNTM5NDNaIn1dfQ==","X-Amz-Signature":"48f0546a6453d2238d4f2c94d076a5531e67883bf794dfd7fa269a300a0e00da"}}}',
        }
    },
    "createSignedURL2": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/upload/signed-url",
            "method": "post",
            "params": {},
            "data": {
                "name": "1",
                "path": "testdir",
                "format": "jpeg",
                "access": "public-read",
                "tags": ["tag1", "tag2"],
                "metadata": {},
                "overwrite": False,
                "filenameOverride": True,
            },
            "external_call_request_time": "2023-03-07 11:09:42.969110+05:30",
            "status_code": 200,
            "text": '{"s3PresignedUrl":{"url":"https://s3.ap-south-1.amazonaws.com/erase-erasebg-assets-ap-south-1","fields":{"key":"uploads/shrill-bread-710314/original/s10/62be9fe0-9a95-4043-8ca8-5bb6c24fc586.jpeg","x-amz-meta-assetData":"{\\"orgId\\":782,\\"type\\":\\"file\\",\\"name\\":\\"asset-m1vh8lg2W\\",\\"path\\":\\"\\",\\"fileId\\":\\"asset-m1vh8lg2W\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erasebg-assets-ap-south-1\\",\\"s3Key\\":\\"uploads/shrill-bread-710314/original/s10/62be9fe0-9a95-4043-8ca8-5bb6c24fc586.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[],\\"metadata\\":{\\"source\\":\\"signedUrl\\"},\\"overwrite\\":false,\\"filenameOverride\\":false}","x-amz-meta-token":"cd80c99c-0631-4e55-8306-39668c3db67a","bucket":"erase-erasebg-assets-ap-south-1","X-Amz-Algorithm":"AWS4-HMAC-SHA256","X-Amz-Credential":"AKIATGSK32LKLSRL3Q47/20230307/ap-south-1/s3/aws4_request","X-Amz-Date":"20230307T053943Z","Policy":"eyJleHBpcmF0aW9uIjoiMjAyMy0wMy0wN1QwNTo0NDo0M1oiLCJjb25kaXRpb25zIjpbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMCwxNTcyODY0MDBdLHsia2V5IjoidXBsb2Fkcy9zaHJpbGwtYnJlYWQtNzEwMzE0L29yaWdpbmFsL3MxMC82MmJlOWZlMC05YTk1LTQwNDMtOGNhOC01YmI2YzI0ZmM1ODYuanBlZyJ9LHsieC1hbXotbWV0YS1hc3NldERhdGEiOiJ7XCJvcmdJZFwiOjc4MixcInR5cGVcIjpcImZpbGVcIixcIm5hbWVcIjpcImFzc2V0LW0xdmg4bGcyV1wiLFwicGF0aFwiOlwiXCIsXCJmaWxlSWRcIjpcImFzc2V0LW0xdmg4bGcyV1wiLFwiZm9ybWF0XCI6XCJqcGVnXCIsXCJzM0J1Y2tldFwiOlwiZXJhc2UtZXJhc2V4MC1lcmFzZWJnLWFzc2V0cy1hcC1zb3V0aC0xXCIsXCJzM0tleVwiOlwidXBsb2Fkcy9zaHJpbGwtYnJlYWQtNzEwMzE0L29yaWdpbmFsL3MxMC82MmJlOWZlMC05YTk1LTQwNDMtOGNhOC01YmI2YzI0ZmM1ODYuanBlZ1wiLFwiYWNjZXNzXCI6XCJwdWJsaWMtcmVhZFwiLFwidGFnc1wiOltdLFwibWV0YWRhdGFcIjp7XCJzb3VyY2VcIjpcInNpZ25lZFVybFwifSxcIm92ZXJ3cml0ZVwiOmZhbHNlLFwiZmlsZW5hbWVPdmVycmlkZVwiOmZhbHNlfSJ9LHt9LHsieC1hbXotbWV0YS10b2tlbiI6ImNkODBjOTljLTA2MzEtNGU1NS04MzA2LTM5NjY4YzNkYjY3YSJ9LHsiYnVja2V0IjoiZXJhc2UtZXJhc2V4MC1lcmFzZWJnLWFzc2V0cy1hcC1zb3V0aC0xIn0seyJYLUFtei1BbGdvcml0aG0iOiJBV1M0LUhNQUMtU0hBMjU2In0seyJYLUFtei1DcmVkZW50aWFsIjoiQUtJQVRHU0szMkxLTFNSTDNRNDcvMjAyMzAzMDcvYXAtc291dGgtMS9zMy9hd3M0X3JlcXVlc3QifSx7IlgtQW16LURhdGUiOiIyMDIzMDMwN1QwNTM5NDNaIn1dfQ==","X-Amz-Signature":"48f0546a6453d2238d4f2c94d076a5531e67883bf794dfd7fa269a300a0e00da"}}}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 05:39:43 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "2176",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"880-tdTbnE/o5Bv4UqwAgnGdANPvitE"',
                "X-Fynd-Trace-Id": "bf222d03c6d1da16817d4ce132a9bdf2",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"s3PresignedUrl":{"url":"https://s3.ap-south-1.amazonaws.com/erase-erasebg-assets-ap-south-1","fields":{"key":"uploads/shrill-bread-710314/original/s9/09532e21-d446-479e-8ab0-1364e4ee1320.jpeg","x-amz-meta-assetData":"{\\"orgId\\":782,\\"type\\":\\"file\\",\\"name\\":\\"1\\",\\"path\\":\\"testdir\\",\\"fileId\\":\\"testdir/1\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erasebg-assets-ap-south-1\\",\\"s3Key\\":\\"uploads/shrill-bread-710314/original/s9/09532e21-d446-479e-8ab0-1364e4ee1320.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[\\"tag1\\",\\"tag2\\"],\\"metadata\\":{\\"source\\":\\"signedUrl\\"},\\"overwrite\\":false,\\"filenameOverride\\":true}","x-amz-meta-token":"cd80c99c-0631-4e55-8306-39668c3db67a","bucket":"erase-erasebg-assets-ap-south-1","X-Amz-Algorithm":"AWS4-HMAC-SHA256","X-Amz-Credential":"AKIATGSK32LKLSRL3Q47/20230307/ap-south-1/s3/aws4_request","X-Amz-Date":"20230307T055556Z","Policy":"eyJleHBpcmF0aW9uIjoiMjAyMy0wMy0wN1QwNjowMDo1NloiLCJjb25kaXRpb25zIjpbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMCwxNTcyODY0MDBdLHsia2V5IjoidXBsb2Fkcy9zaHJpbGwtYnJlYWQtNzEwMzE0L29yaWdpbmFsL3M5LzA5NTMyZTIxLWQ0NDYtNDc5ZS04YWIwLTEzNjRlNGVlMTMyMC5qcGVnIn0seyJ4LWFtei1tZXRhLWFzc2V0RGF0YSI6IntcIm9yZ0lkXCI6NzgyLFwidHlwZVwiOlwiZmlsZVwiLFwibmFtZVwiOlwiMVwiLFwicGF0aFwiOlwidGVzdGRpclwiLFwiZmlsZUlkXCI6XCJ0ZXN0ZGlyLzFcIixcImZvcm1hdFwiOlwianBlZ1wiLFwiczNCdWNrZXRcIjpcImVyYXNlLWVyYXNleDAtZXJhc2ViZy1hc3NldHMtYXAtc291dGgtMVwiLFwiczNLZXlcIjpcInVwbG9hZHMvc2hyaWxsLWJyZWFkLTcxMDMxNC9vcmlnaW5hbC9zOS8wOTUzMmUyMS1kNDQ2LTQ3OWUtOGFiMC0xMzY0ZTRlZTEzMjAuanBlZ1wiLFwiYWNjZXNzXCI6XCJwdWJsaWMtcmVhZFwiLFwidGFnc1wiOltcInRhZzFcIixcInRhZzJcIl0sXCJtZXRhZGF0YVwiOntcInNvdXJjZVwiOlwic2lnbmVkVXJsXCJ9LFwib3ZlcndyaXRlXCI6ZmFsc2UsXCJmaWxlbmFtZU92ZXJyaWRlXCI6dHJ1ZX0ifSx7fSx7IngtYW16LW1ldGEtdG9rZW4iOiJjZDgwYzk5Yy0wNjMxLTRlNTUtODMwNi0zOTY2OGMzZGI2N2EifSx7ImJ1Y2tldCI6ImVyYXNlLWVyYXNleDAtZXJhc2ViZy1hc3NldHMtYXAtc291dGgtMSJ9LHsiWC1BbXotQWxnb3JpdGhtIjoiQVdTNC1ITUFDLVNIQTI1NiJ9LHsiWC1BbXotQ3JlZGVudGlhbCI6IkFLSUFUR1NLMzJMS0xTUkwzUTQ3LzIwMjMwMzA3L2FwLXNvdXRoLTEvczMvYXdzNF9yZXF1ZXN0In0seyJYLUFtei1EYXRlIjoiMjAyMzAzMDdUMDU1NTU2WiJ9XX0=","X-Amz-Signature":"21e00f703bb4837039825c7e494d8683d7510f60100dc8d6eb06927f950e922b"}}}',
        }
    },
    "createSignedURLV2_1": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v2.0/upload/signed-url",
            "method": "post",
            "params": {},
            "data": {},
            "external_call_request_time": "2024-03-12 16:13:48.862784+05:30",
            "status_code": 200,
            "text": '{"presignedUrl":{"url":"https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6","fields":{"x-pixb-meta-assetdata":"{\\"orgId\\":3308,\\"type\\":\\"file\\",\\"name\\":\\"asset-8WhaVptV2.jpeg\\",\\"path\\":\\"\\",\\"fileId\\":\\"asset-8WhaVptV2.jpeg\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erase-erasebg-assets\\",\\"s3Key\\":\\"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[],\\"metadata\\":{\\"source\\":\\"signedUrl\\",\\"publicUploadId\\":\\"376a20ef-cf61-469d-a90f-c35177cc1dd6\\"},\\"overwrite\\":false,\\"filenameOverride\\":false}"}}}',
            "headers": {
                "Date": "Tue, 12 Mar 2024 10:43:48 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Transfer-Encoding": "chunked",
                "Connection": "keep-alive",
                "x-powered-by": "Express",
                "Vary": "Origin",
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Expose-Headers": "Accept-Ranges,Content-Encoding,Content-Length,Content-Range,Range",
                "Etag": 'W/"301-h/aPj95C/FhjvyhIw0tqK5Kjt3M"',
                "x-fynd-trace-id": "99cd4918c812ee1fa3ef573a16390ed7",
                "Via": "1.1 google",
                "CF-Cache-Status": "DYNAMIC",
                "Server": "cloudflare",
                "CF-RAY": "86332f76fd95f2ef-BOM",
                "Content-Encoding": "gzip",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"presignedUrl":{"url":"https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3ab526b08221fd3e5c6facfc101a&pbe=1710243228975&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=376a20ef-cf61-469d-a90f-c35177cc1dd6","fields":{"x-pixb-meta-assetdata":"{\\"orgId\\":3308,\\"type\\":\\"file\\",\\"name\\":\\"asset-8WhaVptV2.jpeg\\",\\"path\\":\\"\\",\\"fileId\\":\\"asset-8WhaVptV2.jpeg\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erase-erasebg-assets\\",\\"s3Key\\":\\"uploads/shiny-tree-8df4f8/original/13859f04-3dc0-4aca-a762-263108fb0323.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[],\\"metadata\\":{\\"source\\":\\"signedUrl\\",\\"publicUploadId\\":\\"376a20ef-cf61-469d-a90f-c35177cc1dd6\\"},\\"overwrite\\":false,\\"filenameOverride\\":false}"}}}',
        }
    },
    "createSignedURLV2_2": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v2.0/upload/signed-url",
            "method": "post",
            "params": {},
            "data": '{"name":"1","path":"testdir","format":"jpeg","access":"public-read","tags":["tag1","tag2"],"metadata":{},"overwrite":false,"filenameOverride":true}',
            "external_call_request_time": "2024-03-12 16:17:27.076950+05:30",
            "status_code": 200,
            "text": '{"presignedUrl":{"url":"https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3525f3ed00997615b1ea845fe172f4d03196fc25f55f05b1526871b8f7a21198&pbe=1710243447213&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=549b722d-66cf-41bb-8e15-07f8f5b9b456","fields":{"x-pixb-meta-assetdata":"{\\"orgId\\":3308,\\"type\\":\\"file\\",\\"name\\":\\"1.jpeg\\",\\"path\\":\\"testdir\\",\\"fileId\\":\\"testdir/1.jpeg\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erase-erasebg-assets\\",\\"s3Key\\":\\"uploads/shiny-tree-8df4f8/original/9d98f7ab-fa76-433d-97a8-6ab7c751d576.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[\\"tag1\\",\\"tag2\\"],\\"metadata\\":{\\"source\\":\\"signedUrl\\",\\"publicUploadId\\":\\"549b722d-66cf-41bb-8e15-07f8f5b9b456\\"},\\"overwrite\\":false,\\"filenameOverride\\":true}"}}}',
            "headers": {
                "Date": "Tue, 12 Mar 2024 10:47:27 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Transfer-Encoding": "chunked",
                "Connection": "keep-alive",
                "x-powered-by": "Express",
                "Vary": "Origin",
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Expose-Headers": "Accept-Ranges,Content-Encoding,Content-Length,Content-Range,Range",
                "Etag": 'W/"304-Z44N5+n55/80skvt1TcG/yrJsRA"',
                "x-fynd-trace-id": "928d3ec67c55aabc58a1b8e24abd5786",
                "Via": "1.1 google",
                "CF-Cache-Status": "DYNAMIC",
                "Server": "cloudflare",
                "CF-RAY": "863334caf8916ebe-BOM",
                "Content-Encoding": "gzip",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"presignedUrl":{"url":"https://api.pixelbin.io/service/public/assets/v1.0/signed-multipart?pbs=3525f3ed00997615b1ea845fe172f4d03196fc25f55f05b1526871b8f7a21198&pbe=1710243447213&pbt=ca1bdc76-9498-4353-385d-61e190c5c663&pbo=3308&pbu=549b722d-66cf-41bb-8e15-07f8f5b9b456","fields":{"x-pixb-meta-assetdata":"{\\"orgId\\":3308,\\"type\\":\\"file\\",\\"name\\":\\"1.jpeg\\",\\"path\\":\\"testdir\\",\\"fileId\\":\\"testdir/1.jpeg\\",\\"format\\":\\"jpeg\\",\\"s3Bucket\\":\\"erase-erase-erasebg-assets\\",\\"s3Key\\":\\"uploads/shiny-tree-8df4f8/original/9d98f7ab-fa76-433d-97a8-6ab7c751d576.jpeg\\",\\"access\\":\\"public-read\\",\\"tags\\":[\\"tag1\\",\\"tag2\\"],\\"metadata\\":{\\"source\\":\\"signedUrl\\",\\"publicUploadId\\":\\"549b722d-66cf-41bb-8e15-07f8f5b9b456\\"},\\"overwrite\\":false,\\"filenameOverride\\":true}"}}}',
        }
    },
    "updateFile1": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/files/1",
            "method": "patch",
            "params": {},
            "data": {"name": "1_"},
            "external_call_request_time": "2023-03-07 11:35:30.451516+05:30",
            "status_code": 200,
            "text": '{"_id":"24e57515-3b15-48a3-865f-c227488498cf","name":"1_","path":"","fileId":"1_","format":"png","assetType":"image","access":"public-read","size":155108,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/1_.png","meta":{},"kvStore":[],"height":500,"width":500,"createdAt":"2023-03-06T10:13:07.315Z","updatedAt":"2023-03-07T06:05:30.548Z"}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 06:05:30 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "410",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"19a-l3XTtYszDZ/D1B90GbaoGGu1ico"',
                "X-Fynd-Trace-Id": "91f1d78790a5a5f9c4386f9fcb2d22e4",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"24e57515-3b15-48a3-865f-c227488498cf","name":"1_","path":"","fileId":"1_","format":"png","assetType":"image","access":"public-read","size":155108,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/1_.png","meta":{},"kvStore":[],"height":500,"width":500,"createdAt":"2023-03-06T10:13:07.315Z","updatedAt":"2023-03-07T06:05:30.548Z"}',
        }
    },
    "updateFile2": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/files/testdir/1",
            "method": "patch",
            "params": {},
            "data": {
                "name": "testdir_",
                "path": "testdir",
                "access": "private",
                "isActive": True,
                "tags": ["updated-tag1", "updated-tag2"],
                "metadata": {"key": "value"},
            },
            "external_call_request_time": "2023-03-07 11:49:59.273839+05:30",
            "status_code": 200,
            "text": '{"_id":"9b95ddff-9bef-4a67-a1b1-01c7905eaf23","name":"testdir_","path":"testdir","fileId":"testdir/testdir_","format":"png","assetType":"image","access":"private","size":155108,"isActive":true,"tags":["updated-tag1","updated-tag2"],"metadata":{"key":"value"},"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/testdir/testdir_.png","meta":{},"kvStore":[],"height":500,"width":500,"createdAt":"2023-03-07T06:19:47.949Z","updatedAt":"2023-03-07T06:19:59.404Z"}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 06:19:59 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "472",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"1d8-S1hkMu1CppEOz0bkr2e2qrg+eJU"',
                "X-Fynd-Trace-Id": "44420273468e3631bb7e271b8c9d852e",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"9b95ddff-9bef-4a67-a1b1-01c7905eaf23","name":"testdir_","path":"testdir","fileId":"testdir/testdir_","format":"png","assetType":"image","access":"private","size":155108,"isActive":true,"tags":["updated-tag1","updated-tag2"],"metadata":{"key":"value"},"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/testdir/testdir_.png","meta":{},"kvStore":[],"height":500,"width":500,"createdAt":"2023-03-07T06:19:47.949Z","updatedAt":"2023-03-07T06:19:59.404Z"}',
        }
    },
    "getFileByFileId": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/files/testdir/2",
            "method": "get",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 12:05:34.546909+05:30",
            "status_code": 200,
            "text": '{"_id":"044ed804-c165-4f7f-87e4-77dd75633a3f","name":"2","path":"testdir","fileId":"testdir/2","format":"jpeg","assetType":"image","access":"public-read","size":62511,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/testdir/2.jpeg","meta":{},"kvStore":[],"height":760,"width":1140,"createdAt":"2023-03-07T06:29:37.721Z","updatedAt":"2023-03-07T06:29:37.721Z"}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 06:35:34 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "432",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"1b0-pIMoHHGhF2oWzXdC83Tfy+QEAmk"',
                "X-Fynd-Trace-Id": "2785098af88fd006d1661e7cbeef1b76",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"044ed804-c165-4f7f-87e4-77dd75633a3f","name":"2","path":"testdir","fileId":"testdir/2","format":"jpeg","assetType":"image","access":"public-read","size":62511,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/testdir/2.jpeg","meta":{},"kvStore":[],"height":760,"width":1140,"createdAt":"2023-03-07T06:29:37.721Z","updatedAt":"2023-03-07T06:29:37.721Z"}',
        }
    },
    "deleteFile": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/files/1_",
            "method": "delete",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 12:11:14.561397+05:30",
            "status_code": 200,
            "text": '{"_id":"24e57515-3b15-48a3-865f-c227488498cf","name":"1_","path":"","fileId":"1_","format":"png","assetType":"image","access":"public-read","size":155108,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/1_.png","meta":{},"kvStore":[],"height":500,"width":500,"createdAt":"2023-03-06T10:13:07.315Z","updatedAt":"2023-03-07T06:41:04.540Z"}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 06:41:14 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "410",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"19a-Ct33UeKrSCPeP8/1Cxfzh8PKK2Y"',
                "X-Fynd-Trace-Id": "bbd5b3d34b6b1fdfe36f692caaa1c165",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"24e57515-3b15-48a3-865f-c227488498cf","name":"1_","path":"","fileId":"1_","format":"png","assetType":"image","access":"public-read","size":155108,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/1_.png","meta":{},"kvStore":[],"height":500,"width":500,"createdAt":"2023-03-06T10:13:07.315Z","updatedAt":"2023-03-07T06:41:04.540Z"}',
        }
    },
    "deleteFiles": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/files/delete",
            "method": "post",
            "params": {},
            "data": '{"ids":["9d331030-b695-475e-9d4a-a660696d5fa5","aaf3f9c4-18bc-4aa5-8cac-2c45dd8df889"]}',
            "external_call_request_time": "2023-03-16 16:12:05.509864+05:30",
            "status_code": 200,
            "text": '[{"_id":"9d331030-b695-475e-9d4a-a660696d5fa5","name":"2","path":"","fileId":"2","format":"jpeg","assetType":"image","access":"public-read","size":62511,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/dawn-rain-2883/original/2.jpeg","meta":{},"kvStore":[],"height":760,"width":1140,"createdAt":"2023-03-09T13:05:49.420Z","updatedAt":"2023-03-09T13:05:49.420Z"},{"_id":"aaf3f9c4-18bc-4aa5-8cac-2c45dd8df889","name":"download_copy_4_2","path":"","fileId":"download_copy_4_2","format":"png","assetType":"image","access":"public-read","size":3055718,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/dawn-rain-2883/original/download_copy_4_2.png","meta":{},"kvStore":[],"height":960,"width":1440,"createdAt":"2023-03-09T12:43:35.570Z","updatedAt":"2023-03-09T12:43:35.570Z"}]',
            "headers": {
                "Date": "Thu, 16 Mar 2023 10:42:05 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "859",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"35b-ve0cdzX8M4eOTw/g1sf3lRuOR/E"',
                "X-Fynd-Trace-Id": "a76bd33fe4b405b879ce3ac53f53f2e8",
            },
            "cookies": {},
            "error_message": "",
            "content": b'[{"_id":"9d331030-b695-475e-9d4a-a660696d5fa5","name":"2","path":"","fileId":"2","format":"jpeg","assetType":"image","access":"public-read","size":62511,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/dawn-rain-2883/original/2.jpeg","meta":{},"kvStore":[],"height":760,"width":1140,"createdAt":"2023-03-09T13:05:49.420Z","updatedAt":"2023-03-09T13:05:49.420Z"},{"_id":"aaf3f9c4-18bc-4aa5-8cac-2c45dd8df889","name":"download_copy_4_2","path":"","fileId":"download_copy_4_2","format":"png","assetType":"image","access":"public-read","size":3055718,"isActive":true,"tags":[],"metadata":{"source":"direct"},"url":"https://cdn.pixelbin.io/v2/dawn-rain-2883/original/download_copy_4_2.png","meta":{},"kvStore":[],"height":960,"width":1440,"createdAt":"2023-03-09T12:43:35.570Z","updatedAt":"2023-03-09T12:43:35.570Z"}]',
        }
    },
    "updateFolder": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/folders/testdir",
            "method": "patch",
            "params": {},
            "data": {"isActive": True},
            "external_call_request_time": "2023-03-07 12:23:52.464810+05:30",
            "status_code": 200,
            "text": '{"_id":"7e221151-3225-439c-9e77-4c5f38f1c45c","name":"testdir","path":"","isActive":true}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 06:53:52 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "89",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"59-ygaS23E8GxTSwb4Bl9BNlMVvaRE"',
                "X-Fynd-Trace-Id": "3b83a0d10b71ee1d994bf7f66074b6cc",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"7e221151-3225-439c-9e77-4c5f38f1c45c","name":"testdir","path":"","isActive":true}',
        }
    },
    "getFolderDetails": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/folders",
            "method": "get",
            "params": {"name": "testdir"},
            "data": None,
            "external_call_request_time": "2023-03-07 14:28:59.874977+05:30",
            "status_code": 200,
            "text": '{"_id":"7e221151-3225-439c-9e77-4c5f38f1c45c","createdAt":"2023-03-07T05:13:40.417Z","updatedAt":"2023-03-07T07:21:46.790Z","isActive":true,"orgId":"782","type":"folder","name":"testdir","path":"","fileId":null,"format":null,"size":null,"tags":null,"metadata":null,"access":null,"width":null,"height":null,"meta":{},"kvStore":[],"context":null,"assetType":null}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 08:59:00 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "361",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"169-Q4ppD8fYZmcRLgPiX6K4TsWq0c8"',
                "X-Fynd-Trace-Id": "ea505aeb4278d31aa5c36728b38a0570",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"7e221151-3225-439c-9e77-4c5f38f1c45c","createdAt":"2023-03-07T05:13:40.417Z","updatedAt":"2023-03-07T07:21:46.790Z","isActive":true,"orgId":"782","type":"folder","name":"testdir","path":"","fileId":null,"format":null,"size":null,"tags":null,"metadata":null,"access":null,"width":null,"height":null,"meta":{},"kvStore":[],"context":null,"assetType":null}',
        }
    },
    "getFolderAncestors": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/folders/4a08fc27-e8ee-4e2d-9438-85c1ba07423e/ancestors",
            "method": "get",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 14:43:42.908501+05:30",
            "status_code": 200,
            "text": '{"folder":{"_id":"4a08fc27-e8ee-4e2d-9438-85c1ba07423e","path":"nested","name":"folder","type":"folder"},"ancestors":[{"_id":"a2ff6554-75e2-4182-a6dc-8eecb8bb6e94","path":"","name":"nested","type":"folder"}]}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 09:13:43 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "208",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"d0-fE5+leCMnxTID5Y6Ox5OFj0/TMk"',
                "X-Fynd-Trace-Id": "57f46c540070334392a2ad5c3a445cb3",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"folder":{"_id":  "4a08fc27-e8ee-4e2d-9438-85c1ba07423e","path":"nested","name":"folder","type":"folder"},"ancestors":[{"_id":"a2ff6554-75e2-4182-a6dc-8eecb8bb6e94","path":"","name":"nested","type":"folder"}]}',
        }
    },
    "deleteFolder": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/folders/b89b2fbb-c520-444a-98a4-f3c20276c0a3",
            "method": "delete",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 15:01:30.181341+05:30",
            "status_code": 200,
            "text": '{"_id":"b89b2fbb-c520-444a-98a4-f3c20276c0a3","name":"x","path":"","isActive":true}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 09:31:30 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "83",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"53-wpTKAi2KpEVtnuZRTpYQwmifUxs"',
                "X-Fynd-Trace-Id": "ac423f5ac6c341aa7ba0fbefcd1e3d0f",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"b89b2fbb-c520-444a-98a4-f3c20276c0a3","name":"x","path":"","isActive":true}',
        }
    },
    "getModules": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/playground/plugins",
            "method": "get",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 15:12:03.731927+05:30",
            "status_code": 200,
            "text": '{"delimiters": {"operationSeparator": "~","parameterSeparator": ","},"plugins": {"erase": {"identifier": "erase","name": "EraseBG","description": "EraseBG Background Removal Module","credentials": {"required": false},"isHeavy": true,"operations": [{"params": [{"name": "Industry Type","type": "enum","enum": ["general","ecommerce","car"],"preview": [	"car"],"default": "general","identifier": "i","title": "Industry type"},{"name": "Add Shadow","title": "Add Shadow (cars only)","type": "boolean","default": false,"preview": false,"identifier": "shadow"}],"displayName": "Erase BG","method": "bg","description": "Remove the background of any image"}],"enabled": true},"presets": []}}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 09:42:03 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "21099",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"526b-RhyvbjCIU49PDZf8L1JunI4gtGs"',
                "X-Fynd-Trace-Id": "974cb38de8be4efe53fade8b98e5686f",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"delimiters": {"operationSeparator": "~","parameterSeparator": ","},"plugins": {"erase": {"identifier": "erase","name": "EraseBG","description": "EraseBG Background Removal Module","credentials": {"required": false},"isHeavy": true,"operations": [{"params": [{"name": "Industry Type","type": "enum","enum": ["general","ecommerce","car"],"preview": [	"car"],"default": "general","identifier": "i","title": "Industry type"},{"name": "Add Shadow","title": "Add Shadow (cars only)","type": "boolean","default": false,"preview": false,"identifier": "shadow"}],"displayName": "Erase BG","method": "bg","description": "Remove the background of any image"}],"enabled": true},"presets": []}}',
        }
    },
    "getModule": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/playground/plugins/erase",
            "method": "get",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 15:35:54.094449+05:30",
            "status_code": 200,
            "text": '{"identifier":"erase","name":"EraseBG","description":"EraseBG Background Removal Module","credentials":{"required":false},"isHeavy":true,"operations":[{"params":[{"name":"Industry Type","type":"enum","enum":["general","ecommerce","car"],"preview":["car"],"default":"general","identifier":"i","title":"Industry type"},{"name":"Add Shadow","title":"Add Shadow (cars only)","type":"boolean","default":false,"preview":false,"identifier":"shadow"}],"displayName":"Erase BG","method":"bg","description":"Remove the background of any image"}],"enabled":true}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 10:05:54 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "551",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"227-m6v5sdq0ifBZGbaCla1tmD104T8"',
                "X-Fynd-Trace-Id": "599f43d5e27a306b63c896d24874fdb0",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"identifier":"erase","name":"EraseBG","description":"EraseBG Background Removal Module","credentials":{"required":false},"isHeavy":true,"operations":[{"params":[{"name":"Industry Type","type":"enum","enum":["general","ecommerce","car"],"preview":["car"],"default":"general","identifier":"i","title":"Industry type"},{"name":"Add Shadow","title":"Add Shadow (cars only)","type":"boolean","default":false,"preview":false,"identifier":"shadow"}],"displayName":"Erase BG","method":"bg","description":"Remove the background of any image"}],"enabled":true}',
        }
    },
    "addCredentials": {
        "apiKey": "abcdefghi",
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/credentials",
            "method": "post",
            "params": {},
            "data": {
                "credentials": {"apiKey": "abcdefghi"},
                "pluginId": "remove",
            },
            "external_call_request_time": "2023-03-07 15:43:24.592615+05:30",
            "status_code": 200,
            "text": '{"orgId":782,"pluginId":"remove","_id":"dummykey","createdAt":"2023-03-07T10:13:25.367Z","updatedAt":"2023-03-07T10:13:25.367Z"}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 10:13:25 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "156",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"9c-5gkwGJgiDqWFng07aSo5CRDbOh0"',
                "X-Fynd-Trace-Id": "cb94c43cdc96ba30cf77253be330f254",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"orgId":782,"pluginId":"remove","_id":"dummykey","createdAt":"2023-03-07T10:13:25.367Z","updatedAt":"2023-03-07T10:13:25.367Z"}',
        },
    },
    "updateCredentials": {
        "apiKey": "abcdefghi",
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/credentials/remove",
            "method": "patch",
            "params": {},
            "data": {"credentials": {"apiKey": "abcdefghi"}},
            "external_call_request_time": "2023-03-07 15:55:24.592957+05:30",
            "status_code": 200,
            "text": '{"updatedAt":"2023-03-07T10:25:25.309Z","_id":"9627599a-9286-4829-9bd1-675f3319191d","createdAt":"2023-03-07T10:13:25.367Z","isActive":true,"orgId":"782","pluginId":"remove"}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 10:25:25 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "174",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"ae-5/pGXDbW4kSKm/BBHNaD27jic+8"',
                "X-Fynd-Trace-Id": "5544fa969cdced46b25457301f4430f6",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"updatedAt":"2023-03-07T10:25:25.309Z","_id":"9627599a-9286-4829-9bd1-675f3319191d","createdAt":"2023-03-07T10:13:25.367Z","isActive":true,"orgId":"782","pluginId":"remove"}',
        },
    },
    "deleteCredentials": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/credentials/remove",
            "method": "delete",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 16:04:25.004642+05:30",
            "status_code": 200,
            "text": '{"_id":"9627599a-9286-4829-9bd1-675f3319191d","createdAt":"2023-03-07T10:13:25.367Z","updatedAt":"2023-03-07T10:33:04.839Z","isActive":true,"orgId":"782","pluginId":"remove","credentials":{"apiKey":"abcdefghi"}}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 10:34:25 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "226",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"e2-m1NUezmx9UzpUdPjDS3o5SqaRK0"',
                "X-Fynd-Trace-Id": "c763b81619962a12e2109eb341810fa6",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"9627599a-9286-4829-9bd1-675f3319191d","createdAt":"2023-03-07T10:13:25.367Z","updatedAt":"2023-03-07T10:33:04.839Z","isActive":true,"orgId":"782","pluginId":"remove","credentials":{"apiKey":"abcdefghi"}}',
        }
    },
    "addPreset": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/presets",
            "method": "post",
            "params": {},
            "data": {
                "presetName": "p1",
                "transformation": "t.flip()~t.flop()",
                "params": {
                    "w": {"type": "integer", "default": 200},
                    "h": {"type": "integer", "default": 400},
                },
            },
            "external_call_request_time": "2023-03-07 16:08:37.880349+05:30",
            "status_code": 200,
            "text": '{"orgId":"782","presetName":"p1","transformation":"t.flip()~t.flop()","params":{},"_id":"970f0bae-7cfb-4468-bb39-177554ca6788","createdAt":"2023-03-07T10:38:38.044Z","updatedAt":"2023-03-07T10:38:38.044Z","isActive":true,"archived":false}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 10:38:38 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "238",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"ee-MfSZxUDQ9WUKNJVdRULMXuLEHMg"',
                "X-Fynd-Trace-Id": "e9702a34138aab3572db9bd3a4d04363",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"orgId":"782","presetName":"p1","transformation":"t.flip()~t.flop()","params":{},"_id":"970f0bae-7cfb-4468-bb39-177554ca6788","createdAt":"2023-03-07T10:38:38.044Z","updatedAt":"2023-03-07T10:38:38.044Z","isActive":true,"archived":false}',
        }
    },
    "getPresets": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/presets",
            "method": "get",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 16:13:21.731213+05:30",
            "status_code": 200,
            "text": '{"items":[{"_id":"970f0bae-7cfb-4468-bb39-177554ca6788","createdAt":"2023-03-07T10:38:38.044Z","updatedAt":"2023-03-07T10:38:38.044Z","isActive":true,"orgId":"782","presetName":"p1","transformation":"t.flip()~t.flop()","archived":false,"params":{}}],"page":{"type":"number","size":1,"hasNext":false,"itemTotal":1}}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 10:43:21 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "314",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"13a-vckVtAdUJ42kFYwvPaAIuiOxJoU"',
                "X-Fynd-Trace-Id": "4a589c9ea76f6036dd14aa74ad9c27d0",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"items":[{"_id":"970f0bae-7cfb-4468-bb39-177554ca6788","createdAt":"2023-03-07T10:38:38.044Z","updatedAt":"2023-03-07T10:38:38.044Z","isActive":true,"orgId":"782","presetName":"p1","transformation":"t.flip()~t.flop()","archived":false,"params":{}}],"page":{"type":"number","size":1,"hasNext":false,"itemTotal":1}}',
        }
    },
    "updatePresets": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/presets/p1",
            "method": "patch",
            "params": {},
            "data": {"archived": True},
            "external_call_request_time": "2023-03-07 16:26:53.802983+05:30",
            "status_code": 200,
            "text": '{"archived":true,"updatedAt":"2023-03-07T10:56:53.952Z","_id":"970f0bae-7cfb-4468-bb39-177554ca6788","createdAt":"2023-03-07T10:38:38.044Z","isActive":true,"orgId":"782","presetName":"p1","transformation":"t.flip()~t.flop()","params":{}}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 10:56:53 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "237",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"ed-htZ51EXGMSThbAwtQEGCEdYI/mk"',
                "X-Fynd-Trace-Id": "778cd6f6c40bfe6ccd3fc2bacac8bd62",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"archived":true,"updatedAt":"2023-03-07T10:56:53.952Z","_id":"970f0bae-7cfb-4468-bb39-177554ca6788","createdAt":"2023-03-07T10:38:38.044Z","isActive":true,"orgId":"782","presetName":"p1","transformation":"t.flip()~t.flop()","params":{}}',
        }
    },
    "getPreset": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/presets/p1",
            "method": "get",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 16:22:52.411768+05:30",
            "status_code": 200,
            "text": '{"_id":"970f0bae-7cfb-4468-bb39-177554ca6788","createdAt":"2023-03-07T10:38:38.044Z","updatedAt":"2023-03-07T10:38:38.044Z","isActive":true,"orgId":"782","presetName":"p1","transformation":"t.flip()~t.flop()","archived":false,"params":{}}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 10:52:52 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "238",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"ee-qBhSuXb/ZbuZa2L+jPgbA6wQrHc"',
                "X-Fynd-Trace-Id": "03d50db167a4b38c04dea91ce6f09a39",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"970f0bae-7cfb-4468-bb39-177554ca6788","createdAt":"2023-03-07T10:38:38.044Z","updatedAt":"2023-03-07T10:38:38.044Z","isActive":true,"orgId":"782","presetName":"p1","transformation":"t.flip()~t.flop()","archived":false,"params":{}}',
        }
    },
    "deletePreset": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/presets/p1",
            "method": "delete",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 16:29:03.614648+05:30",
            "status_code": 200,
            "text": '{"_id":"970f0bae-7cfb-4468-bb39-177554ca6788","createdAt":"2023-03-07T10:38:38.044Z","updatedAt":"2023-03-07T10:58:27.414Z","isActive":true,"orgId":"782","presetName":"p1","transformation":"t.flip()~t.flop()","archived":true,"params":{}}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 10:59:03 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "237",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"ed-5xLhCOYscHVomVU6XchpwkIUdTU"',
                "X-Fynd-Trace-Id": "fb9a6fb7e61d084c22d76684a4bfa297",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"970f0bae-7cfb-4468-bb39-177554ca6788","createdAt":"2023-03-07T10:38:38.044Z","updatedAt":"2023-03-07T10:58:27.414Z","isActive":true,"orgId":"782","presetName":"p1","transformation":"t.flip()~t.flop()","archived":true,"params":{}}',
        }
    },
    "getDefaultAssetForPlayground": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/assets/v1.0/playground/default",
            "method": "get",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-07 16:36:33.127599+05:30",
            "status_code": 200,
            "text": '{"_id":"8bdbd34b-80f8-4dad-967c-b30d6f70f83b","createdAt":"2023-03-07T06:45:16.841Z","updatedAt":"2023-03-07T06:45:16.841Z","isActive":true,"orgId":"782","type":"file","name":"playground-default","path":"__playground","fileId":"__playground/playground-default","format":"jpeg","size":218409,"tags":[],"metadata":{"source":"direct"},"access":"public-read","width":1140,"height":760,"meta":{},"kvStore":{},"context":{"req":{"query":{},"headers":{}},"meta":{"size":218409,"width":1140,"format":"jpeg","height":760},"steps":[]},"assetType":null,"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/__playground/playground-default.jpeg"}',
            "headers": {
                "Date": "Tue, 07 Mar 2023 11:06:33 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "644",
                "Connection": "keep-alive",
                "X-Powered-By": "Express",
                "Etag": 'W/"284-nb+dfdav6xB7q/L9tIGBqiikBjc"',
                "X-Fynd-Trace-Id": "08aef7c7348c2d8577882efaf875293d",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"_id":"8bdbd34b-80f8-4dad-967c-b30d6f70f83b","createdAt":"2023-03-07T06:45:16.841Z","updatedAt":"2023-03-07T06:45:16.841Z","isActive":true,"orgId":"782","type":"file","name":"playground-default","path":"__playground","fileId":"__playground/playground-default","format":"jpeg","size":218409,"tags":[],"metadata":{"source":"direct"},"access":"public-read","width":1140,"height":760,"meta":{},"kvStore":{},"context":{"req":{"query":{},"headers":{}},"meta":{"size":218409,"width":1140,"format":"jpeg","height":760},"steps":[]},"assetType":null,"url":"https://cdn.pixelbin.io/v2/shrill-bread-710314/original/__playground/playground-default.jpeg"}',
        }
    },
    "getAppOrgDetails": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/organization/v1.0/apps/info",
            "method": "get",
            "params": {},
            "data": None,
            "external_call_request_time": "2023-03-16 16:20:58.370522+05:30",
            "status_code": 200,
            "text": '{"app":{"name":"Test Token","permissions":["read"],"orgId":1285,"token":"token-test-id","createdAt":"2023-02-22T10:17:27.000Z","updatedAt":"2023-02-22T10:17:27.000Z","_id":950,"active":true},"org":{"_id":1285,"name":"Test Organization","cloudName":"dawn-rain-2883","ownerId":"6ad869570e02e1d7ec1f92a2","active":true,"createdAt":"2023-02-22T10:16:27.000Z","updatedAt":"2023-02-22T10:16:55.000Z","restrictions":[],"rateLimit":null}}',
            "headers": {
                "Date": "Thu, 16 Mar 2023 10:50:58 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "449",
                "Connection": "keep-alive",
                "Etag": 'W/"1c1-Z+uPQxlB+Xy6DZGd1tEbCBFo2V0"',
                "X-Fynd-Trace-Id": "cfbe0b4abccf34a19f56ad6dae0b8623",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"app":{"name":"Test Token","permissions":["read"],"orgId":1285,"token":"token-test-id","createdAt":"2023-02-22T10:17:27.000Z","updatedAt":"2023-02-22T10:17:27.000Z","_id":950,"active":true},"org":{"_id":1285,"name":"Test Organization","cloudName":"dawn-rain-2883","ownerId":"6ad869570e02e1d7ec1f92a2","active":true,"createdAt":"2023-02-22T10:16:27.000Z","updatedAt":"2023-02-22T10:16:55.000Z","restrictions":[],"rateLimit":null}}',
        }
    },
    "getTransformationContext": {
        "response": {
            "url": "https://api.pixelbin.io/service/platform/transformation/context?url=/v2/still-band-3297fc/original/test.webp",
            "method": "get",
            "params": {},
            "data": {
                "context": {
                    "req": {"query": {}, "headers": {}},
                    "meta": {
                        "size": 218409,
                        "width": 1140,
                        "format": "jpeg",
                        "height": 760,
                    },
                    "steps": [],
                    "headers": {
                        "host": "cdn.pixelbin.io",
                        "x-real-ip": "125.22.87.250",
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "accept-encoding": "br,gzip",
                        "accept-language": "en-US,en;q=0.9",
                    },
                    "params": {},
                }
            },
            "external_call_request_time": "2023-03-16 16:20:58.370522+05:30",
            "status_code": 200,
            "text": '{"app":{"name":"Test Token","permissions":["read"],"orgId":1285,"token":"token-test-id","createdAt":"2023-02-22T10:17:27.000Z","updatedAt":"2023-02-22T10:17:27.000Z","_id":950,"active":true},"org":{"_id":1285,"name":"Test Organization","cloudName":"dawn-rain-2883","ownerId":"6ad869570e02e1d7ec1f92a2","active":true,"createdAt":"2023-02-22T10:16:27.000Z","updatedAt":"2023-02-22T10:16:55.000Z","restrictions":[],"rateLimit":null}}',
            "headers": {
                "Date": "Thu, 16 Mar 2023 10:50:58 GMT",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "449",
                "Connection": "keep-alive",
                "Etag": 'W/"1c1-Z+uPQxlB+Xy6DZGd1tEbCBFo2V0"',
                "X-Fynd-Trace-Id": "cfbe0b4abccf34a19f56ad6dae0b8623",
            },
            "cookies": {},
            "error_message": "",
            "content": b'{"app":{"name":"Test Token","permissions":["read"],"orgId":1285,"token":"token-test-id","createdAt":"2023-02-22T10:17:27.000Z","updatedAt":"2023-02-22T10:17:27.000Z","_id":950,"active":true},"org":{"_id":1285,"name":"Test Organization","cloudName":"dawn-rain-2883","ownerId":"6ad869570e02e1d7ec1f92a2","active":true,"createdAt":"2023-02-22T10:16:27.000Z","updatedAt":"2023-02-22T10:16:55.000Z","restrictions":[],"rateLimit":null}}',
        }
    },
}

URLS_TO_OBJ = [
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/original/W2.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "original",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)/W2.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:600,w:800)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                }
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/z-slug/t.resize(h:600,w:800)/W2.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:600,w:800)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": "z-slug",
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                }
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)~t.rotate(a:-249)/W2.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:600,w:800)~t.rotate(a:-249)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                },
                {
                    "plugin": "t",
                    "name": "rotate",
                    "values": [{"key": "a", "value": "-249"}],
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)~t.rotate(a:-249)~t.flip()~t.trim(t:217)/W2.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:600,w:800)~t.rotate(a:-249)~t.flip()~t.trim(t:217)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                },
                {
                    "plugin": "t",
                    "name": "rotate",
                    "values": [{"key": "a", "value": "-249"}],
                },
                {"plugin": "t", "name": "flip"},
                {
                    "plugin": "t",
                    "name": "trim",
                    "values": [{"key": "t", "value": "217"}],
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)/W2.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                    "values": [
                        {"key": "a", "value": "100"},
                        {"key": "b", "value": "2.1"},
                        {"key": "c", "value": "test"},
                    ],
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:200,w:100)~p:preset1",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1()/W2.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:200,w:100)~p:preset1()",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1(a:12/W2.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                    "values": [{"key": "a", "value": "12"}],
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/feel/erase.bg(shadow:true)~t.merge(m:underlay,i:eU44YkFJOHlVMmZrWVRDOUNTRm1D,b:screen,r:true)/MZZKB3e1hT48o0NYJ2Kxh.jpeg?dpr=2.0&f_auto=true",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "baseUrl": "https://cdn.pixelbin.io",
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
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/feel/erase.bg()/MZZKB3e1hT48o0NYJ2Kxh.jpeg?dpr=auto",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "baseUrl": "https://cdn.pixelbin.io",
            "filePath": "MZZKB3e1hT48o0NYJ2Kxh.jpeg",
            "pattern": "erase.bg()",
            "cloudName": "feel",
            "options": {
                "dpr": "auto",
            },
            "zone": None,
            "transformations": [
                {
                    "plugin": "erase",
                    "name": "bg",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/feel/erase.bg()/asbc.jpeg?f_auto=false",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "baseUrl": "https://cdn.pixelbin.io",
            "filePath": "asbc.jpeg",
            "pattern": "erase.bg()",
            "cloudName": "feel",
            "options": {
                "f_auto": False,
            },
            "zone": None,
            "transformations": [
                {
                    "plugin": "erase",
                    "name": "bg",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/wrkr/image.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": True,
            "workerPath": "image.jpeg",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/wrkr/resize:w200,h200/image.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/abcdef/wrkr/image.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": True,
            "workerPath": "image.jpeg",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/abcdef/wrkr/resize:w200,h200/image.jpeg",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/abcdef/wrkr/resize:w200,h200/image.jpeg?dpr=1.0",
        "opts": {
            "is_custom_domain": False,
        },
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
            "options": {
                "dpr": 1,
            },
        },
    },
    # custom domain urls
    {
        "url": "https://cdn.twist.vision/v2/original/W2.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "original",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:600,w:800)/W2.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "t.resize(h:600,w:800)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                }
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/z-slug/t.resize(h:600,w:800)/W2.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "t.resize(h:600,w:800)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": "z-slug",
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                }
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:600,w:800)~t.rotate(a:-249)/W2.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "t.resize(h:600,w:800)~t.rotate(a:-249)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                },
                {
                    "plugin": "t",
                    "name": "rotate",
                    "values": [{"key": "a", "value": "-249"}],
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:600,w:800)~t.rotate(a:-249)~t.flip()~t.trim(t:217)/W2.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "t.resize(h:600,w:800)~t.rotate(a:-249)~t.flip()~t.trim(t:217)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                },
                {
                    "plugin": "t",
                    "name": "rotate",
                    "values": [{"key": "a", "value": "-249"}],
                },
                {"plugin": "t", "name": "flip"},
                {
                    "plugin": "t",
                    "name": "trim",
                    "values": [{"key": "t", "value": "217"}],
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)/W2.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                    "values": [
                        {"key": "a", "value": "100"},
                        {"key": "b", "value": "2.1"},
                        {"key": "c", "value": "test"},
                    ],
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "t.resize(h:200,w:100)~p:preset1",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:200,w:100)~p:preset1()/W2.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "t.resize(h:200,w:100)~p:preset1()",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:200,w:100)~p:preset1(a:12/W2.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                    "values": [{"key": "a", "value": "12"}],
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/erase.bg(shadow:true)~t.merge(m:underlay,i:eU44YkFJOHlVMmZrWVRDOUNTRm1D,b:screen,r:true)/MZZKB3e1hT48o0NYJ2Kxh.jpeg?dpr=2.0&f_auto=true",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "baseUrl": "https://cdn.twist.vision",
            "filePath": "MZZKB3e1hT48o0NYJ2Kxh.jpeg",
            "pattern": "erase.bg(shadow:true)~t.merge(m:underlay,i:eU44YkFJOHlVMmZrWVRDOUNTRm1D,b:screen,r:true)",
            "cloudName": None,
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
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/erase.bg()/MZZKB3e1hT48o0NYJ2Kxh.jpeg?dpr=auto",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "baseUrl": "https://cdn.twist.vision",
            "filePath": "MZZKB3e1hT48o0NYJ2Kxh.jpeg",
            "pattern": "erase.bg()",
            "cloudName": None,
            "options": {
                "dpr": "auto",
            },
            "zone": None,
            "transformations": [
                {
                    "plugin": "erase",
                    "name": "bg",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/erase.bg()/asbc.jpeg?f_auto=false",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "baseUrl": "https://cdn.twist.vision",
            "filePath": "asbc.jpeg",
            "pattern": "erase.bg()",
            "cloudName": None,
            "options": {
                "f_auto": False,
            },
            "zone": None,
            "transformations": [
                {
                    "plugin": "erase",
                    "name": "bg",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/original/z0/orgs/33/skills/icons/Fynd_Platform_Commerce_Extension.png",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "original",
            "filePath": "z0/orgs/33/skills/icons/Fynd_Platform_Commerce_Extension.png",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/original/z0/orgs/33/wrkr/icons/Fynd_Platform_Commerce_Extension.png",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "original",
            "filePath": "z0/orgs/33/wrkr/icons/Fynd_Platform_Commerce_Extension.png",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/wrkr/image.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": True,
            "workerPath": "image.jpeg",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/wrkr/resize:w200,h200/image.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/abcdef/wrkr/image.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": True,
            "workerPath": "image.jpeg",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/abcdef/wrkr/resize:w200,h200/image.jpeg",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/abcdef/wrkr/resize:w200,h200/image.jpeg?dpr=1.0",
        "opts": {
            "is_custom_domain": True,
        },
        "obj": {
            "version": "v2",
            "cloudName": None,
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
            "options": {
                "dpr": 1,
            },
        },
    },
]


OBJ_TO_URL = [
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:600,w:800)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                }
            ],
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/z-slug/t.resize(h:600,w:800)/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:600,w:800)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": "z-slug",
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                }
            ],
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)~t.rotate(a:-249)/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:600,w:800)~t.rotate(a:-249)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                },
                {
                    "plugin": "t",
                    "name": "rotate",
                    "values": [{"key": "a", "value": "-249"}],
                },
            ],
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:600,w:800)~t.rotate(a:-249)~t.flip()~t.trim(t:217)/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:600,w:800)~t.rotate(a:-249)~t.flip()~t.trim(t:217)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                },
                {
                    "plugin": "t",
                    "name": "rotate",
                    "values": [{"key": "a", "value": "-249"}],
                },
                {"plugin": "t", "name": "flip"},
                {
                    "plugin": "t",
                    "name": "trim",
                    "values": [{"key": "t", "value": "217"}],
                },
            ],
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                    "values": [
                        {"key": "a", "value": "100"},
                        {"key": "b", "value": "2.1"},
                        {"key": "c", "value": "test"},
                    ],
                },
            ],
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:200,w:100)~p:preset1",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                },
            ],
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1(a:12)/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                    "values": [{"key": "a", "value": "12"}],
                },
            ],
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {"plugin": "p", "name": "preset1", "values": []},
            ],
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:,w:100)~p:preset1/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": ""},
                        {"key": "w", "value": "100"},
                    ],
                },
                {"plugin": "p", "name": "preset1", "values": []},
            ],
        },
        "error": "value not specified for 'h' in 'resize'",
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [{"value": ""}, {"key": "w", "value": "100"}],
                },
                {"plugin": "p", "name": "preset1", "values": []},
            ],
        },
        "error": "key not specified in 'resize'",
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [{}, {"key": "w", "value": "100"}],
                },
                {"plugin": "p", "name": "preset1", "values": []},
            ],
        },
        "error": "key not specified in 'resize'",
    },
    {
        "url": "https://cdn.pixelbin.io/v2/feel/erase.bg(shadow:true)~t.merge(m:underlay,i:eU44YkFJOHlVMmZrWVRDOUNTRm1D,b:screen,r:true)/MZZKB3e1hT48o0NYJ2Kxh.jpeg?dpr=2.0&f_auto=true",
        "obj": {
            "version": "v2",
            "baseUrl": "https://cdn.pixelbin.io",
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
            ],
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/feel/erase.bg()/MZZKB3e1hT48o0NYJ2Kxh.jpeg?dpr=auto",
        "obj": {
            "version": "v2",
            "baseUrl": "https://cdn.pixelbin.io",
            "filePath": "MZZKB3e1hT48o0NYJ2Kxh.jpeg",
            "pattern": "erase.bg()",
            "cloudName": "feel",
            "options": {
                "dpr": "auto",
            },
            "zone": None,
            "transformations": [
                {
                    "plugin": "erase",
                    "name": "bg",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/feel/erase.bg()/asbc.jpeg?f_auto=false",
        "obj": {
            "version": "v2",
            "baseUrl": "https://cdn.pixelbin.io",
            "filePath": "asbc.jpeg",
            "pattern": "erase.bg()",
            "cloudName": "feel",
            "options": {
                "f_auto": False,
            },
            "zone": None,
            "transformations": [
                {
                    "plugin": "erase",
                    "name": "bg",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/wrkr/image.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "isCustomDomain": False,
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": True,
            "workerPath": "image.jpeg",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/wrkr/resize:w200,h200/image.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "isCustomDomain": False,
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/abcdef/wrkr/image.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "isCustomDomain": False,
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": True,
            "workerPath": "image.jpeg",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/abcdef/wrkr/resize:w200,h200/image.jpeg",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "isCustomDomain": False,
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
        },
    },
    {
        "url": "https://cdn.pixelbin.io/v2/broken-butterfly-3b12f1/abcdef/wrkr/resize:w200,h200/image.jpeg?dpr=1.0",
        "obj": {
            "version": "v2",
            "cloudName": "broken-butterfly-3b12f1",
            "isCustomDomain": False,
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.pixelbin.io",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
            "options": {
                "dpr": 1,
            },
        },
    },
    # custom domain
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:600,w:800)/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:600,w:800)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                }
            ],
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/z-slug/t.resize(h:600,w:800)/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:600,w:800)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": "z-slug",
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                }
            ],
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:600,w:800)~t.rotate(a:-249)/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:600,w:800)~t.rotate(a:-249)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                },
                {
                    "plugin": "t",
                    "name": "rotate",
                    "values": [{"key": "a", "value": "-249"}],
                },
            ],
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:600,w:800)~t.rotate(a:-249)~t.flip()~t.trim(t:217)/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:600,w:800)~t.rotate(a:-249)~t.flip()~t.trim(t:217)",
            "filePath": "W2.jpeg",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "600"},
                        {"key": "w", "value": "800"},
                    ],
                },
                {
                    "plugin": "t",
                    "name": "rotate",
                    "values": [{"key": "a", "value": "-249"}],
                },
                {"plugin": "t", "name": "flip"},
                {
                    "plugin": "t",
                    "name": "trim",
                    "values": [{"key": "t", "value": "217"}],
                },
            ],
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:100,b:2.1,c:test)",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                    "values": [
                        {"key": "a", "value": "100"},
                        {"key": "b", "value": "2.1"},
                        {"key": "c", "value": "test"},
                    ],
                },
            ],
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:200,w:100)~p:preset1",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                },
            ],
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:200,w:100)~p:preset1(a:12)/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {
                    "plugin": "p",
                    "name": "preset1",
                    "values": [{"key": "a", "value": "12"}],
                },
            ],
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": "200"},
                        {"key": "w", "value": "100"},
                    ],
                },
                {"plugin": "p", "name": "preset1", "values": []},
            ],
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:,w:100)~p:preset1/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [
                        {"key": "h", "value": ""},
                        {"key": "w", "value": "100"},
                    ],
                },
                {"plugin": "p", "name": "preset1", "values": []},
            ],
        },
        "error": "value not specified for 'h' in 'resize'",
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [{"value": ""}, {"key": "w", "value": "100"}],
                },
                {"plugin": "p", "name": "preset1", "values": []},
            ],
        },
        "error": "key not specified in 'resize'",
    },
    {
        "url": "https://cdn.twist.vision/v2/t.resize(h:200,w:100)~p:preset1/W2.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "t.resize(h:200,w:100)~p:preset1(a:12",
            "filePath": "W2.jpeg",
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [
                {
                    "plugin": "t",
                    "name": "resize",
                    "values": [{}, {"key": "w", "value": "100"}],
                },
                {"plugin": "p", "name": "preset1", "values": []},
            ],
        },
        "error": "key not specified in 'resize'",
    },
    {
        "url": "https://cdn.twist.vision/v2/erase.bg(shadow:true)~t.merge(m:underlay,i:eU44YkFJOHlVMmZrWVRDOUNTRm1D,b:screen,r:true)/MZZKB3e1hT48o0NYJ2Kxh.jpeg?dpr=2.0&f_auto=true",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "baseUrl": "https://cdn.twist.vision",
            "filePath": "MZZKB3e1hT48o0NYJ2Kxh.jpeg",
            "pattern": "erase.bg(shadow:true)~t.merge(m:underlay,i:eU44YkFJOHlVMmZrWVRDOUNTRm1D,b:screen,r:true)",
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
            ],
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/erase.bg()/MZZKB3e1hT48o0NYJ2Kxh.jpeg?dpr=auto",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "baseUrl": "https://cdn.twist.vision",
            "filePath": "MZZKB3e1hT48o0NYJ2Kxh.jpeg",
            "pattern": "erase.bg()",
            # "cloudName": None,
            "options": {
                "dpr": "auto",
            },
            "zone": None,
            "transformations": [
                {
                    "plugin": "erase",
                    "name": "bg",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/erase.bg()/asbc.jpeg?f_auto=false",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "baseUrl": "https://cdn.twist.vision",
            "filePath": "asbc.jpeg",
            "pattern": "erase.bg()",
            # "cloudName": None,
            "options": {
                "f_auto": False,
            },
            "zone": None,
            "transformations": [
                {
                    "plugin": "erase",
                    "name": "bg",
                },
            ],
            "worker": False,
            "workerPath": "",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/wrkr/image.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": True,
            "workerPath": "image.jpeg",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/wrkr/resize:w200,h200/image.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": None,
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/abcdef/wrkr/image.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": True,
            "workerPath": "image.jpeg",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/abcdef/wrkr/resize:w200,h200/image.jpeg",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
        },
    },
    {
        "url": "https://cdn.twist.vision/v2/abcdef/wrkr/resize:w200,h200/image.jpeg?dpr=1.0",
        "obj": {
            "isCustomDomain": True,
            "version": "v2",
            "pattern": "",
            "filePath": "",
            "options": {},
            "zone": "abcdef",
            "baseUrl": "https://cdn.twist.vision",
            "transformations": [],
            "worker": True,
            "workerPath": "resize:w200,h200/image.jpeg",
            "options": {
                "dpr": 1,
            },
        },
    },
]

SIGN_URL_CASES = [
    {
        "input": {
            "url": "https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg",
            "expiry_seconds": 20,
            "access_key": "c364b7b1-b7b8-4019-99b4-422a46b2bb44",
            "token": "dummy-token",
        },
    },
    {
        "input": {
            "url": "https://test.imagebin.io/v2/original/__playground/playground-default.jpeg",
            "expiry_seconds": 20,
            "access_key": "c364b7b1-b7b8-4019-99b4-422a46b2bb44",
            "token": "dummy-token",
        },
    },
    {
        "input": {
            "url": "https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg",
            "expiry_seconds": "twenty",
            "access_key": "c364b7b1-b7b8-4019-99b4-422a46b2bb44",
            "token": "dummy-token",
        },
        "error": "expiry_seconds must be an integer",
    },
    {
        "input": {
            "url": "https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg?pbs=2e7578ba14ef3294a3cc95209fad9801a6abdc917ab8f98e5d1ffb4645a6289e&pbe=1696403372&pbt=2583",
            "expiry_seconds": 20,
            "access_key": "c364b7b1-b7b8-4019-99b4-422a46b2bb44",
            "token": "dummy-token",
        },
        "error": "URL already has a signature",
    },
]
