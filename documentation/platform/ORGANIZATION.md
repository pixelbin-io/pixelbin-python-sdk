##### [Back to Pixelbin API docs](./README.md)

## Organization Methods

Organization Service

-   [getAppByToken](#getappbytoken)

## Methods with example and description

### getAppByToken

**Summary**: Get App Details

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.organization.getAppByToken(
        token="<API-TOKEN>")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.organization.getAppByTokenAsync(
        token="<API-TOKEN>"))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type | Required | Description        |
| -------- | ---- | -------- | ------------------ |
| token    | str  | yes      | Pixelbin api token |

Get App and org details with the API_TOKEN

_Returned Response:_

[AppDetailsByToken](#appdetailsbytoken)

Success. Returns a JSON object as shown below. Refer `AppDetailsByToken` for more details.

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "app": {
        "_id": 123,
        "orgId": 12,
        "name": "Desktop Client App",
        "permissions": ["read", "read_write"],
        "active": false,
        "createdAt": "2021-07-15T07:47:00Z",
        "updatedAt": "2021-07-15T07:47:00Z"
    },
    "org": {
        "_id": 12,
        "name": "org_1",
        "cloudName": "testcloudname",
        "accountType": "individual",
        "industry": "Ecommerce",
        "strength": "1",
        "active": "false"
    }
}
```

</details>

### Schemas

#### OrganizationDetailSchema

| Properties | Type | Nullable | Description                                        |
| ---------- | ---- | -------- | -------------------------------------------------- |
| \_id       | int  | no       | Id of the organization                             |
| name       | str  | no       | Organization Name                                  |
| cloudName  | str  | no       | Unique cloud name associated with the organization |
| ownerId    | str  | no       | User Id of the organization owner                  |
| active     | bool | no       | Whether the organization is active                 |
| createdAt  | str  | no       | Timestamp when the organization was created        |
| updatedAt  | str  | no       | Timestamp when the organization was last updated   |

#### AppSchema

| Properties  | Type      | Nullable | Description                             |
| ----------- | --------- | -------- | --------------------------------------- |
| \_id        | int       | no       | App id                                  |
| orgId       | int       | no       | Organization id the app belongs to      |
| name        | str       | no       | Name of the app                         |
| token       | str       | no       | api token for the app                   |
| permissions | List[str] | no       | Permissions applied on the app          |
| active      | bool      | no       | Whether the app is active               |
| createdAt   | str       | no       | Timestamp when the app was created      |
| updatedAt   | str       | no       | Timestamp when the app was last updated |

#### AppDetailsByToken

| Properties | Type                     | Nullable | Description |
| ---------- | ------------------------ | -------- | ----------- |
| app        | AppSchema                | no       |             |
| org        | OrganizationDetailSchema | no       |             |

#### ErrorSchema

| Properties | Type | Nullable | Description |
| ---------- | ---- | -------- | ----------- |
| message    | str  | no       |             |
