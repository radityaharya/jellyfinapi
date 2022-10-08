
# Base Item Dto

This is strictly used as a data transfer object from the api layer.
This holds information about a BaseItem in a format that is convenient for the client.

## Structure

`BaseItemDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the name. |
| `original_title` | `string` | Optional | - |
| `server_id` | `string` | Optional | Gets or sets the server identifier. |
| `id` | `uuid\|string` | Optional | Gets or sets the id. |
| `etag` | `string` | Optional | Gets or sets the etag. |
| `source_type` | `string` | Optional | Gets or sets the type of the source. |
| `playlist_item_id` | `string` | Optional | Gets or sets the playlist item identifier. |
| `date_created` | `datetime` | Optional | Gets or sets the date created. |
| `date_last_media_added` | `datetime` | Optional | - |
| `extra_type` | `string` | Optional | - |
| `airs_before_season_number` | `int` | Optional | - |
| `airs_after_season_number` | `int` | Optional | - |
| `airs_before_episode_number` | `int` | Optional | - |
| `can_delete` | `bool` | Optional | - |
| `can_download` | `bool` | Optional | - |
| `has_subtitles` | `bool` | Optional | - |
| `preferred_metadata_language` | `string` | Optional | - |
| `preferred_metadata_country_code` | `string` | Optional | - |
| `supports_sync` | `bool` | Optional | Gets or sets a value indicating whether [supports synchronize]. |
| `container` | `string` | Optional | - |
| `sort_name` | `string` | Optional | Gets or sets the name of the sort. |
| `forced_sort_name` | `string` | Optional | - |
| `video_3_d_format` | [`Video3DFormatEnum`](../../doc/models/video-3-d-format-enum.md) | Optional | Gets or sets the video3 D format. |
| `premiere_date` | `datetime` | Optional | Gets or sets the premiere date. |
| `external_urls` | [`List of ExternalUrl`](../../doc/models/external-url.md) | Optional | Gets or sets the external urls. |
| `media_sources` | [`List of MediaSourceInfo`](../../doc/models/media-source-info.md) | Optional | Gets or sets the media versions. |
| `critic_rating` | `float` | Optional | Gets or sets the critic rating. |
| `production_locations` | `List of string` | Optional | - |
| `path` | `string` | Optional | Gets or sets the path. |
| `enable_media_source_display` | `bool` | Optional | - |
| `official_rating` | `string` | Optional | Gets or sets the official rating. |
| `custom_rating` | `string` | Optional | Gets or sets the custom rating. |
| `channel_id` | `uuid\|string` | Optional | Gets or sets the channel identifier. |
| `channel_name` | `string` | Optional | - |
| `overview` | `string` | Optional | Gets or sets the overview. |
| `taglines` | `List of string` | Optional | Gets or sets the taglines. |
| `genres` | `List of string` | Optional | Gets or sets the genres. |
| `community_rating` | `float` | Optional | Gets or sets the community rating. |
| `cumulative_run_time_ticks` | `long\|int` | Optional | Gets or sets the cumulative run time ticks. |
| `run_time_ticks` | `long\|int` | Optional | Gets or sets the run time ticks. |
| `play_access` | [`PlayAccessEnum`](../../doc/models/play-access-enum.md) | Optional | Gets or sets the play access. |
| `aspect_ratio` | `string` | Optional | Gets or sets the aspect ratio. |
| `production_year` | `int` | Optional | Gets or sets the production year. |
| `is_place_holder` | `bool` | Optional | Gets or sets a value indicating whether this instance is place holder. |
| `number` | `string` | Optional | Gets or sets the number. |
| `channel_number` | `string` | Optional | - |
| `index_number` | `int` | Optional | Gets or sets the index number. |
| `index_number_end` | `int` | Optional | Gets or sets the index number end. |
| `parent_index_number` | `int` | Optional | Gets or sets the parent index number. |
| `remote_trailers` | [`List of MediaUrl`](../../doc/models/media-url.md) | Optional | Gets or sets the trailer urls. |
| `provider_ids` | `dict` | Optional | Gets or sets the provider ids. |
| `is_hd` | `bool` | Optional | Gets or sets a value indicating whether this instance is HD. |
| `is_folder` | `bool` | Optional | Gets or sets a value indicating whether this instance is folder. |
| `parent_id` | `uuid\|string` | Optional | Gets or sets the parent id. |
| `mtype` | [`BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Optional | The base item kind. |
| `people` | [`List of BaseItemPerson`](../../doc/models/base-item-person.md) | Optional | Gets or sets the people. |
| `studios` | [`List of NameGuidPair`](../../doc/models/name-guid-pair.md) | Optional | Gets or sets the studios. |
| `genre_items` | [`List of NameGuidPair`](../../doc/models/name-guid-pair.md) | Optional | - |
| `parent_logo_item_id` | `uuid\|string` | Optional | Gets or sets wether the item has a logo, this will hold the Id of the Parent that has one. |
| `parent_backdrop_item_id` | `uuid\|string` | Optional | Gets or sets wether the item has any backdrops, this will hold the Id of the Parent that has one. |
| `parent_backdrop_image_tags` | `List of string` | Optional | Gets or sets the parent backdrop image tags. |
| `local_trailer_count` | `int` | Optional | Gets or sets the local trailer count. |
| `user_data` | [`UserItemDataDto`](../../doc/models/user-item-data-dto.md) | Optional | Gets or sets the user data for this item based on the user it's being requested for. |
| `recursive_item_count` | `int` | Optional | Gets or sets the recursive item count. |
| `child_count` | `int` | Optional | Gets or sets the child count. |
| `series_name` | `string` | Optional | Gets or sets the name of the series. |
| `series_id` | `uuid\|string` | Optional | Gets or sets the series id. |
| `season_id` | `uuid\|string` | Optional | Gets or sets the season identifier. |
| `special_feature_count` | `int` | Optional | Gets or sets the special feature count. |
| `display_preferences_id` | `string` | Optional | Gets or sets the display preferences id. |
| `status` | `string` | Optional | Gets or sets the status. |
| `air_time` | `string` | Optional | Gets or sets the air time. |
| `air_days` | [`List of DayOfWeekEnum`](../../doc/models/day-of-week-enum.md) | Optional | Gets or sets the air days. |
| `tags` | `List of string` | Optional | Gets or sets the tags. |
| `primary_image_aspect_ratio` | `float` | Optional | Gets or sets the primary image aspect ratio, after image enhancements. |
| `artists` | `List of string` | Optional | Gets or sets the artists. |
| `artist_items` | [`List of NameGuidPair`](../../doc/models/name-guid-pair.md) | Optional | Gets or sets the artist items. |
| `album` | `string` | Optional | Gets or sets the album. |
| `collection_type` | `string` | Optional | Gets or sets the type of the collection. |
| `display_order` | `string` | Optional | Gets or sets the display order. |
| `album_id` | `uuid\|string` | Optional | Gets or sets the album id. |
| `album_primary_image_tag` | `string` | Optional | Gets or sets the album image tag. |
| `series_primary_image_tag` | `string` | Optional | Gets or sets the series primary image tag. |
| `album_artist` | `string` | Optional | Gets or sets the album artist. |
| `album_artists` | [`List of NameGuidPair`](../../doc/models/name-guid-pair.md) | Optional | Gets or sets the album artists. |
| `season_name` | `string` | Optional | Gets or sets the name of the season. |
| `media_streams` | [`List of MediaStream`](../../doc/models/media-stream.md) | Optional | Gets or sets the media streams. |
| `video_type` | [`VideoTypeEnum`](../../doc/models/video-type-enum.md) | Optional | Gets or sets the type of the video. |
| `part_count` | `int` | Optional | Gets or sets the part count. |
| `media_source_count` | `int` | Optional | - |
| `image_tags` | `dict` | Optional | Gets or sets the image tags. |
| `backdrop_image_tags` | `List of string` | Optional | Gets or sets the backdrop image tags. |
| `screenshot_image_tags` | `List of string` | Optional | Gets or sets the screenshot image tags. |
| `parent_logo_image_tag` | `string` | Optional | Gets or sets the parent logo image tag. |
| `parent_art_item_id` | `uuid\|string` | Optional | Gets or sets wether the item has fan art, this will hold the Id of the Parent that has one. |
| `parent_art_image_tag` | `string` | Optional | Gets or sets the parent art image tag. |
| `series_thumb_image_tag` | `string` | Optional | Gets or sets the series thumb image tag. |
| `image_blur_hashes` | [`ImageBlurHashes1`](../../doc/models/image-blur-hashes-1.md) | Optional | Gets or sets the blurhashes for the image tags.<br>Maps image type to dictionary mapping image tag to blurhash value. |
| `series_studio` | `string` | Optional | Gets or sets the series studio. |
| `parent_thumb_item_id` | `uuid\|string` | Optional | Gets or sets the parent thumb item id. |
| `parent_thumb_image_tag` | `string` | Optional | Gets or sets the parent thumb image tag. |
| `parent_primary_image_item_id` | `string` | Optional | Gets or sets the parent primary image item identifier. |
| `parent_primary_image_tag` | `string` | Optional | Gets or sets the parent primary image tag. |
| `chapters` | [`List of ChapterInfo`](../../doc/models/chapter-info.md) | Optional | Gets or sets the chapters. |
| `location_type` | [`LocationTypeEnum`](../../doc/models/location-type-enum.md) | Optional | Gets or sets the type of the location. |
| `iso_type` | [`IsoTypeEnum`](../../doc/models/iso-type-enum.md) | Optional | Gets or sets the type of the iso. |
| `media_type` | `string` | Optional | Gets or sets the type of the media. |
| `end_date` | `datetime` | Optional | Gets or sets the end date. |
| `locked_fields` | [`List of MetadataFieldEnum`](../../doc/models/metadata-field-enum.md) | Optional | Gets or sets the locked fields. |
| `trailer_count` | `int` | Optional | Gets or sets the trailer count. |
| `movie_count` | `int` | Optional | Gets or sets the movie count. |
| `series_count` | `int` | Optional | Gets or sets the series count. |
| `program_count` | `int` | Optional | - |
| `episode_count` | `int` | Optional | Gets or sets the episode count. |
| `song_count` | `int` | Optional | Gets or sets the song count. |
| `album_count` | `int` | Optional | Gets or sets the album count. |
| `artist_count` | `int` | Optional | - |
| `music_video_count` | `int` | Optional | Gets or sets the music video count. |
| `lock_data` | `bool` | Optional | Gets or sets a value indicating whether [enable internet providers]. |
| `width` | `int` | Optional | - |
| `height` | `int` | Optional | - |
| `camera_make` | `string` | Optional | - |
| `camera_model` | `string` | Optional | - |
| `software` | `string` | Optional | - |
| `exposure_time` | `float` | Optional | - |
| `focal_length` | `float` | Optional | - |
| `image_orientation` | [`ImageOrientationEnum`](../../doc/models/image-orientation-enum.md) | Optional | - |
| `aperture` | `float` | Optional | - |
| `shutter_speed` | `float` | Optional | - |
| `latitude` | `float` | Optional | - |
| `longitude` | `float` | Optional | - |
| `altitude` | `float` | Optional | - |
| `iso_speed_rating` | `int` | Optional | - |
| `series_timer_id` | `string` | Optional | Gets or sets the series timer identifier. |
| `program_id` | `string` | Optional | Gets or sets the program identifier. |
| `channel_primary_image_tag` | `string` | Optional | Gets or sets the channel primary image tag. |
| `start_date` | `datetime` | Optional | Gets or sets the start date of the recording, in UTC. |
| `completion_percentage` | `float` | Optional | Gets or sets the completion percentage. |
| `is_repeat` | `bool` | Optional | Gets or sets a value indicating whether this instance is repeat. |
| `episode_title` | `string` | Optional | Gets or sets the episode title. |
| `channel_type` | [`ChannelTypeEnum`](../../doc/models/channel-type-enum.md) | Optional | Gets or sets the type of the channel. |
| `audio` | [`ProgramAudioEnum`](../../doc/models/program-audio-enum.md) | Optional | Gets or sets the audio. |
| `is_movie` | `bool` | Optional | Gets or sets a value indicating whether this instance is movie. |
| `is_sports` | `bool` | Optional | Gets or sets a value indicating whether this instance is sports. |
| `is_series` | `bool` | Optional | Gets or sets a value indicating whether this instance is series. |
| `is_live` | `bool` | Optional | Gets or sets a value indicating whether this instance is live. |
| `is_news` | `bool` | Optional | Gets or sets a value indicating whether this instance is news. |
| `is_kids` | `bool` | Optional | Gets or sets a value indicating whether this instance is kids. |
| `is_premiere` | `bool` | Optional | Gets or sets a value indicating whether this instance is premiere. |
| `timer_id` | `string` | Optional | Gets or sets the timer identifier. |
| `current_program` | [`BaseItemDto`](../../doc/models/base-item-dto.md) | Optional | Gets or sets the current program. |

## Example (as JSON)

```json
{
  "Name": null,
  "OriginalTitle": null,
  "ServerId": null,
  "Id": null,
  "Etag": null,
  "SourceType": null,
  "PlaylistItemId": null,
  "DateCreated": null,
  "DateLastMediaAdded": null,
  "ExtraType": null,
  "AirsBeforeSeasonNumber": null,
  "AirsAfterSeasonNumber": null,
  "AirsBeforeEpisodeNumber": null,
  "CanDelete": null,
  "CanDownload": null,
  "HasSubtitles": null,
  "PreferredMetadataLanguage": null,
  "PreferredMetadataCountryCode": null,
  "SupportsSync": null,
  "Container": null,
  "SortName": null,
  "ForcedSortName": null,
  "Video3DFormat": null,
  "PremiereDate": null,
  "ExternalUrls": null,
  "MediaSources": null,
  "CriticRating": null,
  "ProductionLocations": null,
  "Path": null,
  "EnableMediaSourceDisplay": null,
  "OfficialRating": null,
  "CustomRating": null,
  "ChannelId": null,
  "ChannelName": null,
  "Overview": null,
  "Taglines": null,
  "Genres": null,
  "CommunityRating": null,
  "CumulativeRunTimeTicks": null,
  "RunTimeTicks": null,
  "PlayAccess": null,
  "AspectRatio": null,
  "ProductionYear": null,
  "IsPlaceHolder": null,
  "Number": null,
  "ChannelNumber": null,
  "IndexNumber": null,
  "IndexNumberEnd": null,
  "ParentIndexNumber": null,
  "RemoteTrailers": null,
  "ProviderIds": null,
  "IsHD": null,
  "IsFolder": null,
  "ParentId": null,
  "Type": null,
  "People": null,
  "Studios": null,
  "GenreItems": null,
  "ParentLogoItemId": null,
  "ParentBackdropItemId": null,
  "ParentBackdropImageTags": null,
  "LocalTrailerCount": null,
  "UserData": null,
  "RecursiveItemCount": null,
  "ChildCount": null,
  "SeriesName": null,
  "SeriesId": null,
  "SeasonId": null,
  "SpecialFeatureCount": null,
  "DisplayPreferencesId": null,
  "Status": null,
  "AirTime": null,
  "AirDays": null,
  "Tags": null,
  "PrimaryImageAspectRatio": null,
  "Artists": null,
  "ArtistItems": null,
  "Album": null,
  "CollectionType": null,
  "DisplayOrder": null,
  "AlbumId": null,
  "AlbumPrimaryImageTag": null,
  "SeriesPrimaryImageTag": null,
  "AlbumArtist": null,
  "AlbumArtists": null,
  "SeasonName": null,
  "MediaStreams": null,
  "VideoType": null,
  "PartCount": null,
  "MediaSourceCount": null,
  "ImageTags": null,
  "BackdropImageTags": null,
  "ScreenshotImageTags": null,
  "ParentLogoImageTag": null,
  "ParentArtItemId": null,
  "ParentArtImageTag": null,
  "SeriesThumbImageTag": null,
  "ImageBlurHashes": null,
  "SeriesStudio": null,
  "ParentThumbItemId": null,
  "ParentThumbImageTag": null,
  "ParentPrimaryImageItemId": null,
  "ParentPrimaryImageTag": null,
  "Chapters": null,
  "LocationType": null,
  "IsoType": null,
  "MediaType": null,
  "EndDate": null,
  "LockedFields": null,
  "TrailerCount": null,
  "MovieCount": null,
  "SeriesCount": null,
  "ProgramCount": null,
  "EpisodeCount": null,
  "SongCount": null,
  "AlbumCount": null,
  "ArtistCount": null,
  "MusicVideoCount": null,
  "LockData": null,
  "Width": null,
  "Height": null,
  "CameraMake": null,
  "CameraModel": null,
  "Software": null,
  "ExposureTime": null,
  "FocalLength": null,
  "ImageOrientation": null,
  "Aperture": null,
  "ShutterSpeed": null,
  "Latitude": null,
  "Longitude": null,
  "Altitude": null,
  "IsoSpeedRating": null,
  "SeriesTimerId": null,
  "ProgramId": null,
  "ChannelPrimaryImageTag": null,
  "StartDate": null,
  "CompletionPercentage": null,
  "IsRepeat": null,
  "EpisodeTitle": null,
  "ChannelType": null,
  "Audio": null,
  "IsMovie": null,
  "IsSports": null,
  "IsSeries": null,
  "IsLive": null,
  "IsNews": null,
  "IsKids": null,
  "IsPremiere": null,
  "TimerId": null,
  "CurrentProgram": null
}
```

