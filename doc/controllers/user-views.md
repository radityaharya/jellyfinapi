# User Views

```python
user_views_controller = client.user_views
```

## Class Name

`UserViewsController`

## Methods

* [Get Grouping Options](../../doc/controllers/user-views.md#get-grouping-options)
* [Get User Views](../../doc/controllers/user-views.md#get-user-views)


# Get Grouping Options

Get user view grouping options.

```python
def get_grouping_options(self,
                        user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |

## Response Type

[`List of SpecialViewOptionDto`](../../doc/models/special-view-option-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'

result = user_views_controller.get_grouping_options(user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | User not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get User Views

Get user views.

```python
def get_user_views(self,
                  user_id,
                  include_external_content=None,
                  preset_views=None,
                  include_hidden=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `include_external_content` | `bool` | Query, Optional | Whether or not to include external views such as channels or live tv. |
| `preset_views` | `List of string` | Query, Optional | Preset views. |
| `include_hidden` | `bool` | Query, Optional | Whether or not to include hidden content.<br>**Default**: `False` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
include_hidden = False

result = user_views_controller.get_user_views(user_id, None, None, include_hidden)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

