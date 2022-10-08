# Tv Shows

```python
tv_shows_controller = client.tv_shows
```

## Class Name

`TvShowsController`

## Methods

* [Get Episodes](../../doc/controllers/tv-shows.md#get-episodes)
* [Get Next Up](../../doc/controllers/tv-shows.md#get-next-up)
* [Get Seasons](../../doc/controllers/tv-shows.md#get-seasons)
* [Get Upcoming Episodes](../../doc/controllers/tv-shows.md#get-upcoming-episodes)


# Get Episodes

Gets episodes for a tv season.

```python
def get_episodes(self,
                series_id,
                user_id=None,
                fields=None,
                season=None,
                season_id=None,
                is_missing=None,
                adjacent_to=None,
                start_item_id=None,
                start_index=None,
                limit=None,
                enable_images=None,
                image_type_limit=None,
                enable_image_types=None,
                enable_user_data=None,
                sort_by=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `series_id` | `uuid\|string` | Template, Required | The series id. |
| `user_id` | `uuid\|string` | Query, Optional | The user id. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. |
| `season` | `int` | Query, Optional | Optional filter by season number. |
| `season_id` | `uuid\|string` | Query, Optional | Optional. Filter by season id. |
| `is_missing` | `bool` | Query, Optional | Optional. Filter by items that are missing episodes or not. |
| `adjacent_to` | `string` | Query, Optional | Optional. Return items that are siblings of a supplied item. |
| `start_item_id` | `uuid\|string` | Query, Optional | Optional. Skip through the list until a given item is found. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `enable_images` | `bool` | Query, Optional | Optional, include image information in output. |
| `image_type_limit` | `int` | Query, Optional | Optional, the max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `sort_by` | `string` | Query, Optional | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
series_id = '00001358-0000-0000-0000-000000000000'

result = tv_shows_controller.get_episodes(series_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Next Up

Gets a list of next up episodes.

```python
def get_next_up(self,
               user_id=None,
               start_index=None,
               limit=None,
               fields=None,
               series_id=None,
               parent_id=None,
               enable_images=None,
               image_type_limit=None,
               enable_image_types=None,
               enable_user_data=None,
               next_up_date_cutoff=None,
               enable_total_record_count=True,
               disable_first_episode=False,
               enable_rewatching=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | The user id of the user to get the next up episodes for. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `series_id` | `string` | Query, Optional | Optional. Filter by series id. |
| `parent_id` | `uuid\|string` | Query, Optional | Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `next_up_date_cutoff` | `datetime` | Query, Optional | Optional. Starting date of shows to show in Next Up section. |
| `enable_total_record_count` | `bool` | Query, Optional | Whether to enable the total records count. Defaults to true.<br>**Default**: `True` |
| `disable_first_episode` | `bool` | Query, Optional | Whether to disable sending the first episode in a series as next up.<br>**Default**: `False` |
| `enable_rewatching` | `bool` | Query, Optional | Whether to include watched episode in next up results.<br>**Default**: `False` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_total_record_count = True
disable_first_episode = False
enable_rewatching = False

result = tv_shows_controller.get_next_up(None, None, None, None, None, None, None, None, None, None, None, enable_total_record_count, disable_first_episode, enable_rewatching)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Seasons

Gets seasons for a tv series.

```python
def get_seasons(self,
               series_id,
               user_id=None,
               fields=None,
               is_special_season=None,
               is_missing=None,
               adjacent_to=None,
               enable_images=None,
               image_type_limit=None,
               enable_image_types=None,
               enable_user_data=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `series_id` | `uuid\|string` | Template, Required | The series id. |
| `user_id` | `uuid\|string` | Query, Optional | The user id. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. |
| `is_special_season` | `bool` | Query, Optional | Optional. Filter by special season. |
| `is_missing` | `bool` | Query, Optional | Optional. Filter by items that are missing episodes or not. |
| `adjacent_to` | `string` | Query, Optional | Optional. Return items that are siblings of a supplied item. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
series_id = '00001358-0000-0000-0000-000000000000'

result = tv_shows_controller.get_seasons(series_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Upcoming Episodes

Gets a list of upcoming episodes.

```python
def get_upcoming_episodes(self,
                         user_id=None,
                         start_index=None,
                         limit=None,
                         fields=None,
                         parent_id=None,
                         enable_images=None,
                         image_type_limit=None,
                         enable_image_types=None,
                         enable_user_data=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | The user id of the user to get the upcoming episodes for. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `parent_id` | `uuid\|string` | Query, Optional | Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
result = tv_shows_controller.get_upcoming_episodes()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

