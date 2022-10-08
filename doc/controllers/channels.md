# Channels

```python
channels_controller = client.channels
```

## Class Name

`ChannelsController`

## Methods

* [Get All Channel Features](../../doc/controllers/channels.md#get-all-channel-features)
* [Get Channel Features](../../doc/controllers/channels.md#get-channel-features)
* [Get Channel Items](../../doc/controllers/channels.md#get-channel-items)
* [Get Channels](../../doc/controllers/channels.md#get-channels)
* [Get Latest Channel Items](../../doc/controllers/channels.md#get-latest-channel-items)


# Get All Channel Features

Get all channel features.

```python
def get_all_channel_features(self)
```

## Response Type

[`List of ChannelFeatures`](../../doc/models/channel-features.md)

## Example Usage

```python
result = channels_controller.get_all_channel_features()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Channel Features

Get channel features.

```python
def get_channel_features(self,
                        channel_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_id` | `uuid\|string` | Template, Required | Channel id. |

## Response Type

[`ChannelFeatures`](../../doc/models/channel-features.md)

## Example Usage

```python
channel_id = '00001a8a-0000-0000-0000-000000000000'

result = channels_controller.get_channel_features(channel_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Channel Items

Get channel items.

```python
def get_channel_items(self,
                     channel_id,
                     folder_id=None,
                     user_id=None,
                     start_index=None,
                     limit=None,
                     sort_order=None,
                     filters=None,
                     sort_by=None,
                     fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_id` | `uuid\|string` | Template, Required | Channel Id. |
| `folder_id` | `uuid\|string` | Query, Optional | Optional. Folder Id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. User Id. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `sort_order` | [`List of SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Optional. Sort Order - Ascending,Descending. |
| `filters` | [`List of ItemFilterEnum`](../../doc/models/item-filter-enum.md) | Query, Optional | Optional. Specify additional filters to apply. |
| `sort_by` | `List of string` | Query, Optional | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
channel_id = '00001a8a-0000-0000-0000-000000000000'

result = channels_controller.get_channel_items(channel_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Channels

Gets available channels.

```python
def get_channels(self,
                user_id=None,
                start_index=None,
                limit=None,
                supports_latest_items=None,
                supports_media_deletion=None,
                is_favorite=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | User Id to filter by. Use System.Guid.Empty to not filter by user. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `supports_latest_items` | `bool` | Query, Optional | Optional. Filter by channels that support getting latest items. |
| `supports_media_deletion` | `bool` | Query, Optional | Optional. Filter by channels that support media deletion. |
| `is_favorite` | `bool` | Query, Optional | Optional. Filter by channels that are favorite. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
result = channels_controller.get_channels()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Latest Channel Items

Gets latest channel items.

```python
def get_latest_channel_items(self,
                            user_id=None,
                            start_index=None,
                            limit=None,
                            filters=None,
                            fields=None,
                            channel_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | Optional. User Id. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `filters` | [`List of ItemFilterEnum`](../../doc/models/item-filter-enum.md) | Query, Optional | Optional. Specify additional filters to apply. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `channel_ids` | `List of uuid\|string` | Query, Optional | Optional. Specify one or more channel id's, comma delimited. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
result = channels_controller.get_latest_channel_items()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

