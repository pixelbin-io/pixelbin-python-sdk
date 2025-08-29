import os
from pixelbin import PixelbinClient, PixelbinConfig


def main():
    # Minimal setup via environment variables
    api_token = os.getenv("PIXELBIN_API_TOKEN") or "API_TOKEN"
    domain = os.getenv("PIXELBIN_DOMAIN") or "https://api.pixelbin.io"
    image_path = os.getenv("PREDICT_IMAGE_PATH") or "result.jpeg"
    webhook = os.getenv("PREDICT_WEBHOOK")  # optional
    name = os.getenv("PREDICT_NAME") or "erase_bg"

    if not api_token or api_token == "API_TOKEN":
        print(
            "Please set PIXELBIN_API_TOKEN or replace API_TOKEN in sample.predictions.py"
        )
        return

    client = PixelbinClient(
        config=PixelbinConfig(
            {
                "domain": domain,
                "apiSecret": api_token,
            }
        )
    )

    try:
        print("\n=== list predictions ===")
        items = client.predictions.list()
        print("total:", len(items) if isinstance(items, list) else 0)

        print("\n=== get schema ===")
        schema = client.predictions.get_schema(name)
        print("schema name:", schema.get("name") if isinstance(schema, dict) else None)

        print("\n=== create ===")
        img_bytes = None
        try:
            with open(image_path, "rb") as f:
                img_bytes = f.read()
        except Exception:
            pass

        job = client.predictions.create(
            name=name,
            input={
                **({"image": img_bytes} if img_bytes else {}),
                "industry_type": os.getenv("PREDICT_INDUSTRY_TYPE") or "general",
                "quality_type": os.getenv("PREDICT_QUALITY_TYPE") or "original",
                "shadow": os.getenv("PREDICT_SHADOW") or "false",
                "refine": os.getenv("PREDICT_REFINE") or "true",
            },
            webhook=webhook,
        )
        print("created job:", job)

        print("\n=== get (by id) ===")
        details = client.predictions.get(job["_id"])  # string only
        print("get by id:", details.get("status"))

        print("\n=== wait ===")
        final_status = client.predictions.wait(
            job["_id"], {"maxAttempts": 30, "retryFactor": 1, "retryInterval": 1.0}
        )
        print("wait ->", final_status.get("status"))

        print("\n=== outputs ===")
        print(final_status.get("output"))

        print("\n=== create_and_wait ===")
        final_result = client.predictions.create_and_wait(
            name=name,
            input={
                **({"image": img_bytes} if img_bytes else {}),
                "industry_type": os.getenv("PREDICT_INDUSTRY_TYPE") or "general",
                "quality_type": os.getenv("PREDICT_QUALITY_TYPE") or "original",
                "shadow": os.getenv("PREDICT_SHADOW") or "false",
                "refine": os.getenv("PREDICT_REFINE") or "true",
            },
            webhook=webhook,
            options={"maxAttempts": 60, "retryFactor": 1, "retryInterval": 2.0},
        )
        print("create_and_wait ->", final_result.get("status"))

        print("\nDone.")
    except Exception as err:
        print("Error:", getattr(err, "message", str(err)))


if __name__ == "__main__":
    main()
