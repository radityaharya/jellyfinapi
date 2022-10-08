# Item Refresh

```python
item_refresh_controller = client.item_refresh
```

## Class Name

`ItemRefreshController`


# Refresh Item

Refreshes metadata for an item.

```python
def refresh_item(self,
                item_id,
                metadata_refresh_mode='None',
                image_refresh_mode='None',
                replace_all_metadata=False,
                replace_all_images=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `metadata_refresh_mode` | [`MetadataRefreshModeEnum`](../../doc/models/metadata-refresh-mode-enum.md) | Query, Optional | (Optional) Specifies the metadata refresh mode.<br>**Default**: `'None'` |
| `image_refresh_mode` | [`MetadataRefreshModeEnum`](../../doc/models/metadata-refresh-mode-enum.md) | Query, Optional | (Optional) Specifies the image refresh mode.<br>**Default**: `'None'` |
| `replace_all_metadata` | `bool` | Query, Optional | (Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh.<br>**Default**: `False` |
| `replace_all_images` | `bool` | Query, Optional | (Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh.<br>**Default**: `False` |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
metadata_refresh_mode = MetadataRefreshModeEnum.ENUM_NONE
image_refresh_mode = MetadataRefreshModeEnum.ENUM_NONE
replace_all_metadata = False
replace_all_images = False

result = item_refresh_controller.refresh_item(item_id, metadata_refresh_mode, image_refresh_mode, replace_all_metadata, replace_all_images)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item to refresh not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

