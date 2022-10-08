# Live Tv

```python
live_tv_controller = client.live_tv
```

## Class Name

`LiveTvController`

## Methods

* [Add Listing Provider](../../doc/controllers/live-tv.md#add-listing-provider)
* [Add Tuner Host](../../doc/controllers/live-tv.md#add-tuner-host)
* [Cancel Series Timer](../../doc/controllers/live-tv.md#cancel-series-timer)
* [Cancel Timer](../../doc/controllers/live-tv.md#cancel-timer)
* [Create Series Timer](../../doc/controllers/live-tv.md#create-series-timer)
* [Create Timer](../../doc/controllers/live-tv.md#create-timer)
* [Delete Listing Provider](../../doc/controllers/live-tv.md#delete-listing-provider)
* [Delete Recording](../../doc/controllers/live-tv.md#delete-recording)
* [Delete Tuner Host](../../doc/controllers/live-tv.md#delete-tuner-host)
* [Discover Tuners](../../doc/controllers/live-tv.md#discover-tuners)
* [Discvover Tuners](../../doc/controllers/live-tv.md#discvover-tuners)
* [Get Channel](../../doc/controllers/live-tv.md#get-channel)
* [Get Channel Mapping Options](../../doc/controllers/live-tv.md#get-channel-mapping-options)
* [Get Default Listing Provider](../../doc/controllers/live-tv.md#get-default-listing-provider)
* [Get Default Timer](../../doc/controllers/live-tv.md#get-default-timer)
* [Get Guide Info](../../doc/controllers/live-tv.md#get-guide-info)
* [Get Lineups](../../doc/controllers/live-tv.md#get-lineups)
* [Get Live Recording File](../../doc/controllers/live-tv.md#get-live-recording-file)
* [Get Live Stream File](../../doc/controllers/live-tv.md#get-live-stream-file)
* [Get Live Tv Channels](../../doc/controllers/live-tv.md#get-live-tv-channels)
* [Get Live Tv Info](../../doc/controllers/live-tv.md#get-live-tv-info)
* [Get Live Tv Programs](../../doc/controllers/live-tv.md#get-live-tv-programs)
* [Get Program](../../doc/controllers/live-tv.md#get-program)
* [Get Programs](../../doc/controllers/live-tv.md#get-programs)
* [Get Recommended Programs](../../doc/controllers/live-tv.md#get-recommended-programs)
* [Get Recording](../../doc/controllers/live-tv.md#get-recording)
* [Get Recording Folders](../../doc/controllers/live-tv.md#get-recording-folders)
* [Get Recording Group](../../doc/controllers/live-tv.md#get-recording-group)
* [Get Recording Groups](../../doc/controllers/live-tv.md#get-recording-groups)
* [Get Recordings](../../doc/controllers/live-tv.md#get-recordings)
* [Get Recordings Series](../../doc/controllers/live-tv.md#get-recordings-series)
* [Get Schedules Direct Countries](../../doc/controllers/live-tv.md#get-schedules-direct-countries)
* [Get Series Timer](../../doc/controllers/live-tv.md#get-series-timer)
* [Get Series Timers](../../doc/controllers/live-tv.md#get-series-timers)
* [Get Timer](../../doc/controllers/live-tv.md#get-timer)
* [Get Timers](../../doc/controllers/live-tv.md#get-timers)
* [Get Tuner Host Types](../../doc/controllers/live-tv.md#get-tuner-host-types)
* [Reset Tuner](../../doc/controllers/live-tv.md#reset-tuner)
* [Set Channel Mapping](../../doc/controllers/live-tv.md#set-channel-mapping)
* [Update Series Timer](../../doc/controllers/live-tv.md#update-series-timer)
* [Update Timer](../../doc/controllers/live-tv.md#update-timer)


# Add Listing Provider

Adds a listings provider.

```python
def add_listing_provider(self,
                        pw=None,
                        validate_listings=False,
                        validate_login=False,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pw` | `string` | Query, Optional | Password. |
| `validate_listings` | `bool` | Query, Optional | Validate listings.<br>**Default**: `False` |
| `validate_login` | `bool` | Query, Optional | Validate login.<br>**Default**: `False` |
| `body` | [`ListingsProviderInfo`](../../doc/models/listings-provider-info.md) | Body, Optional | New listings info. |

## Response Type

[`ListingsProviderInfo`](../../doc/models/listings-provider-info.md)

## Example Usage

```python
validate_listings = False
validate_login = False

result = live_tv_controller.add_listing_provider(None, validate_listings, validate_login)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Add Tuner Host

Adds a tuner host.

```python
def add_tuner_host(self,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TunerHostInfo`](../../doc/models/tuner-host-info.md) | Body, Optional | New tuner host. |

## Response Type

[`TunerHostInfo`](../../doc/models/tuner-host-info.md)

## Example Usage

```python
result = live_tv_controller.add_tuner_host()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Cancel Series Timer

Cancels a live tv series timer.

```python
def cancel_series_timer(self,
                       timer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timer_id` | `string` | Template, Required | Timer id. |

## Response Type

`void`

## Example Usage

```python
timer_id = 'timerId0'

result = live_tv_controller.cancel_series_timer(timer_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Cancel Timer

Cancels a live tv timer.

```python
def cancel_timer(self,
                timer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timer_id` | `string` | Template, Required | Timer id. |

## Response Type

`void`

## Example Usage

```python
timer_id = 'timerId0'

result = live_tv_controller.cancel_timer(timer_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Create Series Timer

Creates a live tv series timer.

```python
def create_series_timer(self,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SeriesTimerInfoDto`](../../doc/models/series-timer-info-dto.md) | Body, Optional | New series timer info. |

## Response Type

`void`

## Example Usage

```python
result = live_tv_controller.create_series_timer()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Create Timer

Creates a live tv timer.

```python
def create_timer(self,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TimerInfoDto`](../../doc/models/timer-info-dto.md) | Body, Optional | New timer info. |

## Response Type

`void`

## Example Usage

```python
result = live_tv_controller.create_timer()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Delete Listing Provider

Delete listing provider.

```python
def delete_listing_provider(self,
                           id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Query, Optional | Listing provider id. |

## Response Type

`void`

## Example Usage

```python
result = live_tv_controller.delete_listing_provider()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Delete Recording

Deletes a live tv recording.

```python
def delete_recording(self,
                    recording_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recording_id` | `uuid\|string` | Template, Required | Recording id. |

## Response Type

`void`

## Example Usage

```python
recording_id = '000015e2-0000-0000-0000-000000000000'

result = live_tv_controller.delete_recording(recording_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Delete Tuner Host

Deletes a tuner host.

```python
def delete_tuner_host(self,
                     id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Query, Optional | Tuner host id. |

## Response Type

`void`

## Example Usage

```python
result = live_tv_controller.delete_tuner_host()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Discover Tuners

Discover tuners.

```python
def discover_tuners(self,
                   new_devices_only=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_devices_only` | `bool` | Query, Optional | Only discover new tuners.<br>**Default**: `False` |

## Response Type

[`List of TunerHostInfo`](../../doc/models/tuner-host-info.md)

## Example Usage

```python
new_devices_only = False

result = live_tv_controller.discover_tuners(new_devices_only)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Discvover Tuners

Discover tuners.

```python
def discvover_tuners(self,
                    new_devices_only=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_devices_only` | `bool` | Query, Optional | Only discover new tuners.<br>**Default**: `False` |

## Response Type

[`List of TunerHostInfo`](../../doc/models/tuner-host-info.md)

## Example Usage

```python
new_devices_only = False

result = live_tv_controller.discvover_tuners(new_devices_only)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Channel

Gets a live tv channel.

```python
def get_channel(self,
               channel_id,
               user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_id` | `uuid\|string` | Template, Required | Channel id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Attach user data. |

## Response Type

[`BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
channel_id = '00001a8a-0000-0000-0000-000000000000'

result = live_tv_controller.get_channel(channel_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Channel Mapping Options

Get channel mapping options.

```python
def get_channel_mapping_options(self,
                               provider_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `provider_id` | `string` | Query, Optional | Provider id. |

## Response Type

[`ChannelMappingOptionsDto`](../../doc/models/channel-mapping-options-dto.md)

## Example Usage

```python
result = live_tv_controller.get_channel_mapping_options()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Default Listing Provider

Gets default listings provider info.

```python
def get_default_listing_provider(self)
```

## Response Type

[`ListingsProviderInfo`](../../doc/models/listings-provider-info.md)

## Example Usage

```python
result = live_tv_controller.get_default_listing_provider()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Default Timer

Gets the default values for a new timer.

```python
def get_default_timer(self,
                     program_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `program_id` | `string` | Query, Optional | Optional. To attach default values based on a program. |

## Response Type

[`SeriesTimerInfoDto`](../../doc/models/series-timer-info-dto.md)

## Example Usage

```python
result = live_tv_controller.get_default_timer()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Guide Info

Get guid info.

```python
def get_guide_info(self)
```

## Response Type

[`GuideInfo`](../../doc/models/guide-info.md)

## Example Usage

```python
result = live_tv_controller.get_guide_info()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Lineups

Gets available lineups.

```python
def get_lineups(self,
               id=None,
               mtype=None,
               location=None,
               country=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Query, Optional | Provider id. |
| `mtype` | `string` | Query, Optional | Provider type. |
| `location` | `string` | Query, Optional | Location. |
| `country` | `string` | Query, Optional | Country. |

## Response Type

[`List of NameIdPair`](../../doc/models/name-id-pair.md)

## Example Usage

```python
result = live_tv_controller.get_lineups()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Live Recording File

Gets a live tv recording stream.

```python
def get_live_recording_file(self,
                           recording_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recording_id` | `string` | Template, Required | Recording id. |

## Response Type

`mixed`

## Example Usage

```python
recording_id = 'recordingId2'

result = live_tv_controller.get_live_recording_file(recording_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Recording not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Live Stream File

Gets a live tv channel stream.

```python
def get_live_stream_file(self,
                        stream_id,
                        container)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stream_id` | `string` | Template, Required | Stream id. |
| `container` | `string` | Template, Required | Container type. |

## Response Type

`mixed`

## Example Usage

```python
stream_id = 'streamId4'
container = 'container2'

result = live_tv_controller.get_live_stream_file(stream_id, container)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Stream not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Live Tv Channels

Gets available live tv channels.

```python
def get_live_tv_channels(self,
                        mtype=None,
                        user_id=None,
                        start_index=None,
                        is_movie=None,
                        is_series=None,
                        is_news=None,
                        is_kids=None,
                        is_sports=None,
                        limit=None,
                        is_favorite=None,
                        is_liked=None,
                        is_disliked=None,
                        enable_images=None,
                        image_type_limit=None,
                        enable_image_types=None,
                        fields=None,
                        enable_user_data=None,
                        sort_by=None,
                        sort_order=None,
                        enable_favorite_sorting=False,
                        add_current_program=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`ChannelTypeEnum`](../../doc/models/channel-type-enum.md) | Query, Optional | Optional. Filter by channel type. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user and attach user data. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `is_movie` | `bool` | Query, Optional | Optional. Filter for movies. |
| `is_series` | `bool` | Query, Optional | Optional. Filter for series. |
| `is_news` | `bool` | Query, Optional | Optional. Filter for news. |
| `is_kids` | `bool` | Query, Optional | Optional. Filter for kids. |
| `is_sports` | `bool` | Query, Optional | Optional. Filter for sports. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `is_favorite` | `bool` | Query, Optional | Optional. Filter by channels that are favorites, or not. |
| `is_liked` | `bool` | Query, Optional | Optional. Filter by channels that are liked, or not. |
| `is_disliked` | `bool` | Query, Optional | Optional. Filter by channels that are disliked, or not. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | "Optional. The image types to include in the output. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `sort_by` | `List of string` | Query, Optional | Optional. Key to sort by. |
| `sort_order` | [`SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Optional. Sort order. |
| `enable_favorite_sorting` | `bool` | Query, Optional | Optional. Incorporate favorite and like status into channel sorting.<br>**Default**: `False` |
| `add_current_program` | `bool` | Query, Optional | Optional. Adds current program info to each channel.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_favorite_sorting = False
add_current_program = True

result = live_tv_controller.get_live_tv_channels(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_favorite_sorting, add_current_program)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Live Tv Info

Gets available live tv services.

```python
def get_live_tv_info(self)
```

## Response Type

[`LiveTvInfo`](../../doc/models/live-tv-info.md)

## Example Usage

```python
result = live_tv_controller.get_live_tv_info()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Live Tv Programs

Gets available live tv epgs.

```python
def get_live_tv_programs(self,
                        channel_ids=None,
                        user_id=None,
                        min_start_date=None,
                        has_aired=None,
                        is_airing=None,
                        max_start_date=None,
                        min_end_date=None,
                        max_end_date=None,
                        is_movie=None,
                        is_series=None,
                        is_news=None,
                        is_kids=None,
                        is_sports=None,
                        start_index=None,
                        limit=None,
                        sort_by=None,
                        sort_order=None,
                        genres=None,
                        genre_ids=None,
                        enable_images=None,
                        image_type_limit=None,
                        enable_image_types=None,
                        enable_user_data=None,
                        series_timer_id=None,
                        library_series_id=None,
                        fields=None,
                        enable_total_record_count=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_ids` | `List of uuid\|string` | Query, Optional | The channels to return guide information for. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id. |
| `min_start_date` | `datetime` | Query, Optional | Optional. The minimum premiere start date. |
| `has_aired` | `bool` | Query, Optional | Optional. Filter by programs that have completed airing, or not. |
| `is_airing` | `bool` | Query, Optional | Optional. Filter by programs that are currently airing, or not. |
| `max_start_date` | `datetime` | Query, Optional | Optional. The maximum premiere start date. |
| `min_end_date` | `datetime` | Query, Optional | Optional. The minimum premiere end date. |
| `max_end_date` | `datetime` | Query, Optional | Optional. The maximum premiere end date. |
| `is_movie` | `bool` | Query, Optional | Optional. Filter for movies. |
| `is_series` | `bool` | Query, Optional | Optional. Filter for series. |
| `is_news` | `bool` | Query, Optional | Optional. Filter for news. |
| `is_kids` | `bool` | Query, Optional | Optional. Filter for kids. |
| `is_sports` | `bool` | Query, Optional | Optional. Filter for sports. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `sort_by` | `List of string` | Query, Optional | Optional. Specify one or more sort orders, comma delimited. Options: Name, StartDate. |
| `sort_order` | [`List of SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Sort Order - Ascending,Descending. |
| `genres` | `List of string` | Query, Optional | The genres to return guide information for. |
| `genre_ids` | `List of uuid\|string` | Query, Optional | The genre ids to return guide information for. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `series_timer_id` | `string` | Query, Optional | Optional. Filter by series timer id. |
| `library_series_id` | `uuid\|string` | Query, Optional | Optional. Filter by library series id. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_total_record_count` | `bool` | Query, Optional | Retrieve total record count.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_total_record_count = True

result = live_tv_controller.get_live_tv_programs(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_total_record_count)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Program

Gets a live tv program.

```python
def get_program(self,
               program_id,
               user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `program_id` | `string` | Template, Required | Program id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Attach user data. |

## Response Type

[`BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
program_id = 'programId8'

result = live_tv_controller.get_program(program_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Programs

Gets available live tv epgs.

```python
def get_programs(self,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetProgramsDto`](../../doc/models/get-programs-dto.md) | Body, Optional | Request body. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
result = live_tv_controller.get_programs()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Recommended Programs

Gets recommended live tv epgs.

```python
def get_recommended_programs(self,
                            user_id=None,
                            limit=None,
                            is_airing=None,
                            has_aired=None,
                            is_series=None,
                            is_movie=None,
                            is_news=None,
                            is_kids=None,
                            is_sports=None,
                            enable_images=None,
                            image_type_limit=None,
                            enable_image_types=None,
                            genre_ids=None,
                            fields=None,
                            enable_user_data=None,
                            enable_total_record_count=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | Optional. filter by user id. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `is_airing` | `bool` | Query, Optional | Optional. Filter by programs that are currently airing, or not. |
| `has_aired` | `bool` | Query, Optional | Optional. Filter by programs that have completed airing, or not. |
| `is_series` | `bool` | Query, Optional | Optional. Filter for series. |
| `is_movie` | `bool` | Query, Optional | Optional. Filter for movies. |
| `is_news` | `bool` | Query, Optional | Optional. Filter for news. |
| `is_kids` | `bool` | Query, Optional | Optional. Filter for kids. |
| `is_sports` | `bool` | Query, Optional | Optional. Filter for sports. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `genre_ids` | `List of uuid\|string` | Query, Optional | The genres to return guide information for. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. include user data. |
| `enable_total_record_count` | `bool` | Query, Optional | Retrieve total record count.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_total_record_count = True

result = live_tv_controller.get_recommended_programs(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_total_record_count)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Recording

Gets a live tv recording.

```python
def get_recording(self,
                 recording_id,
                 user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recording_id` | `uuid\|string` | Template, Required | Recording id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Attach user data. |

## Response Type

[`BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
recording_id = '000015e2-0000-0000-0000-000000000000'

result = live_tv_controller.get_recording(recording_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Recording Folders

Gets recording folders.

```python
def get_recording_folders(self,
                         user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user and attach user data. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
result = live_tv_controller.get_recording_folders()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Recording Group

**This endpoint is deprecated.**

Get recording group.

```python
def get_recording_group(self,
                       group_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group_id` | `uuid\|string` | Template, Required | Group id. |

## Response Type

`void`

## Example Usage

```python
group_id = '00002262-0000-0000-0000-000000000000'

result = live_tv_controller.get_recording_group(group_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Recording Groups

**This endpoint is deprecated.**

Gets live tv recording groups.

```python
def get_recording_groups(self,
                        user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user and attach user data. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
result = live_tv_controller.get_recording_groups()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Recordings

Gets live tv recordings.

```python
def get_recordings(self,
                  channel_id=None,
                  user_id=None,
                  start_index=None,
                  limit=None,
                  status=None,
                  is_in_progress=None,
                  series_timer_id=None,
                  enable_images=None,
                  image_type_limit=None,
                  enable_image_types=None,
                  fields=None,
                  enable_user_data=None,
                  is_movie=None,
                  is_series=None,
                  is_kids=None,
                  is_sports=None,
                  is_news=None,
                  is_library_item=None,
                  enable_total_record_count=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_id` | `string` | Query, Optional | Optional. Filter by channel id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user and attach user data. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `status` | [`RecordingStatusEnum`](../../doc/models/recording-status-enum.md) | Query, Optional | Optional. Filter by recording status. |
| `is_in_progress` | `bool` | Query, Optional | Optional. Filter by recordings that are in progress, or not. |
| `series_timer_id` | `string` | Query, Optional | Optional. Filter by recordings belonging to a series timer. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `is_movie` | `bool` | Query, Optional | Optional. Filter for movies. |
| `is_series` | `bool` | Query, Optional | Optional. Filter for series. |
| `is_kids` | `bool` | Query, Optional | Optional. Filter for kids. |
| `is_sports` | `bool` | Query, Optional | Optional. Filter for sports. |
| `is_news` | `bool` | Query, Optional | Optional. Filter for news. |
| `is_library_item` | `bool` | Query, Optional | Optional. Filter for is library item. |
| `enable_total_record_count` | `bool` | Query, Optional | Optional. Return total record count.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_total_record_count = True

result = live_tv_controller.get_recordings(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_total_record_count)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Recordings Series

**This endpoint is deprecated.**

Gets live tv recording series.

```python
def get_recordings_series(self,
                         channel_id=None,
                         user_id=None,
                         group_id=None,
                         start_index=None,
                         limit=None,
                         status=None,
                         is_in_progress=None,
                         series_timer_id=None,
                         enable_images=None,
                         image_type_limit=None,
                         enable_image_types=None,
                         fields=None,
                         enable_user_data=None,
                         enable_total_record_count=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_id` | `string` | Query, Optional | Optional. Filter by channel id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user and attach user data. |
| `group_id` | `string` | Query, Optional | Optional. Filter by recording group. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `status` | [`RecordingStatusEnum`](../../doc/models/recording-status-enum.md) | Query, Optional | Optional. Filter by recording status. |
| `is_in_progress` | `bool` | Query, Optional | Optional. Filter by recordings that are in progress, or not. |
| `series_timer_id` | `string` | Query, Optional | Optional. Filter by recordings belonging to a series timer. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `enable_total_record_count` | `bool` | Query, Optional | Optional. Return total record count.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_total_record_count = True

result = live_tv_controller.get_recordings_series(None, None, None, None, None, None, None, None, None, None, None, None, None, enable_total_record_count)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Schedules Direct Countries

Gets available countries.

```python
def get_schedules_direct_countries(self)
```

## Response Type

`binary`

## Example Usage

```python
result = live_tv_controller.get_schedules_direct_countries()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Series Timer

Gets a live tv series timer.

```python
def get_series_timer(self,
                    timer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timer_id` | `string` | Template, Required | Timer id. |

## Response Type

[`SeriesTimerInfoDto`](../../doc/models/series-timer-info-dto.md)

## Example Usage

```python
timer_id = 'timerId0'

result = live_tv_controller.get_series_timer(timer_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Series timer not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Series Timers

Gets live tv series timers.

```python
def get_series_timers(self,
                     sort_by=None,
                     sort_order=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sort_by` | `string` | Query, Optional | Optional. Sort by SortName or Priority. |
| `sort_order` | [`SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Optional. Sort in Ascending or Descending order. |

## Response Type

[`SeriesTimerInfoDtoQueryResult`](../../doc/models/series-timer-info-dto-query-result.md)

## Example Usage

```python
result = live_tv_controller.get_series_timers()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Timer

Gets a timer.

```python
def get_timer(self,
             timer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timer_id` | `string` | Template, Required | Timer id. |

## Response Type

[`TimerInfoDto`](../../doc/models/timer-info-dto.md)

## Example Usage

```python
timer_id = 'timerId0'

result = live_tv_controller.get_timer(timer_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Timers

Gets the live tv timers.

```python
def get_timers(self,
              channel_id=None,
              series_timer_id=None,
              is_active=None,
              is_scheduled=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_id` | `string` | Query, Optional | Optional. Filter by channel id. |
| `series_timer_id` | `string` | Query, Optional | Optional. Filter by timers belonging to a series timer. |
| `is_active` | `bool` | Query, Optional | Optional. Filter by timers that are active. |
| `is_scheduled` | `bool` | Query, Optional | Optional. Filter by timers that are scheduled. |

## Response Type

[`TimerInfoDtoQueryResult`](../../doc/models/timer-info-dto-query-result.md)

## Example Usage

```python
result = live_tv_controller.get_timers()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Tuner Host Types

Get tuner host types.

```python
def get_tuner_host_types(self)
```

## Response Type

[`List of NameIdPair`](../../doc/models/name-id-pair.md)

## Example Usage

```python
result = live_tv_controller.get_tuner_host_types()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Reset Tuner

Resets a tv tuner.

```python
def reset_tuner(self,
               tuner_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tuner_id` | `string` | Template, Required | Tuner id. |

## Response Type

`void`

## Example Usage

```python
tuner_id = 'tunerId2'

result = live_tv_controller.reset_tuner(tuner_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Set Channel Mapping

Set channel mappings.

```python
def set_channel_mapping(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SetChannelMappingDto`](../../doc/models/set-channel-mapping-dto.md) | Body, Required | The set channel mapping dto. |

## Response Type

[`TunerChannelMapping`](../../doc/models/tuner-channel-mapping.md)

## Example Usage

```python
body = SetChannelMappingDto()
body.provider_id = 'ProviderId8'
body.tuner_channel_id = 'TunerChannelId8'
body.provider_channel_id = 'ProviderChannelId6'

result = live_tv_controller.set_channel_mapping(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Series Timer

Updates a live tv series timer.

```python
def update_series_timer(self,
                       timer_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timer_id` | `string` | Template, Required | Timer id. |
| `body` | [`SeriesTimerInfoDto`](../../doc/models/series-timer-info-dto.md) | Body, Optional | New series timer info. |

## Response Type

`void`

## Example Usage

```python
timer_id = 'timerId0'

result = live_tv_controller.update_series_timer(timer_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Timer

Updates a live tv timer.

```python
def update_timer(self,
                timer_id,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timer_id` | `string` | Template, Required | Timer id. |
| `body` | [`TimerInfoDto`](../../doc/models/timer-info-dto.md) | Body, Optional | New timer info. |

## Response Type

`void`

## Example Usage

```python
timer_id = 'timerId0'

result = live_tv_controller.update_timer(timer_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

