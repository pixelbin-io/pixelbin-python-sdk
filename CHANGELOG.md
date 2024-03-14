# 3.2.0

-   Added method for generating V2 Signed Multipart Upload Urls `createSignedUrlV2`

# 3.1.1

-   Fixed regex for Custom Domain URLs

# 3.1.0

-   Added support for generating signed Custom Domain and PixelBin CDN urls

# 3.0.0

-   Fixed bugs parsing `dpr` & `f_auto` in `obj_to_url` & `url_to_obj`
-   Added support for parsing Custom Domains in `obj_to_url` and `url_to_obj`
-   Improved support for worker urls in `obj_to_url` and `url_to_obj`

# 2.2.0

-   Added a method for obtaining the context of a file via url.

# 2.1.1

-   Removed unused model
-   Rewritten test suite to improve test reliability

# 2.1.0

-   Fixed `tags` being stringified inadvertently. If you are experiencing validation errors around `tags` in previous versions, you should upgrade your SDKs.

# 2.0.0

-   method for getting org details has changed from `getAppByToken` => `getAppOrgDetails`
