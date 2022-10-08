# Item Lookup

```python
item_lookup_controller = client.item_lookup
```

## Class Name

`ItemLookupController`

## Methods

* [Apply Search Criteria](../../doc/controllers/item-lookup.md#apply-search-criteria)
* [Get Book Remote Search Results](../../doc/controllers/item-lookup.md#get-book-remote-search-results)
* [Get Box Set Remote Search Results](../../doc/controllers/item-lookup.md#get-box-set-remote-search-results)
* [Get External Id Infos](../../doc/controllers/item-lookup.md#get-external-id-infos)
* [Get Movie Remote Search Results](../../doc/controllers/item-lookup.md#get-movie-remote-search-results)
* [Get Music Album Remote Search Results](../../doc/controllers/item-lookup.md#get-music-album-remote-search-results)
* [Get Music Artist Remote Search Results](../../doc/controllers/item-lookup.md#get-music-artist-remote-search-results)
* [Get Music Video Remote Search Results](../../doc/controllers/item-lookup.md#get-music-video-remote-search-results)
* [Get Person Remote Search Results](../../doc/controllers/item-lookup.md#get-person-remote-search-results)
* [Get Series Remote Search Results](../../doc/controllers/item-lookup.md#get-series-remote-search-results)
* [Get Trailer Remote Search Results](../../doc/controllers/item-lookup.md#get-trailer-remote-search-results)


# Apply Search Criteria

Applies search criteria to an item and refreshes metadata.

```python
def apply_search_criteria(self,
                         item_id,
                         body,
                         replace_all_images=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `body` | [`RemoteSearchResult`](../../doc/models/remote-search-result.md) | Body, Required | The remote search result. |
| `replace_all_images` | `bool` | Query, Optional | Optional. Whether or not to replace all images. Default: True.<br>**Default**: `True` |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
body = RemoteSearchResult()
replace_all_images = True

result = item_lookup_controller.apply_search_criteria(item_id, body, replace_all_images)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Book Remote Search Results

Get book remote search.

```python
def get_book_remote_search_results(self,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BookInfoRemoteSearchQuery`](../../doc/models/book-info-remote-search-query.md) | Body, Required | Remote search query. |

## Response Type

[`List of RemoteSearchResult`](../../doc/models/remote-search-result.md)

## Example Usage

```python
body = BookInfoRemoteSearchQuery()

result = item_lookup_controller.get_book_remote_search_results(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Box Set Remote Search Results

Get box set remote search.

```python
def get_box_set_remote_search_results(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BoxSetInfoRemoteSearchQuery`](../../doc/models/box-set-info-remote-search-query.md) | Body, Required | Remote search query. |

## Response Type

[`List of RemoteSearchResult`](../../doc/models/remote-search-result.md)

## Example Usage

```python
body = BoxSetInfoRemoteSearchQuery()

result = item_lookup_controller.get_box_set_remote_search_results(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get External Id Infos

Get the item's external id info.

```python
def get_external_id_infos(self,
                         item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |

## Response Type

[`List of ExternalIdInfo`](../../doc/models/external-id-info.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = item_lookup_controller.get_external_id_infos(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Movie Remote Search Results

Get movie remote search.

```python
def get_movie_remote_search_results(self,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MovieInfoRemoteSearchQuery`](../../doc/models/movie-info-remote-search-query.md) | Body, Required | Remote search query. |

## Response Type

[`List of RemoteSearchResult`](../../doc/models/remote-search-result.md)

## Example Usage

```python
body = MovieInfoRemoteSearchQuery()

result = item_lookup_controller.get_movie_remote_search_results(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Music Album Remote Search Results

Get music album remote search.

```python
def get_music_album_remote_search_results(self,
                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlbumInfoRemoteSearchQuery`](../../doc/models/album-info-remote-search-query.md) | Body, Required | Remote search query. |

## Response Type

[`List of RemoteSearchResult`](../../doc/models/remote-search-result.md)

## Example Usage

```python
body = AlbumInfoRemoteSearchQuery()

result = item_lookup_controller.get_music_album_remote_search_results(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Music Artist Remote Search Results

Get music artist remote search.

```python
def get_music_artist_remote_search_results(self,
                                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ArtistInfoRemoteSearchQuery`](../../doc/models/artist-info-remote-search-query.md) | Body, Required | Remote search query. |

## Response Type

[`List of RemoteSearchResult`](../../doc/models/remote-search-result.md)

## Example Usage

```python
body = ArtistInfoRemoteSearchQuery()

result = item_lookup_controller.get_music_artist_remote_search_results(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Music Video Remote Search Results

Get music video remote search.

```python
def get_music_video_remote_search_results(self,
                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MusicVideoInfoRemoteSearchQuery`](../../doc/models/music-video-info-remote-search-query.md) | Body, Required | Remote search query. |

## Response Type

[`List of RemoteSearchResult`](../../doc/models/remote-search-result.md)

## Example Usage

```python
body = MusicVideoInfoRemoteSearchQuery()

result = item_lookup_controller.get_music_video_remote_search_results(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Person Remote Search Results

Get person remote search.

```python
def get_person_remote_search_results(self,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PersonLookupInfoRemoteSearchQuery`](../../doc/models/person-lookup-info-remote-search-query.md) | Body, Required | Remote search query. |

## Response Type

[`List of RemoteSearchResult`](../../doc/models/remote-search-result.md)

## Example Usage

```python
body = PersonLookupInfoRemoteSearchQuery()

result = item_lookup_controller.get_person_remote_search_results(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Series Remote Search Results

Get series remote search.

```python
def get_series_remote_search_results(self,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SeriesInfoRemoteSearchQuery`](../../doc/models/series-info-remote-search-query.md) | Body, Required | Remote search query. |

## Response Type

[`List of RemoteSearchResult`](../../doc/models/remote-search-result.md)

## Example Usage

```python
body = SeriesInfoRemoteSearchQuery()

result = item_lookup_controller.get_series_remote_search_results(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Trailer Remote Search Results

Get trailer remote search.

```python
def get_trailer_remote_search_results(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TrailerInfoRemoteSearchQuery`](../../doc/models/trailer-info-remote-search-query.md) | Body, Required | Remote search query. |

## Response Type

[`List of RemoteSearchResult`](../../doc/models/remote-search-result.md)

## Example Usage

```python
body = TrailerInfoRemoteSearchQuery()

result = item_lookup_controller.get_trailer_remote_search_results(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

