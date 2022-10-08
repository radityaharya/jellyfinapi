# Trailers

```python
trailers_controller = client.trailers
```

## Class Name

`TrailersController`


# Get Trailers

Finds movies and trailers similar to a given trailer.

```python
def get_trailers(self,
                user_id=None,
                max_official_rating=None,
                has_theme_song=None,
                has_theme_video=None,
                has_subtitles=None,
                has_special_feature=None,
                has_trailer=None,
                adjacent_to=None,
                parent_index_number=None,
                has_parental_rating=None,
                is_hd=None,
                is_4_k=None,
                location_types=None,
                exclude_location_types=None,
                is_missing=None,
                is_unaired=None,
                min_community_rating=None,
                min_critic_rating=None,
                min_premiere_date=None,
                min_date_last_saved=None,
                min_date_last_saved_for_user=None,
                max_premiere_date=None,
                has_overview=None,
                has_imdb_id=None,
                has_tmdb_id=None,
                has_tvdb_id=None,
                is_movie=None,
                is_series=None,
                is_news=None,
                is_kids=None,
                is_sports=None,
                exclude_item_ids=None,
                start_index=None,
                limit=None,
                recursive=None,
                search_term=None,
                sort_order=None,
                parent_id=None,
                fields=None,
                exclude_item_types=None,
                filters=None,
                is_favorite=None,
                media_types=None,
                image_types=None,
                sort_by=None,
                is_played=None,
                genres=None,
                official_ratings=None,
                tags=None,
                years=None,
                enable_user_data=None,
                image_type_limit=None,
                enable_image_types=None,
                person=None,
                person_ids=None,
                person_types=None,
                studios=None,
                artists=None,
                exclude_artist_ids=None,
                artist_ids=None,
                album_artist_ids=None,
                contributing_artist_ids=None,
                albums=None,
                album_ids=None,
                ids=None,
                video_types=None,
                min_official_rating=None,
                is_locked=None,
                is_place_holder=None,
                has_official_rating=None,
                collapse_box_set_items=None,
                min_width=None,
                min_height=None,
                max_width=None,
                max_height=None,
                is_3_d=None,
                series_status=None,
                name_starts_with_or_greater=None,
                name_starts_with=None,
                name_less_than=None,
                studio_ids=None,
                genre_ids=None,
                enable_total_record_count=True,
                enable_images=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | The user id. |
| `max_official_rating` | `string` | Query, Optional | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). |
| `has_theme_song` | `bool` | Query, Optional | Optional filter by items with theme songs. |
| `has_theme_video` | `bool` | Query, Optional | Optional filter by items with theme videos. |
| `has_subtitles` | `bool` | Query, Optional | Optional filter by items with subtitles. |
| `has_special_feature` | `bool` | Query, Optional | Optional filter by items with special features. |
| `has_trailer` | `bool` | Query, Optional | Optional filter by items with trailers. |
| `adjacent_to` | `string` | Query, Optional | Optional. Return items that are siblings of a supplied item. |
| `parent_index_number` | `int` | Query, Optional | Optional filter by parent index number. |
| `has_parental_rating` | `bool` | Query, Optional | Optional filter by items that have or do not have a parental rating. |
| `is_hd` | `bool` | Query, Optional | Optional filter by items that are HD or not. |
| `is_4_k` | `bool` | Query, Optional | Optional filter by items that are 4K or not. |
| `location_types` | [`List of LocationTypeEnum`](../../doc/models/location-type-enum.md) | Query, Optional | Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimited. |
| `exclude_location_types` | [`List of LocationTypeEnum`](../../doc/models/location-type-enum.md) | Query, Optional | Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimited. |
| `is_missing` | `bool` | Query, Optional | Optional filter by items that are missing episodes or not. |
| `is_unaired` | `bool` | Query, Optional | Optional filter by items that are unaired episodes or not. |
| `min_community_rating` | `float` | Query, Optional | Optional filter by minimum community rating. |
| `min_critic_rating` | `float` | Query, Optional | Optional filter by minimum critic rating. |
| `min_premiere_date` | `datetime` | Query, Optional | Optional. The minimum premiere date. Format = ISO. |
| `min_date_last_saved` | `datetime` | Query, Optional | Optional. The minimum last saved date. Format = ISO. |
| `min_date_last_saved_for_user` | `datetime` | Query, Optional | Optional. The minimum last saved date for the current user. Format = ISO. |
| `max_premiere_date` | `datetime` | Query, Optional | Optional. The maximum premiere date. Format = ISO. |
| `has_overview` | `bool` | Query, Optional | Optional filter by items that have an overview or not. |
| `has_imdb_id` | `bool` | Query, Optional | Optional filter by items that have an imdb id or not. |
| `has_tmdb_id` | `bool` | Query, Optional | Optional filter by items that have a tmdb id or not. |
| `has_tvdb_id` | `bool` | Query, Optional | Optional filter by items that have a tvdb id or not. |
| `is_movie` | `bool` | Query, Optional | Optional filter for live tv movies. |
| `is_series` | `bool` | Query, Optional | Optional filter for live tv series. |
| `is_news` | `bool` | Query, Optional | Optional filter for live tv news. |
| `is_kids` | `bool` | Query, Optional | Optional filter for live tv kids. |
| `is_sports` | `bool` | Query, Optional | Optional filter for live tv sports. |
| `exclude_item_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered by excluding item ids. This allows multiple, comma delimited. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `recursive` | `bool` | Query, Optional | When searching within folders, this determines whether or not the search will be recursive. true/false. |
| `search_term` | `string` | Query, Optional | Optional. Filter based on a search term. |
| `sort_order` | [`List of SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Sort Order - Ascending,Descending. |
| `parent_id` | `uuid\|string` | Query, Optional | Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines. |
| `exclude_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. |
| `filters` | [`List of ItemFilterEnum`](../../doc/models/item-filter-enum.md) | Query, Optional | Optional. Specify additional filters to apply. This allows multiple, comma delimited. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes. |
| `is_favorite` | `bool` | Query, Optional | Optional filter by items that are marked as favorite, or not. |
| `media_types` | `List of string` | Query, Optional | Optional filter by MediaType. Allows multiple, comma delimited. |
| `image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. |
| `sort_by` | `List of string` | Query, Optional | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. |
| `is_played` | `bool` | Query, Optional | Optional filter by items that are played, or not. |
| `genres` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. |
| `official_ratings` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. |
| `tags` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. |
| `years` | `List of int` | Query, Optional | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. |
| `enable_user_data` | `bool` | Query, Optional | Optional, include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional, the max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `person` | `string` | Query, Optional | Optional. If specified, results will be filtered to include only those containing the specified person. |
| `person_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered to include only those containing the specified person id. |
| `person_types` | `List of string` | Query, Optional | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. |
| `studios` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. |
| `artists` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimited. |
| `exclude_artist_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimited. |
| `artist_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered to include only those containing the specified artist id. |
| `album_artist_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered to include only those containing the specified album artist id. |
| `contributing_artist_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered to include only those containing the specified contributing artist id. |
| `albums` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimited. |
| `album_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimited. |
| `ids` | `List of uuid\|string` | Query, Optional | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. |
| `video_types` | [`List of VideoTypeEnum`](../../doc/models/video-type-enum.md) | Query, Optional | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimited. |
| `min_official_rating` | `string` | Query, Optional | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). |
| `is_locked` | `bool` | Query, Optional | Optional filter by items that are locked. |
| `is_place_holder` | `bool` | Query, Optional | Optional filter by items that are placeholders. |
| `has_official_rating` | `bool` | Query, Optional | Optional filter by items that have official ratings. |
| `collapse_box_set_items` | `bool` | Query, Optional | Whether or not to hide items behind their boxsets. |
| `min_width` | `int` | Query, Optional | Optional. Filter by the minimum width of the item. |
| `min_height` | `int` | Query, Optional | Optional. Filter by the minimum height of the item. |
| `max_width` | `int` | Query, Optional | Optional. Filter by the maximum width of the item. |
| `max_height` | `int` | Query, Optional | Optional. Filter by the maximum height of the item. |
| `is_3_d` | `bool` | Query, Optional | Optional filter by items that are 3D, or not. |
| `series_status` | [`List of SeriesStatusEnum`](../../doc/models/series-status-enum.md) | Query, Optional | Optional filter by Series Status. Allows multiple, comma delimited. |
| `name_starts_with_or_greater` | `string` | Query, Optional | Optional filter by items whose name is sorted equally or greater than a given input string. |
| `name_starts_with` | `string` | Query, Optional | Optional filter by items whose name is sorted equally than a given input string. |
| `name_less_than` | `string` | Query, Optional | Optional filter by items whose name is equally or lesser than a given input string. |
| `studio_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. |
| `genre_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. |
| `enable_total_record_count` | `bool` | Query, Optional | Optional. Enable the total record count.<br>**Default**: `True` |
| `enable_images` | `bool` | Query, Optional | Optional, include image information in output.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_total_record_count = True
enable_images = True

result = trailers_controller.get_trailers(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_total_record_count, enable_images)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

