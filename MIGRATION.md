## Migration Guide:

### Pixelbin SDK v3.x.x to v4.x.x

#### Breaking Changes

1. **Updated Function Signature in `security.py`**

    The arguments for `sign_url` function has been updated. The `token_id` parameter has been replaced with `access_key`.

    **Previous Method (v3.1.x and above):**

    ```python
    from pixelbin.utils.security import sign_url

    signed_url = sign_url(
        url="https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg",
        expiry_seconds=20,
        token_id=42,
        token="dummy-token",
    );
    ```

    **New Method (v4.x.x):**

    ```python
    from pixelbin.utils.security import sign_url

    signed_url = sign_url(
        url="https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg",
        expiry_seconds=20,
        access_key="6227274d-92c9-4b74-bef8-2528542516d8",
        token="dummy-token",
    );
    ```

    **How to Find Your Access Key:**

    - Go to `console.pixelbin.io`
    - Navigate to `Settings` > `Tokens`
    - Click on any Token
    - Find the `Access Key` in the token details
