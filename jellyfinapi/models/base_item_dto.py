# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.base_item_person import BaseItemPerson
from jellyfinapi.models.chapter_info import ChapterInfo
from jellyfinapi.models.external_url import ExternalUrl
from jellyfinapi.models.image_blur_hashes_1 import ImageBlurHashes1
from jellyfinapi.models.media_source_info import MediaSourceInfo
from jellyfinapi.models.media_stream import MediaStream
from jellyfinapi.models.media_url import MediaUrl
from jellyfinapi.models.name_guid_pair import NameGuidPair
from jellyfinapi.models.user_item_data_dto import UserItemDataDto
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class BaseItemDto(object):

    """Implementation of the 'BaseItemDto' model.

    This is strictly used as a data transfer object from the api layer.
    This holds information about a BaseItem in a format that is convenient for
    the client.

    Attributes:
        name (string): Gets or sets the name.
        original_title (string): TODO: type description here.
        server_id (string): Gets or sets the server identifier.
        id (uuid|string): Gets or sets the id.
        etag (string): Gets or sets the etag.
        source_type (string): Gets or sets the type of the source.
        playlist_item_id (string): Gets or sets the playlist item identifier.
        date_created (datetime): Gets or sets the date created.
        date_last_media_added (datetime): TODO: type description here.
        extra_type (string): TODO: type description here.
        airs_before_season_number (int): TODO: type description here.
        airs_after_season_number (int): TODO: type description here.
        airs_before_episode_number (int): TODO: type description here.
        can_delete (bool): TODO: type description here.
        can_download (bool): TODO: type description here.
        has_subtitles (bool): TODO: type description here.
        preferred_metadata_language (string): TODO: type description here.
        preferred_metadata_country_code (string): TODO: type description
            here.
        supports_sync (bool): Gets or sets a value indicating whether
            [supports synchronize].
        container (string): TODO: type description here.
        sort_name (string): Gets or sets the name of the sort.
        forced_sort_name (string): TODO: type description here.
        video_3_d_format (Video3DFormatEnum): Gets or sets the video3 D
            format.
        premiere_date (datetime): Gets or sets the premiere date.
        external_urls (list of ExternalUrl): Gets or sets the external urls.
        media_sources (list of MediaSourceInfo): Gets or sets the media
            versions.
        critic_rating (float): Gets or sets the critic rating.
        production_locations (list of string): TODO: type description here.
        path (string): Gets or sets the path.
        enable_media_source_display (bool): TODO: type description here.
        official_rating (string): Gets or sets the official rating.
        custom_rating (string): Gets or sets the custom rating.
        channel_id (uuid|string): Gets or sets the channel identifier.
        channel_name (string): TODO: type description here.
        overview (string): Gets or sets the overview.
        taglines (list of string): Gets or sets the taglines.
        genres (list of string): Gets or sets the genres.
        community_rating (float): Gets or sets the community rating.
        cumulative_run_time_ticks (long|int): Gets or sets the cumulative run
            time ticks.
        run_time_ticks (long|int): Gets or sets the run time ticks.
        play_access (PlayAccessEnum): Gets or sets the play access.
        aspect_ratio (string): Gets or sets the aspect ratio.
        production_year (int): Gets or sets the production year.
        is_place_holder (bool): Gets or sets a value indicating whether this
            instance is place holder.
        number (string): Gets or sets the number.
        channel_number (string): TODO: type description here.
        index_number (int): Gets or sets the index number.
        index_number_end (int): Gets or sets the index number end.
        parent_index_number (int): Gets or sets the parent index number.
        remote_trailers (list of MediaUrl): Gets or sets the trailer urls.
        provider_ids (dict): Gets or sets the provider ids.
        is_hd (bool): Gets or sets a value indicating whether this instance is
            HD.
        is_folder (bool): Gets or sets a value indicating whether this
            instance is folder.
        parent_id (uuid|string): Gets or sets the parent id.
        mtype (BaseItemKindEnum): The base item kind.
        people (list of BaseItemPerson): Gets or sets the people.
        studios (list of NameGuidPair): Gets or sets the studios.
        genre_items (list of NameGuidPair): TODO: type description here.
        parent_logo_item_id (uuid|string): Gets or sets wether the item has a
            logo, this will hold the Id of the Parent that has one.
        parent_backdrop_item_id (uuid|string): Gets or sets wether the item
            has any backdrops, this will hold the Id of the Parent that has
            one.
        parent_backdrop_image_tags (list of string): Gets or sets the parent
            backdrop image tags.
        local_trailer_count (int): Gets or sets the local trailer count.
        user_data (UserItemDataDto): Gets or sets the user data for this item
            based on the user it's being requested for.
        recursive_item_count (int): Gets or sets the recursive item count.
        child_count (int): Gets or sets the child count.
        series_name (string): Gets or sets the name of the series.
        series_id (uuid|string): Gets or sets the series id.
        season_id (uuid|string): Gets or sets the season identifier.
        special_feature_count (int): Gets or sets the special feature count.
        display_preferences_id (string): Gets or sets the display preferences
            id.
        status (string): Gets or sets the status.
        air_time (string): Gets or sets the air time.
        air_days (list of DayOfWeekEnum): Gets or sets the air days.
        tags (list of string): Gets or sets the tags.
        primary_image_aspect_ratio (float): Gets or sets the primary image
            aspect ratio, after image enhancements.
        artists (list of string): Gets or sets the artists.
        artist_items (list of NameGuidPair): Gets or sets the artist items.
        album (string): Gets or sets the album.
        collection_type (string): Gets or sets the type of the collection.
        display_order (string): Gets or sets the display order.
        album_id (uuid|string): Gets or sets the album id.
        album_primary_image_tag (string): Gets or sets the album image tag.
        series_primary_image_tag (string): Gets or sets the series primary
            image tag.
        album_artist (string): Gets or sets the album artist.
        album_artists (list of NameGuidPair): Gets or sets the album artists.
        season_name (string): Gets or sets the name of the season.
        media_streams (list of MediaStream): Gets or sets the media streams.
        video_type (VideoTypeEnum): Gets or sets the type of the video.
        part_count (int): Gets or sets the part count.
        media_source_count (int): TODO: type description here.
        image_tags (dict): Gets or sets the image tags.
        backdrop_image_tags (list of string): Gets or sets the backdrop image
            tags.
        screenshot_image_tags (list of string): Gets or sets the screenshot
            image tags.
        parent_logo_image_tag (string): Gets or sets the parent logo image
            tag.
        parent_art_item_id (uuid|string): Gets or sets wether the item has fan
            art, this will hold the Id of the Parent that has one.
        parent_art_image_tag (string): Gets or sets the parent art image tag.
        series_thumb_image_tag (string): Gets or sets the series thumb image
            tag.
        image_blur_hashes (ImageBlurHashes1): Gets or sets the blurhashes for
            the image tags.  Maps image type to dictionary mapping image tag
            to blurhash value.
        series_studio (string): Gets or sets the series studio.
        parent_thumb_item_id (uuid|string): Gets or sets the parent thumb item
            id.
        parent_thumb_image_tag (string): Gets or sets the parent thumb image
            tag.
        parent_primary_image_item_id (string): Gets or sets the parent primary
            image item identifier.
        parent_primary_image_tag (string): Gets or sets the parent primary
            image tag.
        chapters (list of ChapterInfo): Gets or sets the chapters.
        location_type (LocationTypeEnum): Gets or sets the type of the
            location.
        iso_type (IsoTypeEnum): Gets or sets the type of the iso.
        media_type (string): Gets or sets the type of the media.
        end_date (datetime): Gets or sets the end date.
        locked_fields (list of MetadataFieldEnum): Gets or sets the locked
            fields.
        trailer_count (int): Gets or sets the trailer count.
        movie_count (int): Gets or sets the movie count.
        series_count (int): Gets or sets the series count.
        program_count (int): TODO: type description here.
        episode_count (int): Gets or sets the episode count.
        song_count (int): Gets or sets the song count.
        album_count (int): Gets or sets the album count.
        artist_count (int): TODO: type description here.
        music_video_count (int): Gets or sets the music video count.
        lock_data (bool): Gets or sets a value indicating whether [enable
            internet providers].
        width (int): TODO: type description here.
        height (int): TODO: type description here.
        camera_make (string): TODO: type description here.
        camera_model (string): TODO: type description here.
        software (string): TODO: type description here.
        exposure_time (float): TODO: type description here.
        focal_length (float): TODO: type description here.
        image_orientation (ImageOrientationEnum): TODO: type description
            here.
        aperture (float): TODO: type description here.
        shutter_speed (float): TODO: type description here.
        latitude (float): TODO: type description here.
        longitude (float): TODO: type description here.
        altitude (float): TODO: type description here.
        iso_speed_rating (int): TODO: type description here.
        series_timer_id (string): Gets or sets the series timer identifier.
        program_id (string): Gets or sets the program identifier.
        channel_primary_image_tag (string): Gets or sets the channel primary
            image tag.
        start_date (datetime): Gets or sets the start date of the recording,
            in UTC.
        completion_percentage (float): Gets or sets the completion
            percentage.
        is_repeat (bool): Gets or sets a value indicating whether this
            instance is repeat.
        episode_title (string): Gets or sets the episode title.
        channel_type (ChannelTypeEnum): Gets or sets the type of the channel.
        audio (ProgramAudioEnum): Gets or sets the audio.
        is_movie (bool): Gets or sets a value indicating whether this instance
            is movie.
        is_sports (bool): Gets or sets a value indicating whether this
            instance is sports.
        is_series (bool): Gets or sets a value indicating whether this
            instance is series.
        is_live (bool): Gets or sets a value indicating whether this instance
            is live.
        is_news (bool): Gets or sets a value indicating whether this instance
            is news.
        is_kids (bool): Gets or sets a value indicating whether this instance
            is kids.
        is_premiere (bool): Gets or sets a value indicating whether this
            instance is premiere.
        timer_id (string): Gets or sets the timer identifier.
        current_program (BaseItemDto): Gets or sets the current program.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "original_title": "OriginalTitle",
        "server_id": "ServerId",
        "id": "Id",
        "etag": "Etag",
        "source_type": "SourceType",
        "playlist_item_id": "PlaylistItemId",
        "date_created": "DateCreated",
        "date_last_media_added": "DateLastMediaAdded",
        "extra_type": "ExtraType",
        "airs_before_season_number": "AirsBeforeSeasonNumber",
        "airs_after_season_number": "AirsAfterSeasonNumber",
        "airs_before_episode_number": "AirsBeforeEpisodeNumber",
        "can_delete": "CanDelete",
        "can_download": "CanDownload",
        "has_subtitles": "HasSubtitles",
        "preferred_metadata_language": "PreferredMetadataLanguage",
        "preferred_metadata_country_code": "PreferredMetadataCountryCode",
        "supports_sync": "SupportsSync",
        "container": "Container",
        "sort_name": "SortName",
        "forced_sort_name": "ForcedSortName",
        "video_3_d_format": "Video3DFormat",
        "premiere_date": "PremiereDate",
        "external_urls": "ExternalUrls",
        "media_sources": "MediaSources",
        "critic_rating": "CriticRating",
        "production_locations": "ProductionLocations",
        "path": "Path",
        "enable_media_source_display": "EnableMediaSourceDisplay",
        "official_rating": "OfficialRating",
        "custom_rating": "CustomRating",
        "channel_id": "ChannelId",
        "channel_name": "ChannelName",
        "overview": "Overview",
        "taglines": "Taglines",
        "genres": "Genres",
        "community_rating": "CommunityRating",
        "cumulative_run_time_ticks": "CumulativeRunTimeTicks",
        "run_time_ticks": "RunTimeTicks",
        "play_access": "PlayAccess",
        "aspect_ratio": "AspectRatio",
        "production_year": "ProductionYear",
        "is_place_holder": "IsPlaceHolder",
        "number": "Number",
        "channel_number": "ChannelNumber",
        "index_number": "IndexNumber",
        "index_number_end": "IndexNumberEnd",
        "parent_index_number": "ParentIndexNumber",
        "remote_trailers": "RemoteTrailers",
        "provider_ids": "ProviderIds",
        "is_hd": "IsHD",
        "is_folder": "IsFolder",
        "parent_id": "ParentId",
        "mtype": "Type",
        "people": "People",
        "studios": "Studios",
        "genre_items": "GenreItems",
        "parent_logo_item_id": "ParentLogoItemId",
        "parent_backdrop_item_id": "ParentBackdropItemId",
        "parent_backdrop_image_tags": "ParentBackdropImageTags",
        "local_trailer_count": "LocalTrailerCount",
        "user_data": "UserData",
        "recursive_item_count": "RecursiveItemCount",
        "child_count": "ChildCount",
        "series_name": "SeriesName",
        "series_id": "SeriesId",
        "season_id": "SeasonId",
        "special_feature_count": "SpecialFeatureCount",
        "display_preferences_id": "DisplayPreferencesId",
        "status": "Status",
        "air_time": "AirTime",
        "air_days": "AirDays",
        "tags": "Tags",
        "primary_image_aspect_ratio": "PrimaryImageAspectRatio",
        "artists": "Artists",
        "artist_items": "ArtistItems",
        "album": "Album",
        "collection_type": "CollectionType",
        "display_order": "DisplayOrder",
        "album_id": "AlbumId",
        "album_primary_image_tag": "AlbumPrimaryImageTag",
        "series_primary_image_tag": "SeriesPrimaryImageTag",
        "album_artist": "AlbumArtist",
        "album_artists": "AlbumArtists",
        "season_name": "SeasonName",
        "media_streams": "MediaStreams",
        "video_type": "VideoType",
        "part_count": "PartCount",
        "media_source_count": "MediaSourceCount",
        "image_tags": "ImageTags",
        "backdrop_image_tags": "BackdropImageTags",
        "screenshot_image_tags": "ScreenshotImageTags",
        "parent_logo_image_tag": "ParentLogoImageTag",
        "parent_art_item_id": "ParentArtItemId",
        "parent_art_image_tag": "ParentArtImageTag",
        "series_thumb_image_tag": "SeriesThumbImageTag",
        "image_blur_hashes": "ImageBlurHashes",
        "series_studio": "SeriesStudio",
        "parent_thumb_item_id": "ParentThumbItemId",
        "parent_thumb_image_tag": "ParentThumbImageTag",
        "parent_primary_image_item_id": "ParentPrimaryImageItemId",
        "parent_primary_image_tag": "ParentPrimaryImageTag",
        "chapters": "Chapters",
        "location_type": "LocationType",
        "iso_type": "IsoType",
        "media_type": "MediaType",
        "end_date": "EndDate",
        "locked_fields": "LockedFields",
        "trailer_count": "TrailerCount",
        "movie_count": "MovieCount",
        "series_count": "SeriesCount",
        "program_count": "ProgramCount",
        "episode_count": "EpisodeCount",
        "song_count": "SongCount",
        "album_count": "AlbumCount",
        "artist_count": "ArtistCount",
        "music_video_count": "MusicVideoCount",
        "lock_data": "LockData",
        "width": "Width",
        "height": "Height",
        "camera_make": "CameraMake",
        "camera_model": "CameraModel",
        "software": "Software",
        "exposure_time": "ExposureTime",
        "focal_length": "FocalLength",
        "image_orientation": "ImageOrientation",
        "aperture": "Aperture",
        "shutter_speed": "ShutterSpeed",
        "latitude": "Latitude",
        "longitude": "Longitude",
        "altitude": "Altitude",
        "iso_speed_rating": "IsoSpeedRating",
        "series_timer_id": "SeriesTimerId",
        "program_id": "ProgramId",
        "channel_primary_image_tag": "ChannelPrimaryImageTag",
        "start_date": "StartDate",
        "completion_percentage": "CompletionPercentage",
        "is_repeat": "IsRepeat",
        "episode_title": "EpisodeTitle",
        "channel_type": "ChannelType",
        "audio": "Audio",
        "is_movie": "IsMovie",
        "is_sports": "IsSports",
        "is_series": "IsSeries",
        "is_live": "IsLive",
        "is_news": "IsNews",
        "is_kids": "IsKids",
        "is_premiere": "IsPremiere",
        "timer_id": "TimerId",
        "current_program": "CurrentProgram",
    }

    _optionals = [
        "name",
        "original_title",
        "server_id",
        "id",
        "etag",
        "source_type",
        "playlist_item_id",
        "date_created",
        "date_last_media_added",
        "extra_type",
        "airs_before_season_number",
        "airs_after_season_number",
        "airs_before_episode_number",
        "can_delete",
        "can_download",
        "has_subtitles",
        "preferred_metadata_language",
        "preferred_metadata_country_code",
        "supports_sync",
        "container",
        "sort_name",
        "forced_sort_name",
        "video_3_d_format",
        "premiere_date",
        "external_urls",
        "media_sources",
        "critic_rating",
        "production_locations",
        "path",
        "enable_media_source_display",
        "official_rating",
        "custom_rating",
        "channel_id",
        "channel_name",
        "overview",
        "taglines",
        "genres",
        "community_rating",
        "cumulative_run_time_ticks",
        "run_time_ticks",
        "play_access",
        "aspect_ratio",
        "production_year",
        "is_place_holder",
        "number",
        "channel_number",
        "index_number",
        "index_number_end",
        "parent_index_number",
        "remote_trailers",
        "provider_ids",
        "is_hd",
        "is_folder",
        "parent_id",
        "mtype",
        "people",
        "studios",
        "genre_items",
        "parent_logo_item_id",
        "parent_backdrop_item_id",
        "parent_backdrop_image_tags",
        "local_trailer_count",
        "user_data",
        "recursive_item_count",
        "child_count",
        "series_name",
        "series_id",
        "season_id",
        "special_feature_count",
        "display_preferences_id",
        "status",
        "air_time",
        "air_days",
        "tags",
        "primary_image_aspect_ratio",
        "artists",
        "artist_items",
        "album",
        "collection_type",
        "display_order",
        "album_id",
        "album_primary_image_tag",
        "series_primary_image_tag",
        "album_artist",
        "album_artists",
        "season_name",
        "media_streams",
        "video_type",
        "part_count",
        "media_source_count",
        "image_tags",
        "backdrop_image_tags",
        "screenshot_image_tags",
        "parent_logo_image_tag",
        "parent_art_item_id",
        "parent_art_image_tag",
        "series_thumb_image_tag",
        "image_blur_hashes",
        "series_studio",
        "parent_thumb_item_id",
        "parent_thumb_image_tag",
        "parent_primary_image_item_id",
        "parent_primary_image_tag",
        "chapters",
        "location_type",
        "iso_type",
        "media_type",
        "end_date",
        "locked_fields",
        "trailer_count",
        "movie_count",
        "series_count",
        "program_count",
        "episode_count",
        "song_count",
        "album_count",
        "artist_count",
        "music_video_count",
        "lock_data",
        "width",
        "height",
        "camera_make",
        "camera_model",
        "software",
        "exposure_time",
        "focal_length",
        "image_orientation",
        "aperture",
        "shutter_speed",
        "latitude",
        "longitude",
        "altitude",
        "iso_speed_rating",
        "series_timer_id",
        "program_id",
        "channel_primary_image_tag",
        "start_date",
        "completion_percentage",
        "is_repeat",
        "episode_title",
        "channel_type",
        "audio",
        "is_movie",
        "is_sports",
        "is_series",
        "is_live",
        "is_news",
        "is_kids",
        "is_premiere",
        "timer_id",
        "current_program",
    ]

    _nullables = [
        "name",
        "original_title",
        "server_id",
        "etag",
        "source_type",
        "playlist_item_id",
        "date_created",
        "date_last_media_added",
        "extra_type",
        "airs_before_season_number",
        "airs_after_season_number",
        "airs_before_episode_number",
        "can_delete",
        "can_download",
        "has_subtitles",
        "preferred_metadata_language",
        "preferred_metadata_country_code",
        "supports_sync",
        "container",
        "sort_name",
        "forced_sort_name",
        "video_3_d_format",
        "premiere_date",
        "external_urls",
        "media_sources",
        "critic_rating",
        "production_locations",
        "path",
        "enable_media_source_display",
        "official_rating",
        "custom_rating",
        "channel_id",
        "channel_name",
        "overview",
        "taglines",
        "genres",
        "community_rating",
        "cumulative_run_time_ticks",
        "run_time_ticks",
        "play_access",
        "aspect_ratio",
        "production_year",
        "is_place_holder",
        "number",
        "channel_number",
        "index_number",
        "index_number_end",
        "parent_index_number",
        "remote_trailers",
        "provider_ids",
        "is_hd",
        "is_folder",
        "parent_id",
        "people",
        "studios",
        "genre_items",
        "parent_logo_item_id",
        "parent_backdrop_item_id",
        "parent_backdrop_image_tags",
        "local_trailer_count",
        "user_data",
        "recursive_item_count",
        "child_count",
        "series_name",
        "series_id",
        "season_id",
        "special_feature_count",
        "display_preferences_id",
        "status",
        "air_time",
        "air_days",
        "tags",
        "primary_image_aspect_ratio",
        "artists",
        "artist_items",
        "album",
        "collection_type",
        "display_order",
        "album_id",
        "album_primary_image_tag",
        "series_primary_image_tag",
        "album_artist",
        "album_artists",
        "season_name",
        "media_streams",
        "video_type",
        "part_count",
        "media_source_count",
        "backdrop_image_tags",
        "screenshot_image_tags",
        "parent_logo_image_tag",
        "parent_art_item_id",
        "parent_art_image_tag",
        "series_thumb_image_tag",
        "image_blur_hashes",
        "series_studio",
        "parent_thumb_item_id",
        "parent_thumb_image_tag",
        "parent_primary_image_item_id",
        "parent_primary_image_tag",
        "chapters",
        "location_type",
        "iso_type",
        "media_type",
        "end_date",
        "locked_fields",
        "trailer_count",
        "movie_count",
        "series_count",
        "program_count",
        "episode_count",
        "song_count",
        "album_count",
        "artist_count",
        "music_video_count",
        "lock_data",
        "width",
        "height",
        "camera_make",
        "camera_model",
        "software",
        "exposure_time",
        "focal_length",
        "image_orientation",
        "aperture",
        "shutter_speed",
        "latitude",
        "longitude",
        "altitude",
        "iso_speed_rating",
        "series_timer_id",
        "program_id",
        "channel_primary_image_tag",
        "start_date",
        "completion_percentage",
        "is_repeat",
        "episode_title",
        "channel_type",
        "audio",
        "is_movie",
        "is_sports",
        "is_series",
        "is_live",
        "is_news",
        "is_kids",
        "is_premiere",
        "timer_id",
        "current_program",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        original_title=APIHelper.SKIP,
        server_id=APIHelper.SKIP,
        id=APIHelper.SKIP,
        etag=APIHelper.SKIP,
        source_type=APIHelper.SKIP,
        playlist_item_id=APIHelper.SKIP,
        date_created=APIHelper.SKIP,
        date_last_media_added=APIHelper.SKIP,
        extra_type=APIHelper.SKIP,
        airs_before_season_number=APIHelper.SKIP,
        airs_after_season_number=APIHelper.SKIP,
        airs_before_episode_number=APIHelper.SKIP,
        can_delete=APIHelper.SKIP,
        can_download=APIHelper.SKIP,
        has_subtitles=APIHelper.SKIP,
        preferred_metadata_language=APIHelper.SKIP,
        preferred_metadata_country_code=APIHelper.SKIP,
        supports_sync=APIHelper.SKIP,
        container=APIHelper.SKIP,
        sort_name=APIHelper.SKIP,
        forced_sort_name=APIHelper.SKIP,
        video_3_d_format=APIHelper.SKIP,
        premiere_date=APIHelper.SKIP,
        external_urls=APIHelper.SKIP,
        media_sources=APIHelper.SKIP,
        critic_rating=APIHelper.SKIP,
        production_locations=APIHelper.SKIP,
        path=APIHelper.SKIP,
        enable_media_source_display=APIHelper.SKIP,
        official_rating=APIHelper.SKIP,
        custom_rating=APIHelper.SKIP,
        channel_id=APIHelper.SKIP,
        channel_name=APIHelper.SKIP,
        overview=APIHelper.SKIP,
        taglines=APIHelper.SKIP,
        genres=APIHelper.SKIP,
        community_rating=APIHelper.SKIP,
        cumulative_run_time_ticks=APIHelper.SKIP,
        run_time_ticks=APIHelper.SKIP,
        play_access=APIHelper.SKIP,
        aspect_ratio=APIHelper.SKIP,
        production_year=APIHelper.SKIP,
        is_place_holder=APIHelper.SKIP,
        number=APIHelper.SKIP,
        channel_number=APIHelper.SKIP,
        index_number=APIHelper.SKIP,
        index_number_end=APIHelper.SKIP,
        parent_index_number=APIHelper.SKIP,
        remote_trailers=APIHelper.SKIP,
        provider_ids=APIHelper.SKIP,
        is_hd=APIHelper.SKIP,
        is_folder=APIHelper.SKIP,
        parent_id=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        people=APIHelper.SKIP,
        studios=APIHelper.SKIP,
        genre_items=APIHelper.SKIP,
        parent_logo_item_id=APIHelper.SKIP,
        parent_backdrop_item_id=APIHelper.SKIP,
        parent_backdrop_image_tags=APIHelper.SKIP,
        local_trailer_count=APIHelper.SKIP,
        user_data=APIHelper.SKIP,
        recursive_item_count=APIHelper.SKIP,
        child_count=APIHelper.SKIP,
        series_name=APIHelper.SKIP,
        series_id=APIHelper.SKIP,
        season_id=APIHelper.SKIP,
        special_feature_count=APIHelper.SKIP,
        display_preferences_id=APIHelper.SKIP,
        status=APIHelper.SKIP,
        air_time=APIHelper.SKIP,
        air_days=APIHelper.SKIP,
        tags=APIHelper.SKIP,
        primary_image_aspect_ratio=APIHelper.SKIP,
        artists=APIHelper.SKIP,
        artist_items=APIHelper.SKIP,
        album=APIHelper.SKIP,
        collection_type=APIHelper.SKIP,
        display_order=APIHelper.SKIP,
        album_id=APIHelper.SKIP,
        album_primary_image_tag=APIHelper.SKIP,
        series_primary_image_tag=APIHelper.SKIP,
        album_artist=APIHelper.SKIP,
        album_artists=APIHelper.SKIP,
        season_name=APIHelper.SKIP,
        media_streams=APIHelper.SKIP,
        video_type=APIHelper.SKIP,
        part_count=APIHelper.SKIP,
        media_source_count=APIHelper.SKIP,
        image_tags=APIHelper.SKIP,
        backdrop_image_tags=APIHelper.SKIP,
        screenshot_image_tags=APIHelper.SKIP,
        parent_logo_image_tag=APIHelper.SKIP,
        parent_art_item_id=APIHelper.SKIP,
        parent_art_image_tag=APIHelper.SKIP,
        series_thumb_image_tag=APIHelper.SKIP,
        image_blur_hashes=APIHelper.SKIP,
        series_studio=APIHelper.SKIP,
        parent_thumb_item_id=APIHelper.SKIP,
        parent_thumb_image_tag=APIHelper.SKIP,
        parent_primary_image_item_id=APIHelper.SKIP,
        parent_primary_image_tag=APIHelper.SKIP,
        chapters=APIHelper.SKIP,
        location_type=APIHelper.SKIP,
        iso_type=APIHelper.SKIP,
        media_type=APIHelper.SKIP,
        end_date=APIHelper.SKIP,
        locked_fields=APIHelper.SKIP,
        trailer_count=APIHelper.SKIP,
        movie_count=APIHelper.SKIP,
        series_count=APIHelper.SKIP,
        program_count=APIHelper.SKIP,
        episode_count=APIHelper.SKIP,
        song_count=APIHelper.SKIP,
        album_count=APIHelper.SKIP,
        artist_count=APIHelper.SKIP,
        music_video_count=APIHelper.SKIP,
        lock_data=APIHelper.SKIP,
        width=APIHelper.SKIP,
        height=APIHelper.SKIP,
        camera_make=APIHelper.SKIP,
        camera_model=APIHelper.SKIP,
        software=APIHelper.SKIP,
        exposure_time=APIHelper.SKIP,
        focal_length=APIHelper.SKIP,
        image_orientation=APIHelper.SKIP,
        aperture=APIHelper.SKIP,
        shutter_speed=APIHelper.SKIP,
        latitude=APIHelper.SKIP,
        longitude=APIHelper.SKIP,
        altitude=APIHelper.SKIP,
        iso_speed_rating=APIHelper.SKIP,
        series_timer_id=APIHelper.SKIP,
        program_id=APIHelper.SKIP,
        channel_primary_image_tag=APIHelper.SKIP,
        start_date=APIHelper.SKIP,
        completion_percentage=APIHelper.SKIP,
        is_repeat=APIHelper.SKIP,
        episode_title=APIHelper.SKIP,
        channel_type=APIHelper.SKIP,
        audio=APIHelper.SKIP,
        is_movie=APIHelper.SKIP,
        is_sports=APIHelper.SKIP,
        is_series=APIHelper.SKIP,
        is_live=APIHelper.SKIP,
        is_news=APIHelper.SKIP,
        is_kids=APIHelper.SKIP,
        is_premiere=APIHelper.SKIP,
        timer_id=APIHelper.SKIP,
        current_program=APIHelper.SKIP,
    ):
        """Constructor for the BaseItemDto class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if original_title is not APIHelper.SKIP:
            self.original_title = original_title
        if server_id is not APIHelper.SKIP:
            self.server_id = server_id
        if id is not APIHelper.SKIP:
            self.id = id
        if etag is not APIHelper.SKIP:
            self.etag = etag
        if source_type is not APIHelper.SKIP:
            self.source_type = source_type
        if playlist_item_id is not APIHelper.SKIP:
            self.playlist_item_id = playlist_item_id
        if date_created is not APIHelper.SKIP:
            self.date_created = (
                APIHelper.RFC3339DateTime(date_created) if date_created else None
            )
        if date_last_media_added is not APIHelper.SKIP:
            self.date_last_media_added = (
                APIHelper.RFC3339DateTime(date_last_media_added)
                if date_last_media_added
                else None
            )
        if extra_type is not APIHelper.SKIP:
            self.extra_type = extra_type
        if airs_before_season_number is not APIHelper.SKIP:
            self.airs_before_season_number = airs_before_season_number
        if airs_after_season_number is not APIHelper.SKIP:
            self.airs_after_season_number = airs_after_season_number
        if airs_before_episode_number is not APIHelper.SKIP:
            self.airs_before_episode_number = airs_before_episode_number
        if can_delete is not APIHelper.SKIP:
            self.can_delete = can_delete
        if can_download is not APIHelper.SKIP:
            self.can_download = can_download
        if has_subtitles is not APIHelper.SKIP:
            self.has_subtitles = has_subtitles
        if preferred_metadata_language is not APIHelper.SKIP:
            self.preferred_metadata_language = preferred_metadata_language
        if preferred_metadata_country_code is not APIHelper.SKIP:
            self.preferred_metadata_country_code = preferred_metadata_country_code
        if supports_sync is not APIHelper.SKIP:
            self.supports_sync = supports_sync
        if container is not APIHelper.SKIP:
            self.container = container
        if sort_name is not APIHelper.SKIP:
            self.sort_name = sort_name
        if forced_sort_name is not APIHelper.SKIP:
            self.forced_sort_name = forced_sort_name
        if video_3_d_format is not APIHelper.SKIP:
            self.video_3_d_format = video_3_d_format
        if premiere_date is not APIHelper.SKIP:
            self.premiere_date = (
                APIHelper.RFC3339DateTime(premiere_date) if premiere_date else None
            )
        if external_urls is not APIHelper.SKIP:
            self.external_urls = external_urls
        if media_sources is not APIHelper.SKIP:
            self.media_sources = media_sources
        if critic_rating is not APIHelper.SKIP:
            self.critic_rating = critic_rating
        if production_locations is not APIHelper.SKIP:
            self.production_locations = production_locations
        if path is not APIHelper.SKIP:
            self.path = path
        if enable_media_source_display is not APIHelper.SKIP:
            self.enable_media_source_display = enable_media_source_display
        if official_rating is not APIHelper.SKIP:
            self.official_rating = official_rating
        if custom_rating is not APIHelper.SKIP:
            self.custom_rating = custom_rating
        if channel_id is not APIHelper.SKIP:
            self.channel_id = channel_id
        if channel_name is not APIHelper.SKIP:
            self.channel_name = channel_name
        if overview is not APIHelper.SKIP:
            self.overview = overview
        if taglines is not APIHelper.SKIP:
            self.taglines = taglines
        if genres is not APIHelper.SKIP:
            self.genres = genres
        if community_rating is not APIHelper.SKIP:
            self.community_rating = community_rating
        if cumulative_run_time_ticks is not APIHelper.SKIP:
            self.cumulative_run_time_ticks = cumulative_run_time_ticks
        if run_time_ticks is not APIHelper.SKIP:
            self.run_time_ticks = run_time_ticks
        if play_access is not APIHelper.SKIP:
            self.play_access = play_access
        if aspect_ratio is not APIHelper.SKIP:
            self.aspect_ratio = aspect_ratio
        if production_year is not APIHelper.SKIP:
            self.production_year = production_year
        if is_place_holder is not APIHelper.SKIP:
            self.is_place_holder = is_place_holder
        if number is not APIHelper.SKIP:
            self.number = number
        if channel_number is not APIHelper.SKIP:
            self.channel_number = channel_number
        if index_number is not APIHelper.SKIP:
            self.index_number = index_number
        if index_number_end is not APIHelper.SKIP:
            self.index_number_end = index_number_end
        if parent_index_number is not APIHelper.SKIP:
            self.parent_index_number = parent_index_number
        if remote_trailers is not APIHelper.SKIP:
            self.remote_trailers = remote_trailers
        if provider_ids is not APIHelper.SKIP:
            self.provider_ids = provider_ids
        if is_hd is not APIHelper.SKIP:
            self.is_hd = is_hd
        if is_folder is not APIHelper.SKIP:
            self.is_folder = is_folder
        if parent_id is not APIHelper.SKIP:
            self.parent_id = parent_id
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if people is not APIHelper.SKIP:
            self.people = people
        if studios is not APIHelper.SKIP:
            self.studios = studios
        if genre_items is not APIHelper.SKIP:
            self.genre_items = genre_items
        if parent_logo_item_id is not APIHelper.SKIP:
            self.parent_logo_item_id = parent_logo_item_id
        if parent_backdrop_item_id is not APIHelper.SKIP:
            self.parent_backdrop_item_id = parent_backdrop_item_id
        if parent_backdrop_image_tags is not APIHelper.SKIP:
            self.parent_backdrop_image_tags = parent_backdrop_image_tags
        if local_trailer_count is not APIHelper.SKIP:
            self.local_trailer_count = local_trailer_count
        if user_data is not APIHelper.SKIP:
            self.user_data = user_data
        if recursive_item_count is not APIHelper.SKIP:
            self.recursive_item_count = recursive_item_count
        if child_count is not APIHelper.SKIP:
            self.child_count = child_count
        if series_name is not APIHelper.SKIP:
            self.series_name = series_name
        if series_id is not APIHelper.SKIP:
            self.series_id = series_id
        if season_id is not APIHelper.SKIP:
            self.season_id = season_id
        if special_feature_count is not APIHelper.SKIP:
            self.special_feature_count = special_feature_count
        if display_preferences_id is not APIHelper.SKIP:
            self.display_preferences_id = display_preferences_id
        if status is not APIHelper.SKIP:
            self.status = status
        if air_time is not APIHelper.SKIP:
            self.air_time = air_time
        if air_days is not APIHelper.SKIP:
            self.air_days = air_days
        if tags is not APIHelper.SKIP:
            self.tags = tags
        if primary_image_aspect_ratio is not APIHelper.SKIP:
            self.primary_image_aspect_ratio = primary_image_aspect_ratio
        if artists is not APIHelper.SKIP:
            self.artists = artists
        if artist_items is not APIHelper.SKIP:
            self.artist_items = artist_items
        if album is not APIHelper.SKIP:
            self.album = album
        if collection_type is not APIHelper.SKIP:
            self.collection_type = collection_type
        if display_order is not APIHelper.SKIP:
            self.display_order = display_order
        if album_id is not APIHelper.SKIP:
            self.album_id = album_id
        if album_primary_image_tag is not APIHelper.SKIP:
            self.album_primary_image_tag = album_primary_image_tag
        if series_primary_image_tag is not APIHelper.SKIP:
            self.series_primary_image_tag = series_primary_image_tag
        if album_artist is not APIHelper.SKIP:
            self.album_artist = album_artist
        if album_artists is not APIHelper.SKIP:
            self.album_artists = album_artists
        if season_name is not APIHelper.SKIP:
            self.season_name = season_name
        if media_streams is not APIHelper.SKIP:
            self.media_streams = media_streams
        if video_type is not APIHelper.SKIP:
            self.video_type = video_type
        if part_count is not APIHelper.SKIP:
            self.part_count = part_count
        if media_source_count is not APIHelper.SKIP:
            self.media_source_count = media_source_count
        if image_tags is not APIHelper.SKIP:
            self.image_tags = image_tags
        if backdrop_image_tags is not APIHelper.SKIP:
            self.backdrop_image_tags = backdrop_image_tags
        if screenshot_image_tags is not APIHelper.SKIP:
            self.screenshot_image_tags = screenshot_image_tags
        if parent_logo_image_tag is not APIHelper.SKIP:
            self.parent_logo_image_tag = parent_logo_image_tag
        if parent_art_item_id is not APIHelper.SKIP:
            self.parent_art_item_id = parent_art_item_id
        if parent_art_image_tag is not APIHelper.SKIP:
            self.parent_art_image_tag = parent_art_image_tag
        if series_thumb_image_tag is not APIHelper.SKIP:
            self.series_thumb_image_tag = series_thumb_image_tag
        if image_blur_hashes is not APIHelper.SKIP:
            self.image_blur_hashes = image_blur_hashes
        if series_studio is not APIHelper.SKIP:
            self.series_studio = series_studio
        if parent_thumb_item_id is not APIHelper.SKIP:
            self.parent_thumb_item_id = parent_thumb_item_id
        if parent_thumb_image_tag is not APIHelper.SKIP:
            self.parent_thumb_image_tag = parent_thumb_image_tag
        if parent_primary_image_item_id is not APIHelper.SKIP:
            self.parent_primary_image_item_id = parent_primary_image_item_id
        if parent_primary_image_tag is not APIHelper.SKIP:
            self.parent_primary_image_tag = parent_primary_image_tag
        if chapters is not APIHelper.SKIP:
            self.chapters = chapters
        if location_type is not APIHelper.SKIP:
            self.location_type = location_type
        if iso_type is not APIHelper.SKIP:
            self.iso_type = iso_type
        if media_type is not APIHelper.SKIP:
            self.media_type = media_type
        if end_date is not APIHelper.SKIP:
            self.end_date = APIHelper.RFC3339DateTime(end_date) if end_date else None
        if locked_fields is not APIHelper.SKIP:
            self.locked_fields = locked_fields
        if trailer_count is not APIHelper.SKIP:
            self.trailer_count = trailer_count
        if movie_count is not APIHelper.SKIP:
            self.movie_count = movie_count
        if series_count is not APIHelper.SKIP:
            self.series_count = series_count
        if program_count is not APIHelper.SKIP:
            self.program_count = program_count
        if episode_count is not APIHelper.SKIP:
            self.episode_count = episode_count
        if song_count is not APIHelper.SKIP:
            self.song_count = song_count
        if album_count is not APIHelper.SKIP:
            self.album_count = album_count
        if artist_count is not APIHelper.SKIP:
            self.artist_count = artist_count
        if music_video_count is not APIHelper.SKIP:
            self.music_video_count = music_video_count
        if lock_data is not APIHelper.SKIP:
            self.lock_data = lock_data
        if width is not APIHelper.SKIP:
            self.width = width
        if height is not APIHelper.SKIP:
            self.height = height
        if camera_make is not APIHelper.SKIP:
            self.camera_make = camera_make
        if camera_model is not APIHelper.SKIP:
            self.camera_model = camera_model
        if software is not APIHelper.SKIP:
            self.software = software
        if exposure_time is not APIHelper.SKIP:
            self.exposure_time = exposure_time
        if focal_length is not APIHelper.SKIP:
            self.focal_length = focal_length
        if image_orientation is not APIHelper.SKIP:
            self.image_orientation = image_orientation
        if aperture is not APIHelper.SKIP:
            self.aperture = aperture
        if shutter_speed is not APIHelper.SKIP:
            self.shutter_speed = shutter_speed
        if latitude is not APIHelper.SKIP:
            self.latitude = latitude
        if longitude is not APIHelper.SKIP:
            self.longitude = longitude
        if altitude is not APIHelper.SKIP:
            self.altitude = altitude
        if iso_speed_rating is not APIHelper.SKIP:
            self.iso_speed_rating = iso_speed_rating
        if series_timer_id is not APIHelper.SKIP:
            self.series_timer_id = series_timer_id
        if program_id is not APIHelper.SKIP:
            self.program_id = program_id
        if channel_primary_image_tag is not APIHelper.SKIP:
            self.channel_primary_image_tag = channel_primary_image_tag
        if start_date is not APIHelper.SKIP:
            self.start_date = (
                APIHelper.RFC3339DateTime(start_date) if start_date else None
            )
        if completion_percentage is not APIHelper.SKIP:
            self.completion_percentage = completion_percentage
        if is_repeat is not APIHelper.SKIP:
            self.is_repeat = is_repeat
        if episode_title is not APIHelper.SKIP:
            self.episode_title = episode_title
        if channel_type is not APIHelper.SKIP:
            self.channel_type = channel_type
        if audio is not APIHelper.SKIP:
            self.audio = audio
        if is_movie is not APIHelper.SKIP:
            self.is_movie = is_movie
        if is_sports is not APIHelper.SKIP:
            self.is_sports = is_sports
        if is_series is not APIHelper.SKIP:
            self.is_series = is_series
        if is_live is not APIHelper.SKIP:
            self.is_live = is_live
        if is_news is not APIHelper.SKIP:
            self.is_news = is_news
        if is_kids is not APIHelper.SKIP:
            self.is_kids = is_kids
        if is_premiere is not APIHelper.SKIP:
            self.is_premiere = is_premiere
        if timer_id is not APIHelper.SKIP:
            self.timer_id = timer_id
        if current_program is not APIHelper.SKIP:
            self.current_program = current_program

    @classmethod
    def from_dictionary(cls, dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        original_title = (
            dictionary.get("OriginalTitle")
            if "OriginalTitle" in dictionary.keys()
            else APIHelper.SKIP
        )
        server_id = (
            dictionary.get("ServerId")
            if "ServerId" in dictionary.keys()
            else APIHelper.SKIP
        )
        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        etag = dictionary.get("Etag") if "Etag" in dictionary.keys() else APIHelper.SKIP
        source_type = (
            dictionary.get("SourceType")
            if "SourceType" in dictionary.keys()
            else APIHelper.SKIP
        )
        playlist_item_id = (
            dictionary.get("PlaylistItemId")
            if "PlaylistItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "DateCreated" in dictionary.keys():
            date_created = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("DateCreated")
                ).datetime
                if dictionary.get("DateCreated")
                else None
            )
        else:
            date_created = APIHelper.SKIP
        if "DateLastMediaAdded" in dictionary.keys():
            date_last_media_added = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("DateLastMediaAdded")
                ).datetime
                if dictionary.get("DateLastMediaAdded")
                else None
            )
        else:
            date_last_media_added = APIHelper.SKIP
        extra_type = (
            dictionary.get("ExtraType")
            if "ExtraType" in dictionary.keys()
            else APIHelper.SKIP
        )
        airs_before_season_number = (
            dictionary.get("AirsBeforeSeasonNumber")
            if "AirsBeforeSeasonNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        airs_after_season_number = (
            dictionary.get("AirsAfterSeasonNumber")
            if "AirsAfterSeasonNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        airs_before_episode_number = (
            dictionary.get("AirsBeforeEpisodeNumber")
            if "AirsBeforeEpisodeNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        can_delete = (
            dictionary.get("CanDelete")
            if "CanDelete" in dictionary.keys()
            else APIHelper.SKIP
        )
        can_download = (
            dictionary.get("CanDownload")
            if "CanDownload" in dictionary.keys()
            else APIHelper.SKIP
        )
        has_subtitles = (
            dictionary.get("HasSubtitles")
            if "HasSubtitles" in dictionary.keys()
            else APIHelper.SKIP
        )
        preferred_metadata_language = (
            dictionary.get("PreferredMetadataLanguage")
            if "PreferredMetadataLanguage" in dictionary.keys()
            else APIHelper.SKIP
        )
        preferred_metadata_country_code = (
            dictionary.get("PreferredMetadataCountryCode")
            if "PreferredMetadataCountryCode" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_sync = (
            dictionary.get("SupportsSync")
            if "SupportsSync" in dictionary.keys()
            else APIHelper.SKIP
        )
        container = (
            dictionary.get("Container")
            if "Container" in dictionary.keys()
            else APIHelper.SKIP
        )
        sort_name = (
            dictionary.get("SortName")
            if "SortName" in dictionary.keys()
            else APIHelper.SKIP
        )
        forced_sort_name = (
            dictionary.get("ForcedSortName")
            if "ForcedSortName" in dictionary.keys()
            else APIHelper.SKIP
        )
        video_3_d_format = (
            dictionary.get("Video3DFormat")
            if "Video3DFormat" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "PremiereDate" in dictionary.keys():
            premiere_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("PremiereDate")
                ).datetime
                if dictionary.get("PremiereDate")
                else None
            )
        else:
            premiere_date = APIHelper.SKIP
        if "ExternalUrls" in dictionary.keys():
            external_urls = (
                [ExternalUrl.from_dictionary(x) for x in dictionary.get("ExternalUrls")]
                if dictionary.get("ExternalUrls")
                else None
            )
        else:
            external_urls = APIHelper.SKIP
        if "MediaSources" in dictionary.keys():
            media_sources = (
                [
                    MediaSourceInfo.from_dictionary(x)
                    for x in dictionary.get("MediaSources")
                ]
                if dictionary.get("MediaSources")
                else None
            )
        else:
            media_sources = APIHelper.SKIP
        critic_rating = (
            dictionary.get("CriticRating")
            if "CriticRating" in dictionary.keys()
            else APIHelper.SKIP
        )
        production_locations = (
            dictionary.get("ProductionLocations")
            if "ProductionLocations" in dictionary.keys()
            else APIHelper.SKIP
        )
        path = dictionary.get("Path") if "Path" in dictionary.keys() else APIHelper.SKIP
        enable_media_source_display = (
            dictionary.get("EnableMediaSourceDisplay")
            if "EnableMediaSourceDisplay" in dictionary.keys()
            else APIHelper.SKIP
        )
        official_rating = (
            dictionary.get("OfficialRating")
            if "OfficialRating" in dictionary.keys()
            else APIHelper.SKIP
        )
        custom_rating = (
            dictionary.get("CustomRating")
            if "CustomRating" in dictionary.keys()
            else APIHelper.SKIP
        )
        channel_id = (
            dictionary.get("ChannelId")
            if "ChannelId" in dictionary.keys()
            else APIHelper.SKIP
        )
        channel_name = (
            dictionary.get("ChannelName")
            if "ChannelName" in dictionary.keys()
            else APIHelper.SKIP
        )
        overview = (
            dictionary.get("Overview")
            if "Overview" in dictionary.keys()
            else APIHelper.SKIP
        )
        taglines = (
            dictionary.get("Taglines")
            if "Taglines" in dictionary.keys()
            else APIHelper.SKIP
        )
        genres = (
            dictionary.get("Genres")
            if "Genres" in dictionary.keys()
            else APIHelper.SKIP
        )
        community_rating = (
            dictionary.get("CommunityRating")
            if "CommunityRating" in dictionary.keys()
            else APIHelper.SKIP
        )
        cumulative_run_time_ticks = (
            dictionary.get("CumulativeRunTimeTicks")
            if "CumulativeRunTimeTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        run_time_ticks = (
            dictionary.get("RunTimeTicks")
            if "RunTimeTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        play_access = (
            dictionary.get("PlayAccess")
            if "PlayAccess" in dictionary.keys()
            else APIHelper.SKIP
        )
        aspect_ratio = (
            dictionary.get("AspectRatio")
            if "AspectRatio" in dictionary.keys()
            else APIHelper.SKIP
        )
        production_year = (
            dictionary.get("ProductionYear")
            if "ProductionYear" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_place_holder = (
            dictionary.get("IsPlaceHolder")
            if "IsPlaceHolder" in dictionary.keys()
            else APIHelper.SKIP
        )
        number = (
            dictionary.get("Number")
            if "Number" in dictionary.keys()
            else APIHelper.SKIP
        )
        channel_number = (
            dictionary.get("ChannelNumber")
            if "ChannelNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        index_number = (
            dictionary.get("IndexNumber")
            if "IndexNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        index_number_end = (
            dictionary.get("IndexNumberEnd")
            if "IndexNumberEnd" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_index_number = (
            dictionary.get("ParentIndexNumber")
            if "ParentIndexNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "RemoteTrailers" in dictionary.keys():
            remote_trailers = (
                [MediaUrl.from_dictionary(x) for x in dictionary.get("RemoteTrailers")]
                if dictionary.get("RemoteTrailers")
                else None
            )
        else:
            remote_trailers = APIHelper.SKIP
        provider_ids = (
            dictionary.get("ProviderIds")
            if "ProviderIds" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_hd = (
            dictionary.get("IsHD") if "IsHD" in dictionary.keys() else APIHelper.SKIP
        )
        is_folder = (
            dictionary.get("IsFolder")
            if "IsFolder" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_id = (
            dictionary.get("ParentId")
            if "ParentId" in dictionary.keys()
            else APIHelper.SKIP
        )
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        if "People" in dictionary.keys():
            people = (
                [BaseItemPerson.from_dictionary(x) for x in dictionary.get("People")]
                if dictionary.get("People")
                else None
            )
        else:
            people = APIHelper.SKIP
        if "Studios" in dictionary.keys():
            studios = (
                [NameGuidPair.from_dictionary(x) for x in dictionary.get("Studios")]
                if dictionary.get("Studios")
                else None
            )
        else:
            studios = APIHelper.SKIP
        if "GenreItems" in dictionary.keys():
            genre_items = (
                [NameGuidPair.from_dictionary(x) for x in dictionary.get("GenreItems")]
                if dictionary.get("GenreItems")
                else None
            )
        else:
            genre_items = APIHelper.SKIP
        parent_logo_item_id = (
            dictionary.get("ParentLogoItemId")
            if "ParentLogoItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_backdrop_item_id = (
            dictionary.get("ParentBackdropItemId")
            if "ParentBackdropItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_backdrop_image_tags = (
            dictionary.get("ParentBackdropImageTags")
            if "ParentBackdropImageTags" in dictionary.keys()
            else APIHelper.SKIP
        )
        local_trailer_count = (
            dictionary.get("LocalTrailerCount")
            if "LocalTrailerCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "UserData" in dictionary.keys():
            user_data = (
                UserItemDataDto.from_dictionary(dictionary.get("UserData"))
                if dictionary.get("UserData")
                else None
            )
        else:
            user_data = APIHelper.SKIP
        recursive_item_count = (
            dictionary.get("RecursiveItemCount")
            if "RecursiveItemCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        child_count = (
            dictionary.get("ChildCount")
            if "ChildCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        series_name = (
            dictionary.get("SeriesName")
            if "SeriesName" in dictionary.keys()
            else APIHelper.SKIP
        )
        series_id = (
            dictionary.get("SeriesId")
            if "SeriesId" in dictionary.keys()
            else APIHelper.SKIP
        )
        season_id = (
            dictionary.get("SeasonId")
            if "SeasonId" in dictionary.keys()
            else APIHelper.SKIP
        )
        special_feature_count = (
            dictionary.get("SpecialFeatureCount")
            if "SpecialFeatureCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        display_preferences_id = (
            dictionary.get("DisplayPreferencesId")
            if "DisplayPreferencesId" in dictionary.keys()
            else APIHelper.SKIP
        )
        status = (
            dictionary.get("Status")
            if "Status" in dictionary.keys()
            else APIHelper.SKIP
        )
        air_time = (
            dictionary.get("AirTime")
            if "AirTime" in dictionary.keys()
            else APIHelper.SKIP
        )
        air_days = (
            dictionary.get("AirDays")
            if "AirDays" in dictionary.keys()
            else APIHelper.SKIP
        )
        tags = dictionary.get("Tags") if "Tags" in dictionary.keys() else APIHelper.SKIP
        primary_image_aspect_ratio = (
            dictionary.get("PrimaryImageAspectRatio")
            if "PrimaryImageAspectRatio" in dictionary.keys()
            else APIHelper.SKIP
        )
        artists = (
            dictionary.get("Artists")
            if "Artists" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "ArtistItems" in dictionary.keys():
            artist_items = (
                [NameGuidPair.from_dictionary(x) for x in dictionary.get("ArtistItems")]
                if dictionary.get("ArtistItems")
                else None
            )
        else:
            artist_items = APIHelper.SKIP
        album = (
            dictionary.get("Album") if "Album" in dictionary.keys() else APIHelper.SKIP
        )
        collection_type = (
            dictionary.get("CollectionType")
            if "CollectionType" in dictionary.keys()
            else APIHelper.SKIP
        )
        display_order = (
            dictionary.get("DisplayOrder")
            if "DisplayOrder" in dictionary.keys()
            else APIHelper.SKIP
        )
        album_id = (
            dictionary.get("AlbumId")
            if "AlbumId" in dictionary.keys()
            else APIHelper.SKIP
        )
        album_primary_image_tag = (
            dictionary.get("AlbumPrimaryImageTag")
            if "AlbumPrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        series_primary_image_tag = (
            dictionary.get("SeriesPrimaryImageTag")
            if "SeriesPrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        album_artist = (
            dictionary.get("AlbumArtist")
            if "AlbumArtist" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "AlbumArtists" in dictionary.keys():
            album_artists = (
                [
                    NameGuidPair.from_dictionary(x)
                    for x in dictionary.get("AlbumArtists")
                ]
                if dictionary.get("AlbumArtists")
                else None
            )
        else:
            album_artists = APIHelper.SKIP
        season_name = (
            dictionary.get("SeasonName")
            if "SeasonName" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "MediaStreams" in dictionary.keys():
            media_streams = (
                [MediaStream.from_dictionary(x) for x in dictionary.get("MediaStreams")]
                if dictionary.get("MediaStreams")
                else None
            )
        else:
            media_streams = APIHelper.SKIP
        video_type = (
            dictionary.get("VideoType")
            if "VideoType" in dictionary.keys()
            else APIHelper.SKIP
        )
        part_count = (
            dictionary.get("PartCount")
            if "PartCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        media_source_count = (
            dictionary.get("MediaSourceCount")
            if "MediaSourceCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        image_tags = (
            dictionary.get("ImageTags")
            if dictionary.get("ImageTags")
            else APIHelper.SKIP
        )
        backdrop_image_tags = (
            dictionary.get("BackdropImageTags")
            if "BackdropImageTags" in dictionary.keys()
            else APIHelper.SKIP
        )
        screenshot_image_tags = (
            dictionary.get("ScreenshotImageTags")
            if "ScreenshotImageTags" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_logo_image_tag = (
            dictionary.get("ParentLogoImageTag")
            if "ParentLogoImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_art_item_id = (
            dictionary.get("ParentArtItemId")
            if "ParentArtItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_art_image_tag = (
            dictionary.get("ParentArtImageTag")
            if "ParentArtImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        series_thumb_image_tag = (
            dictionary.get("SeriesThumbImageTag")
            if "SeriesThumbImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "ImageBlurHashes" in dictionary.keys():
            image_blur_hashes = (
                ImageBlurHashes1.from_dictionary(dictionary.get("ImageBlurHashes"))
                if dictionary.get("ImageBlurHashes")
                else None
            )
        else:
            image_blur_hashes = APIHelper.SKIP
        series_studio = (
            dictionary.get("SeriesStudio")
            if "SeriesStudio" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_thumb_item_id = (
            dictionary.get("ParentThumbItemId")
            if "ParentThumbItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_thumb_image_tag = (
            dictionary.get("ParentThumbImageTag")
            if "ParentThumbImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_primary_image_item_id = (
            dictionary.get("ParentPrimaryImageItemId")
            if "ParentPrimaryImageItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_primary_image_tag = (
            dictionary.get("ParentPrimaryImageTag")
            if "ParentPrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "Chapters" in dictionary.keys():
            chapters = (
                [ChapterInfo.from_dictionary(x) for x in dictionary.get("Chapters")]
                if dictionary.get("Chapters")
                else None
            )
        else:
            chapters = APIHelper.SKIP
        location_type = (
            dictionary.get("LocationType")
            if "LocationType" in dictionary.keys()
            else APIHelper.SKIP
        )
        iso_type = (
            dictionary.get("IsoType")
            if "IsoType" in dictionary.keys()
            else APIHelper.SKIP
        )
        media_type = (
            dictionary.get("MediaType")
            if "MediaType" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "EndDate" in dictionary.keys():
            end_date = (
                APIHelper.RFC3339DateTime.from_value(dictionary.get("EndDate")).datetime
                if dictionary.get("EndDate")
                else None
            )
        else:
            end_date = APIHelper.SKIP
        locked_fields = (
            dictionary.get("LockedFields")
            if "LockedFields" in dictionary.keys()
            else APIHelper.SKIP
        )
        trailer_count = (
            dictionary.get("TrailerCount")
            if "TrailerCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        movie_count = (
            dictionary.get("MovieCount")
            if "MovieCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        series_count = (
            dictionary.get("SeriesCount")
            if "SeriesCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        program_count = (
            dictionary.get("ProgramCount")
            if "ProgramCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        episode_count = (
            dictionary.get("EpisodeCount")
            if "EpisodeCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        song_count = (
            dictionary.get("SongCount")
            if "SongCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        album_count = (
            dictionary.get("AlbumCount")
            if "AlbumCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        artist_count = (
            dictionary.get("ArtistCount")
            if "ArtistCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        music_video_count = (
            dictionary.get("MusicVideoCount")
            if "MusicVideoCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        lock_data = (
            dictionary.get("LockData")
            if "LockData" in dictionary.keys()
            else APIHelper.SKIP
        )
        width = (
            dictionary.get("Width") if "Width" in dictionary.keys() else APIHelper.SKIP
        )
        height = (
            dictionary.get("Height")
            if "Height" in dictionary.keys()
            else APIHelper.SKIP
        )
        camera_make = (
            dictionary.get("CameraMake")
            if "CameraMake" in dictionary.keys()
            else APIHelper.SKIP
        )
        camera_model = (
            dictionary.get("CameraModel")
            if "CameraModel" in dictionary.keys()
            else APIHelper.SKIP
        )
        software = (
            dictionary.get("Software")
            if "Software" in dictionary.keys()
            else APIHelper.SKIP
        )
        exposure_time = (
            dictionary.get("ExposureTime")
            if "ExposureTime" in dictionary.keys()
            else APIHelper.SKIP
        )
        focal_length = (
            dictionary.get("FocalLength")
            if "FocalLength" in dictionary.keys()
            else APIHelper.SKIP
        )
        image_orientation = (
            dictionary.get("ImageOrientation")
            if "ImageOrientation" in dictionary.keys()
            else APIHelper.SKIP
        )
        aperture = (
            dictionary.get("Aperture")
            if "Aperture" in dictionary.keys()
            else APIHelper.SKIP
        )
        shutter_speed = (
            dictionary.get("ShutterSpeed")
            if "ShutterSpeed" in dictionary.keys()
            else APIHelper.SKIP
        )
        latitude = (
            dictionary.get("Latitude")
            if "Latitude" in dictionary.keys()
            else APIHelper.SKIP
        )
        longitude = (
            dictionary.get("Longitude")
            if "Longitude" in dictionary.keys()
            else APIHelper.SKIP
        )
        altitude = (
            dictionary.get("Altitude")
            if "Altitude" in dictionary.keys()
            else APIHelper.SKIP
        )
        iso_speed_rating = (
            dictionary.get("IsoSpeedRating")
            if "IsoSpeedRating" in dictionary.keys()
            else APIHelper.SKIP
        )
        series_timer_id = (
            dictionary.get("SeriesTimerId")
            if "SeriesTimerId" in dictionary.keys()
            else APIHelper.SKIP
        )
        program_id = (
            dictionary.get("ProgramId")
            if "ProgramId" in dictionary.keys()
            else APIHelper.SKIP
        )
        channel_primary_image_tag = (
            dictionary.get("ChannelPrimaryImageTag")
            if "ChannelPrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "StartDate" in dictionary.keys():
            start_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("StartDate")
                ).datetime
                if dictionary.get("StartDate")
                else None
            )
        else:
            start_date = APIHelper.SKIP
        completion_percentage = (
            dictionary.get("CompletionPercentage")
            if "CompletionPercentage" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_repeat = (
            dictionary.get("IsRepeat")
            if "IsRepeat" in dictionary.keys()
            else APIHelper.SKIP
        )
        episode_title = (
            dictionary.get("EpisodeTitle")
            if "EpisodeTitle" in dictionary.keys()
            else APIHelper.SKIP
        )
        channel_type = (
            dictionary.get("ChannelType")
            if "ChannelType" in dictionary.keys()
            else APIHelper.SKIP
        )
        audio = (
            dictionary.get("Audio") if "Audio" in dictionary.keys() else APIHelper.SKIP
        )
        is_movie = (
            dictionary.get("IsMovie")
            if "IsMovie" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_sports = (
            dictionary.get("IsSports")
            if "IsSports" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_series = (
            dictionary.get("IsSeries")
            if "IsSeries" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_live = (
            dictionary.get("IsLive")
            if "IsLive" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_news = (
            dictionary.get("IsNews")
            if "IsNews" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_kids = (
            dictionary.get("IsKids")
            if "IsKids" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_premiere = (
            dictionary.get("IsPremiere")
            if "IsPremiere" in dictionary.keys()
            else APIHelper.SKIP
        )
        timer_id = (
            dictionary.get("TimerId")
            if "TimerId" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "CurrentProgram" in dictionary.keys():
            current_program = (
                BaseItemDto.from_dictionary(dictionary.get("CurrentProgram"))
                if dictionary.get("CurrentProgram")
                else None
            )
        else:
            current_program = APIHelper.SKIP
        # Return an object of this model
        return cls(
            name,
            original_title,
            server_id,
            id,
            etag,
            source_type,
            playlist_item_id,
            date_created,
            date_last_media_added,
            extra_type,
            airs_before_season_number,
            airs_after_season_number,
            airs_before_episode_number,
            can_delete,
            can_download,
            has_subtitles,
            preferred_metadata_language,
            preferred_metadata_country_code,
            supports_sync,
            container,
            sort_name,
            forced_sort_name,
            video_3_d_format,
            premiere_date,
            external_urls,
            media_sources,
            critic_rating,
            production_locations,
            path,
            enable_media_source_display,
            official_rating,
            custom_rating,
            channel_id,
            channel_name,
            overview,
            taglines,
            genres,
            community_rating,
            cumulative_run_time_ticks,
            run_time_ticks,
            play_access,
            aspect_ratio,
            production_year,
            is_place_holder,
            number,
            channel_number,
            index_number,
            index_number_end,
            parent_index_number,
            remote_trailers,
            provider_ids,
            is_hd,
            is_folder,
            parent_id,
            mtype,
            people,
            studios,
            genre_items,
            parent_logo_item_id,
            parent_backdrop_item_id,
            parent_backdrop_image_tags,
            local_trailer_count,
            user_data,
            recursive_item_count,
            child_count,
            series_name,
            series_id,
            season_id,
            special_feature_count,
            display_preferences_id,
            status,
            air_time,
            air_days,
            tags,
            primary_image_aspect_ratio,
            artists,
            artist_items,
            album,
            collection_type,
            display_order,
            album_id,
            album_primary_image_tag,
            series_primary_image_tag,
            album_artist,
            album_artists,
            season_name,
            media_streams,
            video_type,
            part_count,
            media_source_count,
            image_tags,
            backdrop_image_tags,
            screenshot_image_tags,
            parent_logo_image_tag,
            parent_art_item_id,
            parent_art_image_tag,
            series_thumb_image_tag,
            image_blur_hashes,
            series_studio,
            parent_thumb_item_id,
            parent_thumb_image_tag,
            parent_primary_image_item_id,
            parent_primary_image_tag,
            chapters,
            location_type,
            iso_type,
            media_type,
            end_date,
            locked_fields,
            trailer_count,
            movie_count,
            series_count,
            program_count,
            episode_count,
            song_count,
            album_count,
            artist_count,
            music_video_count,
            lock_data,
            width,
            height,
            camera_make,
            camera_model,
            software,
            exposure_time,
            focal_length,
            image_orientation,
            aperture,
            shutter_speed,
            latitude,
            longitude,
            altitude,
            iso_speed_rating,
            series_timer_id,
            program_id,
            channel_primary_image_tag,
            start_date,
            completion_percentage,
            is_repeat,
            episode_title,
            channel_type,
            audio,
            is_movie,
            is_sports,
            is_series,
            is_live,
            is_news,
            is_kids,
            is_premiere,
            timer_id,
            current_program,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        original_title = XmlUtilities.value_from_xml_element(
            root.find("OriginalTitle"), str
        )
        server_id = XmlUtilities.value_from_xml_element(root.find("ServerId"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        etag = XmlUtilities.value_from_xml_element(root.find("Etag"), str)
        source_type = XmlUtilities.value_from_xml_element(root.find("SourceType"), str)
        playlist_item_id = XmlUtilities.value_from_xml_element(
            root.find("PlaylistItemId"), str
        )
        date_created = XmlUtilities.value_from_xml_element(
            root.find("DateCreated"), APIHelper.RFC3339DateTime
        )
        date_last_media_added = XmlUtilities.value_from_xml_element(
            root.find("DateLastMediaAdded"), APIHelper.RFC3339DateTime
        )
        extra_type = XmlUtilities.value_from_xml_element(root.find("ExtraType"), str)
        airs_before_season_number = XmlUtilities.value_from_xml_element(
            root.find("AirsBeforeSeasonNumber"), int
        )
        airs_after_season_number = XmlUtilities.value_from_xml_element(
            root.find("AirsAfterSeasonNumber"), int
        )
        airs_before_episode_number = XmlUtilities.value_from_xml_element(
            root.find("AirsBeforeEpisodeNumber"), int
        )
        can_delete = XmlUtilities.value_from_xml_element(root.find("CanDelete"), bool)
        can_download = XmlUtilities.value_from_xml_element(
            root.find("CanDownload"), bool
        )
        has_subtitles = XmlUtilities.value_from_xml_element(
            root.find("HasSubtitles"), bool
        )
        preferred_metadata_language = XmlUtilities.value_from_xml_element(
            root.find("PreferredMetadataLanguage"), str
        )
        preferred_metadata_country_code = XmlUtilities.value_from_xml_element(
            root.find("PreferredMetadataCountryCode"), str
        )
        supports_sync = XmlUtilities.value_from_xml_element(
            root.find("SupportsSync"), bool
        )
        container = XmlUtilities.value_from_xml_element(root.find("Container"), str)
        sort_name = XmlUtilities.value_from_xml_element(root.find("SortName"), str)
        forced_sort_name = XmlUtilities.value_from_xml_element(
            root.find("ForcedSortName"), str
        )
        video_3_d_format = XmlUtilities.value_from_xml_element(
            root.find("Video3DFormat"), str
        )
        premiere_date = XmlUtilities.value_from_xml_element(
            root.find("PremiereDate"), APIHelper.RFC3339DateTime
        )
        external_urls = XmlUtilities.list_from_xml_element(
            root, "ExternalUrl", ExternalUrl
        )
        media_sources = XmlUtilities.list_from_xml_element(
            root, "MediaSourceInfo", MediaSourceInfo
        )
        critic_rating = XmlUtilities.value_from_xml_element(
            root.find("CriticRating"), float
        )
        production_locations = XmlUtilities.list_from_xml_element(
            root, "ProductionLocations", str
        )
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)
        enable_media_source_display = XmlUtilities.value_from_xml_element(
            root.find("EnableMediaSourceDisplay"), bool
        )
        official_rating = XmlUtilities.value_from_xml_element(
            root.find("OfficialRating"), str
        )
        custom_rating = XmlUtilities.value_from_xml_element(
            root.find("CustomRating"), str
        )
        channel_id = XmlUtilities.value_from_xml_element(root.find("ChannelId"), str)
        channel_name = XmlUtilities.value_from_xml_element(
            root.find("ChannelName"), str
        )
        overview = XmlUtilities.value_from_xml_element(root.find("Overview"), str)
        taglines = XmlUtilities.list_from_xml_element(root, "Taglines", str)
        genres = XmlUtilities.list_from_xml_element(root, "Genres", str)
        community_rating = XmlUtilities.value_from_xml_element(
            root.find("CommunityRating"), float
        )
        cumulative_run_time_ticks = XmlUtilities.value_from_xml_element(
            root.find("CumulativeRunTimeTicks"), int
        )
        run_time_ticks = XmlUtilities.value_from_xml_element(
            root.find("RunTimeTicks"), int
        )
        play_access = XmlUtilities.value_from_xml_element(root.find("PlayAccess"), str)
        aspect_ratio = XmlUtilities.value_from_xml_element(
            root.find("AspectRatio"), str
        )
        production_year = XmlUtilities.value_from_xml_element(
            root.find("ProductionYear"), int
        )
        is_place_holder = XmlUtilities.value_from_xml_element(
            root.find("IsPlaceHolder"), bool
        )
        number = XmlUtilities.value_from_xml_element(root.find("Number"), str)
        channel_number = XmlUtilities.value_from_xml_element(
            root.find("ChannelNumber"), str
        )
        index_number = XmlUtilities.value_from_xml_element(
            root.find("IndexNumber"), int
        )
        index_number_end = XmlUtilities.value_from_xml_element(
            root.find("IndexNumberEnd"), int
        )
        parent_index_number = XmlUtilities.value_from_xml_element(
            root.find("ParentIndexNumber"), int
        )
        remote_trailers = XmlUtilities.list_from_xml_element(root, "MediaUrl", MediaUrl)
        provider_ids = XmlUtilities.dict_from_xml_element(
            root.find("ProviderIds"), dict
        )

        is_hd = XmlUtilities.value_from_xml_element(root.find("IsHD"), bool)
        is_folder = XmlUtilities.value_from_xml_element(root.find("IsFolder"), bool)
        parent_id = XmlUtilities.value_from_xml_element(root.find("ParentId"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        people = XmlUtilities.list_from_xml_element(
            root, "BaseItemPerson", BaseItemPerson
        )
        studios = XmlUtilities.list_from_xml_element(root, "NameGuidPair", NameGuidPair)
        genre_items = XmlUtilities.list_from_xml_element(
            root, "NameGuidPair", NameGuidPair
        )
        parent_logo_item_id = XmlUtilities.value_from_xml_element(
            root.find("ParentLogoItemId"), str
        )
        parent_backdrop_item_id = XmlUtilities.value_from_xml_element(
            root.find("ParentBackdropItemId"), str
        )
        parent_backdrop_image_tags = XmlUtilities.list_from_xml_element(
            root, "ParentBackdropImageTags", str
        )
        local_trailer_count = XmlUtilities.value_from_xml_element(
            root.find("LocalTrailerCount"), int
        )
        user_data = XmlUtilities.value_from_xml_element(
            root.find("UserItemDataDto"), UserItemDataDto
        )
        recursive_item_count = XmlUtilities.value_from_xml_element(
            root.find("RecursiveItemCount"), int
        )
        child_count = XmlUtilities.value_from_xml_element(root.find("ChildCount"), int)
        series_name = XmlUtilities.value_from_xml_element(root.find("SeriesName"), str)
        series_id = XmlUtilities.value_from_xml_element(root.find("SeriesId"), str)
        season_id = XmlUtilities.value_from_xml_element(root.find("SeasonId"), str)
        special_feature_count = XmlUtilities.value_from_xml_element(
            root.find("SpecialFeatureCount"), int
        )
        display_preferences_id = XmlUtilities.value_from_xml_element(
            root.find("DisplayPreferencesId"), str
        )
        status = XmlUtilities.value_from_xml_element(root.find("Status"), str)
        air_time = XmlUtilities.value_from_xml_element(root.find("AirTime"), str)
        air_days = XmlUtilities.list_from_xml_element(root, "AirDays", str)
        tags = XmlUtilities.list_from_xml_element(root, "Tags", str)
        primary_image_aspect_ratio = XmlUtilities.value_from_xml_element(
            root.find("PrimaryImageAspectRatio"), float
        )
        artists = XmlUtilities.list_from_xml_element(root, "Artists", str)
        artist_items = XmlUtilities.list_from_xml_element(
            root, "NameGuidPair", NameGuidPair
        )
        album = XmlUtilities.value_from_xml_element(root.find("Album"), str)
        collection_type = XmlUtilities.value_from_xml_element(
            root.find("CollectionType"), str
        )
        display_order = XmlUtilities.value_from_xml_element(
            root.find("DisplayOrder"), str
        )
        album_id = XmlUtilities.value_from_xml_element(root.find("AlbumId"), str)
        album_primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("AlbumPrimaryImageTag"), str
        )
        series_primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("SeriesPrimaryImageTag"), str
        )
        album_artist = XmlUtilities.value_from_xml_element(
            root.find("AlbumArtist"), str
        )
        album_artists = XmlUtilities.list_from_xml_element(
            root, "NameGuidPair", NameGuidPair
        )
        season_name = XmlUtilities.value_from_xml_element(root.find("SeasonName"), str)
        media_streams = XmlUtilities.list_from_xml_element(
            root, "MediaStream", MediaStream
        )
        video_type = XmlUtilities.value_from_xml_element(root.find("VideoType"), str)
        part_count = XmlUtilities.value_from_xml_element(root.find("PartCount"), int)
        media_source_count = XmlUtilities.value_from_xml_element(
            root.find("MediaSourceCount"), int
        )
        image_tags = XmlUtilities.dict_from_xml_element(root.find("ImageTags"), dict)

        backdrop_image_tags = XmlUtilities.list_from_xml_element(
            root, "BackdropImageTags", str
        )
        screenshot_image_tags = XmlUtilities.list_from_xml_element(
            root, "ScreenshotImageTags", str
        )
        parent_logo_image_tag = XmlUtilities.value_from_xml_element(
            root.find("ParentLogoImageTag"), str
        )
        parent_art_item_id = XmlUtilities.value_from_xml_element(
            root.find("ParentArtItemId"), str
        )
        parent_art_image_tag = XmlUtilities.value_from_xml_element(
            root.find("ParentArtImageTag"), str
        )
        series_thumb_image_tag = XmlUtilities.value_from_xml_element(
            root.find("SeriesThumbImageTag"), str
        )
        image_blur_hashes = XmlUtilities.value_from_xml_element(
            root.find("ImageBlurHashes1"), ImageBlurHashes1
        )
        series_studio = XmlUtilities.value_from_xml_element(
            root.find("SeriesStudio"), str
        )
        parent_thumb_item_id = XmlUtilities.value_from_xml_element(
            root.find("ParentThumbItemId"), str
        )
        parent_thumb_image_tag = XmlUtilities.value_from_xml_element(
            root.find("ParentThumbImageTag"), str
        )
        parent_primary_image_item_id = XmlUtilities.value_from_xml_element(
            root.find("ParentPrimaryImageItemId"), str
        )
        parent_primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("ParentPrimaryImageTag"), str
        )
        chapters = XmlUtilities.list_from_xml_element(root, "ChapterInfo", ChapterInfo)
        location_type = XmlUtilities.value_from_xml_element(
            root.find("LocationType"), str
        )
        iso_type = XmlUtilities.value_from_xml_element(root.find("IsoType"), str)
        media_type = XmlUtilities.value_from_xml_element(root.find("MediaType"), str)
        end_date = XmlUtilities.value_from_xml_element(
            root.find("EndDate"), APIHelper.RFC3339DateTime
        )
        locked_fields = XmlUtilities.list_from_xml_element(root, "LockedFields", str)
        trailer_count = XmlUtilities.value_from_xml_element(
            root.find("TrailerCount"), int
        )
        movie_count = XmlUtilities.value_from_xml_element(root.find("MovieCount"), int)
        series_count = XmlUtilities.value_from_xml_element(
            root.find("SeriesCount"), int
        )
        program_count = XmlUtilities.value_from_xml_element(
            root.find("ProgramCount"), int
        )
        episode_count = XmlUtilities.value_from_xml_element(
            root.find("EpisodeCount"), int
        )
        song_count = XmlUtilities.value_from_xml_element(root.find("SongCount"), int)
        album_count = XmlUtilities.value_from_xml_element(root.find("AlbumCount"), int)
        artist_count = XmlUtilities.value_from_xml_element(
            root.find("ArtistCount"), int
        )
        music_video_count = XmlUtilities.value_from_xml_element(
            root.find("MusicVideoCount"), int
        )
        lock_data = XmlUtilities.value_from_xml_element(root.find("LockData"), bool)
        width = XmlUtilities.value_from_xml_element(root.find("Width"), int)
        height = XmlUtilities.value_from_xml_element(root.find("Height"), int)
        camera_make = XmlUtilities.value_from_xml_element(root.find("CameraMake"), str)
        camera_model = XmlUtilities.value_from_xml_element(
            root.find("CameraModel"), str
        )
        software = XmlUtilities.value_from_xml_element(root.find("Software"), str)
        exposure_time = XmlUtilities.value_from_xml_element(
            root.find("ExposureTime"), float
        )
        focal_length = XmlUtilities.value_from_xml_element(
            root.find("FocalLength"), float
        )
        image_orientation = XmlUtilities.value_from_xml_element(
            root.find("ImageOrientation"), str
        )
        aperture = XmlUtilities.value_from_xml_element(root.find("Aperture"), float)
        shutter_speed = XmlUtilities.value_from_xml_element(
            root.find("ShutterSpeed"), float
        )
        latitude = XmlUtilities.value_from_xml_element(root.find("Latitude"), float)
        longitude = XmlUtilities.value_from_xml_element(root.find("Longitude"), float)
        altitude = XmlUtilities.value_from_xml_element(root.find("Altitude"), float)
        iso_speed_rating = XmlUtilities.value_from_xml_element(
            root.find("IsoSpeedRating"), int
        )
        series_timer_id = XmlUtilities.value_from_xml_element(
            root.find("SeriesTimerId"), str
        )
        program_id = XmlUtilities.value_from_xml_element(root.find("ProgramId"), str)
        channel_primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("ChannelPrimaryImageTag"), str
        )
        start_date = XmlUtilities.value_from_xml_element(
            root.find("StartDate"), APIHelper.RFC3339DateTime
        )
        completion_percentage = XmlUtilities.value_from_xml_element(
            root.find("CompletionPercentage"), float
        )
        is_repeat = XmlUtilities.value_from_xml_element(root.find("IsRepeat"), bool)
        episode_title = XmlUtilities.value_from_xml_element(
            root.find("EpisodeTitle"), str
        )
        channel_type = XmlUtilities.value_from_xml_element(
            root.find("ChannelType"), str
        )
        audio = XmlUtilities.value_from_xml_element(root.find("Audio"), str)
        is_movie = XmlUtilities.value_from_xml_element(root.find("IsMovie"), bool)
        is_sports = XmlUtilities.value_from_xml_element(root.find("IsSports"), bool)
        is_series = XmlUtilities.value_from_xml_element(root.find("IsSeries"), bool)
        is_live = XmlUtilities.value_from_xml_element(root.find("IsLive"), bool)
        is_news = XmlUtilities.value_from_xml_element(root.find("IsNews"), bool)
        is_kids = XmlUtilities.value_from_xml_element(root.find("IsKids"), bool)
        is_premiere = XmlUtilities.value_from_xml_element(root.find("IsPremiere"), bool)
        timer_id = XmlUtilities.value_from_xml_element(root.find("TimerId"), str)
        current_program = XmlUtilities.value_from_xml_element(
            root.find("BaseItemDto"), BaseItemDto
        )

        return cls(
            name,
            original_title,
            server_id,
            id,
            etag,
            source_type,
            playlist_item_id,
            date_created,
            date_last_media_added,
            extra_type,
            airs_before_season_number,
            airs_after_season_number,
            airs_before_episode_number,
            can_delete,
            can_download,
            has_subtitles,
            preferred_metadata_language,
            preferred_metadata_country_code,
            supports_sync,
            container,
            sort_name,
            forced_sort_name,
            video_3_d_format,
            premiere_date,
            external_urls,
            media_sources,
            critic_rating,
            production_locations,
            path,
            enable_media_source_display,
            official_rating,
            custom_rating,
            channel_id,
            channel_name,
            overview,
            taglines,
            genres,
            community_rating,
            cumulative_run_time_ticks,
            run_time_ticks,
            play_access,
            aspect_ratio,
            production_year,
            is_place_holder,
            number,
            channel_number,
            index_number,
            index_number_end,
            parent_index_number,
            remote_trailers,
            provider_ids,
            is_hd,
            is_folder,
            parent_id,
            mtype,
            people,
            studios,
            genre_items,
            parent_logo_item_id,
            parent_backdrop_item_id,
            parent_backdrop_image_tags,
            local_trailer_count,
            user_data,
            recursive_item_count,
            child_count,
            series_name,
            series_id,
            season_id,
            special_feature_count,
            display_preferences_id,
            status,
            air_time,
            air_days,
            tags,
            primary_image_aspect_ratio,
            artists,
            artist_items,
            album,
            collection_type,
            display_order,
            album_id,
            album_primary_image_tag,
            series_primary_image_tag,
            album_artist,
            album_artists,
            season_name,
            media_streams,
            video_type,
            part_count,
            media_source_count,
            image_tags,
            backdrop_image_tags,
            screenshot_image_tags,
            parent_logo_image_tag,
            parent_art_item_id,
            parent_art_image_tag,
            series_thumb_image_tag,
            image_blur_hashes,
            series_studio,
            parent_thumb_item_id,
            parent_thumb_image_tag,
            parent_primary_image_item_id,
            parent_primary_image_tag,
            chapters,
            location_type,
            iso_type,
            media_type,
            end_date,
            locked_fields,
            trailer_count,
            movie_count,
            series_count,
            program_count,
            episode_count,
            song_count,
            album_count,
            artist_count,
            music_video_count,
            lock_data,
            width,
            height,
            camera_make,
            camera_model,
            software,
            exposure_time,
            focal_length,
            image_orientation,
            aperture,
            shutter_speed,
            latitude,
            longitude,
            altitude,
            iso_speed_rating,
            series_timer_id,
            program_id,
            channel_primary_image_tag,
            start_date,
            completion_percentage,
            is_repeat,
            episode_title,
            channel_type,
            audio,
            is_movie,
            is_sports,
            is_series,
            is_live,
            is_news,
            is_kids,
            is_premiere,
            timer_id,
            current_program,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.original_title, "OriginalTitle")
        XmlUtilities.add_as_subelement(root, self.server_id, "ServerId")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.etag, "Etag")
        XmlUtilities.add_as_subelement(root, self.source_type, "SourceType")
        XmlUtilities.add_as_subelement(root, self.playlist_item_id, "PlaylistItemId")
        XmlUtilities.add_as_subelement(root, self.date_created, "DateCreated")
        XmlUtilities.add_as_subelement(
            root, self.date_last_media_added, "DateLastMediaAdded"
        )
        XmlUtilities.add_as_subelement(root, self.extra_type, "ExtraType")
        XmlUtilities.add_as_subelement(
            root, self.airs_before_season_number, "AirsBeforeSeasonNumber"
        )
        XmlUtilities.add_as_subelement(
            root, self.airs_after_season_number, "AirsAfterSeasonNumber"
        )
        XmlUtilities.add_as_subelement(
            root, self.airs_before_episode_number, "AirsBeforeEpisodeNumber"
        )
        XmlUtilities.add_as_subelement(root, self.can_delete, "CanDelete")
        XmlUtilities.add_as_subelement(root, self.can_download, "CanDownload")
        XmlUtilities.add_as_subelement(root, self.has_subtitles, "HasSubtitles")
        XmlUtilities.add_as_subelement(
            root, self.preferred_metadata_language, "PreferredMetadataLanguage"
        )
        XmlUtilities.add_as_subelement(
            root, self.preferred_metadata_country_code, "PreferredMetadataCountryCode"
        )
        XmlUtilities.add_as_subelement(root, self.supports_sync, "SupportsSync")
        XmlUtilities.add_as_subelement(root, self.container, "Container")
        XmlUtilities.add_as_subelement(root, self.sort_name, "SortName")
        XmlUtilities.add_as_subelement(root, self.forced_sort_name, "ForcedSortName")
        XmlUtilities.add_as_subelement(root, self.video_3_d_format, "Video3DFormat")
        XmlUtilities.add_as_subelement(root, self.premiere_date, "PremiereDate")
        XmlUtilities.add_list_as_subelement(root, self.external_urls, "ExternalUrl")
        XmlUtilities.add_list_as_subelement(root, self.media_sources, "MediaSourceInfo")
        XmlUtilities.add_as_subelement(root, self.critic_rating, "CriticRating")
        XmlUtilities.add_list_as_subelement(
            root, self.production_locations, "ProductionLocations"
        )
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_as_subelement(
            root, self.enable_media_source_display, "EnableMediaSourceDisplay"
        )
        XmlUtilities.add_as_subelement(root, self.official_rating, "OfficialRating")
        XmlUtilities.add_as_subelement(root, self.custom_rating, "CustomRating")
        XmlUtilities.add_as_subelement(root, self.channel_id, "ChannelId")
        XmlUtilities.add_as_subelement(root, self.channel_name, "ChannelName")
        XmlUtilities.add_as_subelement(root, self.overview, "Overview")
        XmlUtilities.add_list_as_subelement(root, self.taglines, "Taglines")
        XmlUtilities.add_list_as_subelement(root, self.genres, "Genres")
        XmlUtilities.add_as_subelement(root, self.community_rating, "CommunityRating")
        XmlUtilities.add_as_subelement(
            root, self.cumulative_run_time_ticks, "CumulativeRunTimeTicks"
        )
        XmlUtilities.add_as_subelement(root, self.run_time_ticks, "RunTimeTicks")
        XmlUtilities.add_as_subelement(root, self.play_access, "PlayAccess")
        XmlUtilities.add_as_subelement(root, self.aspect_ratio, "AspectRatio")
        XmlUtilities.add_as_subelement(root, self.production_year, "ProductionYear")
        XmlUtilities.add_as_subelement(root, self.is_place_holder, "IsPlaceHolder")
        XmlUtilities.add_as_subelement(root, self.number, "Number")
        XmlUtilities.add_as_subelement(root, self.channel_number, "ChannelNumber")
        XmlUtilities.add_as_subelement(root, self.index_number, "IndexNumber")
        XmlUtilities.add_as_subelement(root, self.index_number_end, "IndexNumberEnd")
        XmlUtilities.add_as_subelement(
            root, self.parent_index_number, "ParentIndexNumber"
        )
        XmlUtilities.add_list_as_subelement(root, self.remote_trailers, "MediaUrl")
        XmlUtilities.add_dict_as_subelement(
            root, self.provider_ids, dictionary_name="ProviderIds"
        )
        XmlUtilities.add_as_subelement(root, self.is_hd, "IsHD")
        XmlUtilities.add_as_subelement(root, self.is_folder, "IsFolder")
        XmlUtilities.add_as_subelement(root, self.parent_id, "ParentId")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_list_as_subelement(root, self.people, "BaseItemPerson")
        XmlUtilities.add_list_as_subelement(root, self.studios, "NameGuidPair")
        XmlUtilities.add_list_as_subelement(root, self.genre_items, "NameGuidPair")
        XmlUtilities.add_as_subelement(
            root, self.parent_logo_item_id, "ParentLogoItemId"
        )
        XmlUtilities.add_as_subelement(
            root, self.parent_backdrop_item_id, "ParentBackdropItemId"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.parent_backdrop_image_tags, "ParentBackdropImageTags"
        )
        XmlUtilities.add_as_subelement(
            root, self.local_trailer_count, "LocalTrailerCount"
        )
        XmlUtilities.add_as_subelement(root, self.user_data, "UserItemDataDto")
        XmlUtilities.add_as_subelement(
            root, self.recursive_item_count, "RecursiveItemCount"
        )
        XmlUtilities.add_as_subelement(root, self.child_count, "ChildCount")
        XmlUtilities.add_as_subelement(root, self.series_name, "SeriesName")
        XmlUtilities.add_as_subelement(root, self.series_id, "SeriesId")
        XmlUtilities.add_as_subelement(root, self.season_id, "SeasonId")
        XmlUtilities.add_as_subelement(
            root, self.special_feature_count, "SpecialFeatureCount"
        )
        XmlUtilities.add_as_subelement(
            root, self.display_preferences_id, "DisplayPreferencesId"
        )
        XmlUtilities.add_as_subelement(root, self.status, "Status")
        XmlUtilities.add_as_subelement(root, self.air_time, "AirTime")
        XmlUtilities.add_list_as_subelement(root, self.air_days, "AirDays")
        XmlUtilities.add_list_as_subelement(root, self.tags, "Tags")
        XmlUtilities.add_as_subelement(
            root, self.primary_image_aspect_ratio, "PrimaryImageAspectRatio"
        )
        XmlUtilities.add_list_as_subelement(root, self.artists, "Artists")
        XmlUtilities.add_list_as_subelement(root, self.artist_items, "NameGuidPair")
        XmlUtilities.add_as_subelement(root, self.album, "Album")
        XmlUtilities.add_as_subelement(root, self.collection_type, "CollectionType")
        XmlUtilities.add_as_subelement(root, self.display_order, "DisplayOrder")
        XmlUtilities.add_as_subelement(root, self.album_id, "AlbumId")
        XmlUtilities.add_as_subelement(
            root, self.album_primary_image_tag, "AlbumPrimaryImageTag"
        )
        XmlUtilities.add_as_subelement(
            root, self.series_primary_image_tag, "SeriesPrimaryImageTag"
        )
        XmlUtilities.add_as_subelement(root, self.album_artist, "AlbumArtist")
        XmlUtilities.add_list_as_subelement(root, self.album_artists, "NameGuidPair")
        XmlUtilities.add_as_subelement(root, self.season_name, "SeasonName")
        XmlUtilities.add_list_as_subelement(root, self.media_streams, "MediaStream")
        XmlUtilities.add_as_subelement(root, self.video_type, "VideoType")
        XmlUtilities.add_as_subelement(root, self.part_count, "PartCount")
        XmlUtilities.add_as_subelement(
            root, self.media_source_count, "MediaSourceCount"
        )
        XmlUtilities.add_dict_as_subelement(
            root, self.image_tags, dictionary_name="ImageTags"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.backdrop_image_tags, "BackdropImageTags"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.screenshot_image_tags, "ScreenshotImageTags"
        )
        XmlUtilities.add_as_subelement(
            root, self.parent_logo_image_tag, "ParentLogoImageTag"
        )
        XmlUtilities.add_as_subelement(root, self.parent_art_item_id, "ParentArtItemId")
        XmlUtilities.add_as_subelement(
            root, self.parent_art_image_tag, "ParentArtImageTag"
        )
        XmlUtilities.add_as_subelement(
            root, self.series_thumb_image_tag, "SeriesThumbImageTag"
        )
        XmlUtilities.add_as_subelement(root, self.image_blur_hashes, "ImageBlurHashes1")
        XmlUtilities.add_as_subelement(root, self.series_studio, "SeriesStudio")
        XmlUtilities.add_as_subelement(
            root, self.parent_thumb_item_id, "ParentThumbItemId"
        )
        XmlUtilities.add_as_subelement(
            root, self.parent_thumb_image_tag, "ParentThumbImageTag"
        )
        XmlUtilities.add_as_subelement(
            root, self.parent_primary_image_item_id, "ParentPrimaryImageItemId"
        )
        XmlUtilities.add_as_subelement(
            root, self.parent_primary_image_tag, "ParentPrimaryImageTag"
        )
        XmlUtilities.add_list_as_subelement(root, self.chapters, "ChapterInfo")
        XmlUtilities.add_as_subelement(root, self.location_type, "LocationType")
        XmlUtilities.add_as_subelement(root, self.iso_type, "IsoType")
        XmlUtilities.add_as_subelement(root, self.media_type, "MediaType")
        XmlUtilities.add_as_subelement(root, self.end_date, "EndDate")
        XmlUtilities.add_list_as_subelement(root, self.locked_fields, "LockedFields")
        XmlUtilities.add_as_subelement(root, self.trailer_count, "TrailerCount")
        XmlUtilities.add_as_subelement(root, self.movie_count, "MovieCount")
        XmlUtilities.add_as_subelement(root, self.series_count, "SeriesCount")
        XmlUtilities.add_as_subelement(root, self.program_count, "ProgramCount")
        XmlUtilities.add_as_subelement(root, self.episode_count, "EpisodeCount")
        XmlUtilities.add_as_subelement(root, self.song_count, "SongCount")
        XmlUtilities.add_as_subelement(root, self.album_count, "AlbumCount")
        XmlUtilities.add_as_subelement(root, self.artist_count, "ArtistCount")
        XmlUtilities.add_as_subelement(root, self.music_video_count, "MusicVideoCount")
        XmlUtilities.add_as_subelement(root, self.lock_data, "LockData")
        XmlUtilities.add_as_subelement(root, self.width, "Width")
        XmlUtilities.add_as_subelement(root, self.height, "Height")
        XmlUtilities.add_as_subelement(root, self.camera_make, "CameraMake")
        XmlUtilities.add_as_subelement(root, self.camera_model, "CameraModel")
        XmlUtilities.add_as_subelement(root, self.software, "Software")
        XmlUtilities.add_as_subelement(root, self.exposure_time, "ExposureTime")
        XmlUtilities.add_as_subelement(root, self.focal_length, "FocalLength")
        XmlUtilities.add_as_subelement(root, self.image_orientation, "ImageOrientation")
        XmlUtilities.add_as_subelement(root, self.aperture, "Aperture")
        XmlUtilities.add_as_subelement(root, self.shutter_speed, "ShutterSpeed")
        XmlUtilities.add_as_subelement(root, self.latitude, "Latitude")
        XmlUtilities.add_as_subelement(root, self.longitude, "Longitude")
        XmlUtilities.add_as_subelement(root, self.altitude, "Altitude")
        XmlUtilities.add_as_subelement(root, self.iso_speed_rating, "IsoSpeedRating")
        XmlUtilities.add_as_subelement(root, self.series_timer_id, "SeriesTimerId")
        XmlUtilities.add_as_subelement(root, self.program_id, "ProgramId")
        XmlUtilities.add_as_subelement(
            root, self.channel_primary_image_tag, "ChannelPrimaryImageTag"
        )
        XmlUtilities.add_as_subelement(root, self.start_date, "StartDate")
        XmlUtilities.add_as_subelement(
            root, self.completion_percentage, "CompletionPercentage"
        )
        XmlUtilities.add_as_subelement(root, self.is_repeat, "IsRepeat")
        XmlUtilities.add_as_subelement(root, self.episode_title, "EpisodeTitle")
        XmlUtilities.add_as_subelement(root, self.channel_type, "ChannelType")
        XmlUtilities.add_as_subelement(root, self.audio, "Audio")
        XmlUtilities.add_as_subelement(root, self.is_movie, "IsMovie")
        XmlUtilities.add_as_subelement(root, self.is_sports, "IsSports")
        XmlUtilities.add_as_subelement(root, self.is_series, "IsSeries")
        XmlUtilities.add_as_subelement(root, self.is_live, "IsLive")
        XmlUtilities.add_as_subelement(root, self.is_news, "IsNews")
        XmlUtilities.add_as_subelement(root, self.is_kids, "IsKids")
        XmlUtilities.add_as_subelement(root, self.is_premiere, "IsPremiere")
        XmlUtilities.add_as_subelement(root, self.timer_id, "TimerId")
        XmlUtilities.add_as_subelement(root, self.current_program, "BaseItemDto")
