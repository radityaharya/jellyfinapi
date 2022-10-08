# User Library

```python
user_library_controller = client.user_library
```

## Class Name

`UserLibraryController`

## Methods

* [Delete User Item Rating](../../doc/controllers/user-library.md#delete-user-item-rating)
* [Get Intros](../../doc/controllers/user-library.md#get-intros)
* [Get Item](../../doc/controllers/user-library.md#get-item)
* [Get Latest Media](../../doc/controllers/user-library.md#get-latest-media)
* [Get Local Trailers](../../doc/controllers/user-library.md#get-local-trailers)
* [Get Root Folder](../../doc/controllers/user-library.md#get-root-folder)
* [Get Special Features](../../doc/controllers/user-library.md#get-special-features)
* [Mark Favorite Item](../../doc/controllers/user-library.md#mark-favorite-item)
* [Unmark Favorite Item](../../doc/controllers/user-library.md#unmark-favorite-item)
* [Update User Item Rating](../../doc/controllers/user-library.md#update-user-item-rating)


# Delete User Item Rating

Deletes a user's saved personal rating for an item.

```python
def delete_user_item_rating(self,
                           user_id,
                           item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |

## Response Type

[`UserItemDataDto`](../../doc/models/user-item-data-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = user_library_controller.delete_user_item_rating(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Intros

Gets intros to play before the main media item plays.

```python
def get_intros(self,
              user_id,
              item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = user_library_controller.get_intros(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Item

Gets an item from a user's library.

```python
def get_item(self,
            user_id,
            item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |

## Response Type

[`BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = user_library_controller.get_item(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Latest Media

Gets latest media.

```python
def get_latest_media(self,
                    user_id,
                    parent_id=None,
                    fields=None,
                    include_item_types=None,
                    is_played=None,
                    enable_images=None,
                    image_type_limit=None,
                    enable_image_types=None,
                    enable_user_data=None,
                    limit=20,
                    group_items=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `parent_id` | `uuid\|string` | Query, Optional | Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `include_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. |
| `is_played` | `bool` | Query, Optional | Filter by items that are played, or not. |
| `enable_images` | `bool` | Query, Optional | Optional. include image information in output. |
| `image_type_limit` | `int` | Query, Optional | Optional. the max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. include user data. |
| `limit` | `int` | Query, Optional | Return item limit.<br>**Default**: `20` |
| `group_items` | `bool` | Query, Optional | Whether or not to group items into a parent container.<br>**Default**: `True` |

## Response Type

[`List of BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
limit = 20
group_items = True

result = user_library_controller.get_latest_media(user_id, None, None, None, None, None, None, None, None, limit, group_items)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Local Trailers

Gets local trailers for an item.

```python
def get_local_trailers(self,
                      user_id,
                      item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |

## Response Type

[`List of BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = user_library_controller.get_local_trailers(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Root Folder

Gets the root folder from a user's library.

```python
def get_root_folder(self,
                   user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |

## Response Type

[`BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'

result = user_library_controller.get_root_folder(user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Special Features

Gets special features for an item.

```python
def get_special_features(self,
                        user_id,
                        item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |

## Response Type

[`List of BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = user_library_controller.get_special_features(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Mark Favorite Item

Marks an item as a favorite.

```python
def mark_favorite_item(self,
                      user_id,
                      item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |

## Response Type

[`UserItemDataDto`](../../doc/models/user-item-data-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = user_library_controller.mark_favorite_item(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Unmark Favorite Item

Unmarks item as a favorite.

```python
def unmark_favorite_item(self,
                        user_id,
                        item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |

## Response Type

[`UserItemDataDto`](../../doc/models/user-item-data-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = user_library_controller.unmark_favorite_item(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update User Item Rating

Updates a user's rating for an item.

```python
def update_user_item_rating(self,
                           user_id,
                           item_id,
                           likes=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `likes` | `bool` | Query, Optional | Whether this M:Jellyfin.Api.Controllers.UserLibraryController.UpdateUserItemRating(System.Guid,System.Guid,System.Nullable{System.Boolean}) is likes. |

## Response Type

[`UserItemDataDto`](../../doc/models/user-item-data-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = user_library_controller.update_user_item_rating(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

