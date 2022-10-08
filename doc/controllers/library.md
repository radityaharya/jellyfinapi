# Library

```python
library_controller = client.library
```

## Class Name

`LibraryController`

## Methods

* [Delete Item](../../doc/controllers/library.md#delete-item)
* [Delete Items](../../doc/controllers/library.md#delete-items)
* [Get Ancestors](../../doc/controllers/library.md#get-ancestors)
* [Get Critic Reviews](../../doc/controllers/library.md#get-critic-reviews)
* [Get Download](../../doc/controllers/library.md#get-download)
* [Get File](../../doc/controllers/library.md#get-file)
* [Get Item Counts](../../doc/controllers/library.md#get-item-counts)
* [Get Library Options Info](../../doc/controllers/library.md#get-library-options-info)
* [Get Media Folders](../../doc/controllers/library.md#get-media-folders)
* [Get Physical Paths](../../doc/controllers/library.md#get-physical-paths)
* [Get Similar Albums](../../doc/controllers/library.md#get-similar-albums)
* [Get Similar Artists](../../doc/controllers/library.md#get-similar-artists)
* [Get Similar Items](../../doc/controllers/library.md#get-similar-items)
* [Get Similar Movies](../../doc/controllers/library.md#get-similar-movies)
* [Get Similar Shows](../../doc/controllers/library.md#get-similar-shows)
* [Get Similar Trailers](../../doc/controllers/library.md#get-similar-trailers)
* [Get Theme Media](../../doc/controllers/library.md#get-theme-media)
* [Get Theme Songs](../../doc/controllers/library.md#get-theme-songs)
* [Get Theme Videos](../../doc/controllers/library.md#get-theme-videos)
* [Post Added Movies](../../doc/controllers/library.md#post-added-movies)
* [Post Added Series](../../doc/controllers/library.md#post-added-series)
* [Post Updated Media](../../doc/controllers/library.md#post-updated-media)
* [Post Updated Movies](../../doc/controllers/library.md#post-updated-movies)
* [Post Updated Series](../../doc/controllers/library.md#post-updated-series)
* [Refresh Library](../../doc/controllers/library.md#refresh-library)


# Delete Item

Deletes an item from the library and filesystem.

```python
def delete_item(self,
               item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = library_controller.delete_item(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized access. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 403 | Forbidden | `APIException` |


# Delete Items

Deletes items from the library and filesystem.

```python
def delete_items(self,
                ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `List of uuid\|string` | Query, Optional | The item ids. |

## Response Type

`void`

## Example Usage

```python
result = library_controller.delete_items()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized access. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 403 | Forbidden | `APIException` |


# Get Ancestors

Gets all parents of an item.

```python
def get_ancestors(self,
                 item_id,
                 user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |

## Response Type

[`List of BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = library_controller.get_ancestors(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Critic Reviews

**This endpoint is deprecated.**

Gets critic review for an item.

```python
def get_critic_reviews(self,
                      item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `string` | Template, Required | - |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
item_id = 'itemId8'

result = library_controller.get_critic_reviews(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Download

Downloads item media.

```python
def get_download(self,
                item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = library_controller.get_download(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get File

Get the original file of an item.

```python
def get_file(self,
            item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = library_controller.get_file(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Item Counts

Get item counts.

```python
def get_item_counts(self,
                   user_id=None,
                   is_favorite=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Get counts from a specific user's library. |
| `is_favorite` | `bool` | Query, Optional | Optional. Get counts of favorite items. |

## Response Type

[`ItemCounts`](../../doc/models/item-counts.md)

## Example Usage

```python
result = library_controller.get_item_counts()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Library Options Info

Gets the library options info.

```python
def get_library_options_info(self,
                            library_content_type=None,
                            is_new_library=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `library_content_type` | `string` | Query, Optional | Library content type. |
| `is_new_library` | `bool` | Query, Optional | Whether this is a new library.<br>**Default**: `False` |

## Response Type

[`LibraryOptionsResultDto`](../../doc/models/library-options-result-dto.md)

## Example Usage

```python
is_new_library = False

result = library_controller.get_library_options_info(None, is_new_library)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Media Folders

Gets all user media folders.

```python
def get_media_folders(self,
                     is_hidden=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_hidden` | `bool` | Query, Optional | Optional. Filter by folders that are marked hidden, or not. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
result = library_controller.get_media_folders()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Physical Paths

Gets a list of physical paths from virtual folders.

```python
def get_physical_paths(self)
```

## Response Type

`List of string`

## Example Usage

```python
result = library_controller.get_physical_paths()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Similar Albums

Gets similar items.

```python
def get_similar_albums(self,
                      item_id,
                      exclude_artist_ids=None,
                      user_id=None,
                      limit=None,
                      fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `exclude_artist_ids` | `List of uuid\|string` | Query, Optional | Exclude artist ids. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = library_controller.get_similar_albums(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Similar Artists

Gets similar items.

```python
def get_similar_artists(self,
                       item_id,
                       exclude_artist_ids=None,
                       user_id=None,
                       limit=None,
                       fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `exclude_artist_ids` | `List of uuid\|string` | Query, Optional | Exclude artist ids. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = library_controller.get_similar_artists(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Similar Items

Gets similar items.

```python
def get_similar_items(self,
                     item_id,
                     exclude_artist_ids=None,
                     user_id=None,
                     limit=None,
                     fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `exclude_artist_ids` | `List of uuid\|string` | Query, Optional | Exclude artist ids. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = library_controller.get_similar_items(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Similar Movies

Gets similar items.

```python
def get_similar_movies(self,
                      item_id,
                      exclude_artist_ids=None,
                      user_id=None,
                      limit=None,
                      fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `exclude_artist_ids` | `List of uuid\|string` | Query, Optional | Exclude artist ids. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = library_controller.get_similar_movies(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Similar Shows

Gets similar items.

```python
def get_similar_shows(self,
                     item_id,
                     exclude_artist_ids=None,
                     user_id=None,
                     limit=None,
                     fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `exclude_artist_ids` | `List of uuid\|string` | Query, Optional | Exclude artist ids. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = library_controller.get_similar_shows(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Similar Trailers

Gets similar items.

```python
def get_similar_trailers(self,
                        item_id,
                        exclude_artist_ids=None,
                        user_id=None,
                        limit=None,
                        fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `exclude_artist_ids` | `List of uuid\|string` | Query, Optional | Exclude artist ids. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = library_controller.get_similar_trailers(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Theme Media

Get theme songs and videos for an item.

```python
def get_theme_media(self,
                   item_id,
                   user_id=None,
                   inherit_from_parent=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `inherit_from_parent` | `bool` | Query, Optional | Optional. Determines whether or not parent items should be searched for theme media.<br>**Default**: `False` |

## Response Type

[`AllThemeMediaResult`](../../doc/models/all-theme-media-result.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
inherit_from_parent = False

result = library_controller.get_theme_media(item_id, None, inherit_from_parent)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | `APIException` |


# Get Theme Songs

Get theme songs for an item.

```python
def get_theme_songs(self,
                   item_id,
                   user_id=None,
                   inherit_from_parent=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `inherit_from_parent` | `bool` | Query, Optional | Optional. Determines whether or not parent items should be searched for theme media.<br>**Default**: `False` |

## Response Type

[`ThemeMediaResult`](../../doc/models/theme-media-result.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
inherit_from_parent = False

result = library_controller.get_theme_songs(item_id, None, inherit_from_parent)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Theme Videos

Get theme videos for an item.

```python
def get_theme_videos(self,
                    item_id,
                    user_id=None,
                    inherit_from_parent=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `inherit_from_parent` | `bool` | Query, Optional | Optional. Determines whether or not parent items should be searched for theme media.<br>**Default**: `False` |

## Response Type

[`ThemeMediaResult`](../../doc/models/theme-media-result.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
inherit_from_parent = False

result = library_controller.get_theme_videos(item_id, None, inherit_from_parent)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Post Added Movies

Reports that new movies have been added by an external source.

```python
def post_added_movies(self,
                     tmdb_id=None,
                     imdb_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tmdb_id` | `string` | Query, Optional | The tmdbId. |
| `imdb_id` | `string` | Query, Optional | The imdbId. |

## Response Type

`void`

## Example Usage

```python
result = library_controller.post_added_movies()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Post Added Series

Reports that new episodes of a series have been added by an external source.

```python
def post_added_series(self,
                     tvdb_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tvdb_id` | `string` | Query, Optional | The tvdbId. |

## Response Type

`void`

## Example Usage

```python
result = library_controller.post_added_series()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Post Updated Media

Reports that new movies have been added by an external source.

```python
def post_updated_media(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MediaUpdateInfoDto`](../../doc/models/media-update-info-dto.md) | Body, Required | The update paths. |

## Response Type

`void`

## Example Usage

```python
body = MediaUpdateInfoDto()

result = library_controller.post_updated_media(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Post Updated Movies

Reports that new movies have been added by an external source.

```python
def post_updated_movies(self,
                       tmdb_id=None,
                       imdb_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tmdb_id` | `string` | Query, Optional | The tmdbId. |
| `imdb_id` | `string` | Query, Optional | The imdbId. |

## Response Type

`void`

## Example Usage

```python
result = library_controller.post_updated_movies()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Post Updated Series

Reports that new episodes of a series have been added by an external source.

```python
def post_updated_series(self,
                       tvdb_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tvdb_id` | `string` | Query, Optional | The tvdbId. |

## Response Type

`void`

## Example Usage

```python
result = library_controller.post_updated_series()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Refresh Library

Starts a library scan.

```python
def refresh_library(self)
```

## Response Type

`void`

## Example Usage

```python
result = library_controller.refresh_library()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

