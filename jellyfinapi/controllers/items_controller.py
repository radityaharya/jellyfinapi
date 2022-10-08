# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.exceptions.api_exception import APIException


class ItemsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ItemsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_items(
        self,
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
        include_item_types=None,
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
        enable_images=True,
    ):
        """Does a GET request to /Items.

        Gets items based on a query.

        Args:
            user_id (uuid|string, optional): The user id supplied as query
                parameter.
            max_official_rating (string, optional): Optional filter by maximum
                official rating (PG, PG-13, TV-MA, etc).
            has_theme_song (bool, optional): Optional filter by items with
                theme songs.
            has_theme_video (bool, optional): Optional filter by items with
                theme videos.
            has_subtitles (bool, optional): Optional filter by items with
                subtitles.
            has_special_feature (bool, optional): Optional filter by items
                with special features.
            has_trailer (bool, optional): Optional filter by items with
                trailers.
            adjacent_to (string, optional): Optional. Return items that are
                siblings of a supplied item.
            parent_index_number (int, optional): Optional filter by parent
                index number.
            has_parental_rating (bool, optional): Optional filter by items
                that have or do not have a parental rating.
            is_hd (bool, optional): Optional filter by items that are HD or
                not.
            is_4_k (bool, optional): Optional filter by items that are 4K or
                not.
            location_types (list of LocationTypeEnum, optional): Optional. If
                specified, results will be filtered based on LocationType.
                This allows multiple, comma delimited.
            exclude_location_types (list of LocationTypeEnum, optional):
                Optional. If specified, results will be filtered based on the
                LocationType. This allows multiple, comma delimited.
            is_missing (bool, optional): Optional filter by items that are
                missing episodes or not.
            is_unaired (bool, optional): Optional filter by items that are
                unaired episodes or not.
            min_community_rating (float, optional): Optional filter by minimum
                community rating.
            min_critic_rating (float, optional): Optional filter by minimum
                critic rating.
            min_premiere_date (datetime, optional): Optional. The minimum
                premiere date. Format = ISO.
            min_date_last_saved (datetime, optional): Optional. The minimum
                last saved date. Format = ISO.
            min_date_last_saved_for_user (datetime, optional): Optional. The
                minimum last saved date for the current user. Format = ISO.
            max_premiere_date (datetime, optional): Optional. The maximum
                premiere date. Format = ISO.
            has_overview (bool, optional): Optional filter by items that have
                an overview or not.
            has_imdb_id (bool, optional): Optional filter by items that have
                an imdb id or not.
            has_tmdb_id (bool, optional): Optional filter by items that have a
                tmdb id or not.
            has_tvdb_id (bool, optional): Optional filter by items that have a
                tvdb id or not.
            is_movie (bool, optional): Optional filter for live tv movies.
            is_series (bool, optional): Optional filter for live tv series.
            is_news (bool, optional): Optional filter for live tv news.
            is_kids (bool, optional): Optional filter for live tv kids.
            is_sports (bool, optional): Optional filter for live tv sports.
            exclude_item_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered by excluding item ids.
                This allows multiple, comma delimited.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            recursive (bool, optional): When searching within folders, this
                determines whether or not the search will be recursive.
                true/false.
            search_term (string, optional): Optional. Filter based on a search
                term.
            sort_order (list of SortOrderEnum, optional): Sort Order -
                Ascending,Descending.
            parent_id (uuid|string, optional): Specify this to localize the
                search to a specific item or folder. Omit to use the root.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios,
                Taglines.
            exclude_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on item type.
                This allows multiple, comma delimited.
            include_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on the item type.
                This allows multiple, comma delimited.
            filters (list of ItemFilterEnum, optional): Optional. Specify
                additional filters to apply. This allows multiple, comma
                delimited. Options: IsFolder, IsNotFolder, IsUnplayed,
                IsPlayed, IsFavorite, IsResumable, Likes, Dislikes.
            is_favorite (bool, optional): Optional filter by items that are
                marked as favorite, or not.
            media_types (list of string, optional): Optional filter by
                MediaType. Allows multiple, comma delimited.
            image_types (list of ImageTypeEnum, optional): Optional. If
                specified, results will be filtered based on those containing
                image types. This allows multiple, comma delimited.
            sort_by (list of string, optional): Optional. Specify one or more
                sort orders, comma delimited. Options: Album, AlbumArtist,
                Artist, Budget, CommunityRating, CriticRating, DateCreated,
                DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName,
                Random, Revenue, Runtime.
            is_played (bool, optional): Optional filter by items that are
                played, or not.
            genres (list of string, optional): Optional. If specified, results
                will be filtered based on genre. This allows multiple, pipe
                delimited.
            official_ratings (list of string, optional): Optional. If
                specified, results will be filtered based on OfficialRating.
                This allows multiple, pipe delimited.
            tags (list of string, optional): Optional. If specified, results
                will be filtered based on tag. This allows multiple, pipe
                delimited.
            years (list of int, optional): Optional. If specified, results
                will be filtered based on production year. This allows
                multiple, comma delimited.
            enable_user_data (bool, optional): Optional, include user data.
            image_type_limit (int, optional): Optional, the max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            person (string, optional): Optional. If specified, results will be
                filtered to include only those containing the specified
                person.
            person_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered to include only those
                containing the specified person id.
            person_types (list of string, optional): Optional. If specified,
                along with Person, results will be filtered to include only
                those containing the specified person and PersonType. Allows
                multiple, comma-delimited.
            studios (list of string, optional): Optional. If specified,
                results will be filtered based on studio. This allows
                multiple, pipe delimited.
            artists (list of string, optional): Optional. If specified,
                results will be filtered based on artists. This allows
                multiple, pipe delimited.
            exclude_artist_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered based on artist id. This
                allows multiple, pipe delimited.
            artist_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered to include only those
                containing the specified artist id.
            album_artist_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered to include only those
                containing the specified album artist id.
            contributing_artist_ids (list of uuid|string, optional): Optional.
                If specified, results will be filtered to include only those
                containing the specified contributing artist id.
            albums (list of string, optional): Optional. If specified, results
                will be filtered based on album. This allows multiple, pipe
                delimited.
            album_ids (list of uuid|string, optional): Optional. If specified,
                results will be filtered based on album id. This allows
                multiple, pipe delimited.
            ids (list of uuid|string, optional): Optional. If specific items
                are needed, specify a list of item id's to retrieve. This
                allows multiple, comma delimited.
            video_types (list of VideoTypeEnum, optional): Optional filter by
                VideoType (videofile, dvd, bluray, iso). Allows multiple,
                comma delimited.
            min_official_rating (string, optional): Optional filter by minimum
                official rating (PG, PG-13, TV-MA, etc).
            is_locked (bool, optional): Optional filter by items that are
                locked.
            is_place_holder (bool, optional): Optional filter by items that
                are placeholders.
            has_official_rating (bool, optional): Optional filter by items
                that have official ratings.
            collapse_box_set_items (bool, optional): Whether or not to hide
                items behind their boxsets.
            min_width (int, optional): Optional. Filter by the minimum width
                of the item.
            min_height (int, optional): Optional. Filter by the minimum height
                of the item.
            max_width (int, optional): Optional. Filter by the maximum width
                of the item.
            max_height (int, optional): Optional. Filter by the maximum height
                of the item.
            is_3_d (bool, optional): Optional filter by items that are 3D, or
                not.
            series_status (list of SeriesStatusEnum, optional): Optional
                filter by Series Status. Allows multiple, comma delimited.
            name_starts_with_or_greater (string, optional): Optional filter by
                items whose name is sorted equally or greater than a given
                input string.
            name_starts_with (string, optional): Optional filter by items
                whose name is sorted equally than a given input string.
            name_less_than (string, optional): Optional filter by items whose
                name is equally or lesser than a given input string.
            studio_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered based on studio id. This
                allows multiple, pipe delimited.
            genre_ids (list of uuid|string, optional): Optional. If specified,
                results will be filtered based on genre id. This allows
                multiple, pipe delimited.
            enable_total_record_count (bool, optional): Optional. Enable the
                total record count.
            enable_images (bool, optional): Optional, include image
                information in output.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_items called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_items.")
            _url_path = "/Items"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "maxOfficialRating": max_official_rating,
                "hasThemeSong": has_theme_song,
                "hasThemeVideo": has_theme_video,
                "hasSubtitles": has_subtitles,
                "hasSpecialFeature": has_special_feature,
                "hasTrailer": has_trailer,
                "adjacentTo": adjacent_to,
                "parentIndexNumber": parent_index_number,
                "hasParentalRating": has_parental_rating,
                "isHd": is_hd,
                "is4K": is_4_k,
                "locationTypes": location_types,
                "excludeLocationTypes": exclude_location_types,
                "isMissing": is_missing,
                "isUnaired": is_unaired,
                "minCommunityRating": min_community_rating,
                "minCriticRating": min_critic_rating,
                "minPremiereDate": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, min_premiere_date
                ),
                "minDateLastSaved": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, min_date_last_saved
                ),
                "minDateLastSavedForUser": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, min_date_last_saved_for_user
                ),
                "maxPremiereDate": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, max_premiere_date
                ),
                "hasOverview": has_overview,
                "hasImdbId": has_imdb_id,
                "hasTmdbId": has_tmdb_id,
                "hasTvdbId": has_tvdb_id,
                "isMovie": is_movie,
                "isSeries": is_series,
                "isNews": is_news,
                "isKids": is_kids,
                "isSports": is_sports,
                "excludeItemIds": exclude_item_ids,
                "startIndex": start_index,
                "limit": limit,
                "recursive": recursive,
                "searchTerm": search_term,
                "sortOrder": sort_order,
                "parentId": parent_id,
                "fields": fields,
                "excludeItemTypes": exclude_item_types,
                "includeItemTypes": include_item_types,
                "filters": filters,
                "isFavorite": is_favorite,
                "mediaTypes": media_types,
                "imageTypes": image_types,
                "sortBy": sort_by,
                "isPlayed": is_played,
                "genres": genres,
                "officialRatings": official_ratings,
                "tags": tags,
                "years": years,
                "enableUserData": enable_user_data,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "person": person,
                "personIds": person_ids,
                "personTypes": person_types,
                "studios": studios,
                "artists": artists,
                "excludeArtistIds": exclude_artist_ids,
                "artistIds": artist_ids,
                "albumArtistIds": album_artist_ids,
                "contributingArtistIds": contributing_artist_ids,
                "albums": albums,
                "albumIds": album_ids,
                "ids": ids,
                "videoTypes": video_types,
                "minOfficialRating": min_official_rating,
                "isLocked": is_locked,
                "isPlaceHolder": is_place_holder,
                "hasOfficialRating": has_official_rating,
                "collapseBoxSetItems": collapse_box_set_items,
                "minWidth": min_width,
                "minHeight": min_height,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "is3D": is_3_d,
                "seriesStatus": series_status,
                "nameStartsWithOrGreater": name_starts_with_or_greater,
                "nameStartsWith": name_starts_with,
                "nameLessThan": name_less_than,
                "studioIds": studio_ids,
                "genreIds": genre_ids,
                "enableTotalRecordCount": enable_total_record_count,
                "enableImages": enable_images,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_items.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_items.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_items")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_items.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDtoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_items_by_user_id(
        self,
        user_id,
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
        include_item_types=None,
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
        enable_images=True,
    ):
        """Does a GET request to /Users/{userId}/Items.

        Gets items based on a query.

        Args:
            user_id (uuid|string): The user id supplied as query parameter.
            max_official_rating (string, optional): Optional filter by maximum
                official rating (PG, PG-13, TV-MA, etc).
            has_theme_song (bool, optional): Optional filter by items with
                theme songs.
            has_theme_video (bool, optional): Optional filter by items with
                theme videos.
            has_subtitles (bool, optional): Optional filter by items with
                subtitles.
            has_special_feature (bool, optional): Optional filter by items
                with special features.
            has_trailer (bool, optional): Optional filter by items with
                trailers.
            adjacent_to (string, optional): Optional. Return items that are
                siblings of a supplied item.
            parent_index_number (int, optional): Optional filter by parent
                index number.
            has_parental_rating (bool, optional): Optional filter by items
                that have or do not have a parental rating.
            is_hd (bool, optional): Optional filter by items that are HD or
                not.
            is_4_k (bool, optional): Optional filter by items that are 4K or
                not.
            location_types (list of LocationTypeEnum, optional): Optional. If
                specified, results will be filtered based on LocationType.
                This allows multiple, comma delimited.
            exclude_location_types (list of LocationTypeEnum, optional):
                Optional. If specified, results will be filtered based on the
                LocationType. This allows multiple, comma delimited.
            is_missing (bool, optional): Optional filter by items that are
                missing episodes or not.
            is_unaired (bool, optional): Optional filter by items that are
                unaired episodes or not.
            min_community_rating (float, optional): Optional filter by minimum
                community rating.
            min_critic_rating (float, optional): Optional filter by minimum
                critic rating.
            min_premiere_date (datetime, optional): Optional. The minimum
                premiere date. Format = ISO.
            min_date_last_saved (datetime, optional): Optional. The minimum
                last saved date. Format = ISO.
            min_date_last_saved_for_user (datetime, optional): Optional. The
                minimum last saved date for the current user. Format = ISO.
            max_premiere_date (datetime, optional): Optional. The maximum
                premiere date. Format = ISO.
            has_overview (bool, optional): Optional filter by items that have
                an overview or not.
            has_imdb_id (bool, optional): Optional filter by items that have
                an imdb id or not.
            has_tmdb_id (bool, optional): Optional filter by items that have a
                tmdb id or not.
            has_tvdb_id (bool, optional): Optional filter by items that have a
                tvdb id or not.
            is_movie (bool, optional): Optional filter for live tv movies.
            is_series (bool, optional): Optional filter for live tv series.
            is_news (bool, optional): Optional filter for live tv news.
            is_kids (bool, optional): Optional filter for live tv kids.
            is_sports (bool, optional): Optional filter for live tv sports.
            exclude_item_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered by excluding item ids.
                This allows multiple, comma delimited.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            recursive (bool, optional): When searching within folders, this
                determines whether or not the search will be recursive.
                true/false.
            search_term (string, optional): Optional. Filter based on a search
                term.
            sort_order (list of SortOrderEnum, optional): Sort Order -
                Ascending,Descending.
            parent_id (uuid|string, optional): Specify this to localize the
                search to a specific item or folder. Omit to use the root.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios,
                Taglines.
            exclude_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on item type.
                This allows multiple, comma delimited.
            include_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on the item type.
                This allows multiple, comma delimited.
            filters (list of ItemFilterEnum, optional): Optional. Specify
                additional filters to apply. This allows multiple, comma
                delimited. Options: IsFolder, IsNotFolder, IsUnplayed,
                IsPlayed, IsFavorite, IsResumable, Likes, Dislikes.
            is_favorite (bool, optional): Optional filter by items that are
                marked as favorite, or not.
            media_types (list of string, optional): Optional filter by
                MediaType. Allows multiple, comma delimited.
            image_types (list of ImageTypeEnum, optional): Optional. If
                specified, results will be filtered based on those containing
                image types. This allows multiple, comma delimited.
            sort_by (list of string, optional): Optional. Specify one or more
                sort orders, comma delimited. Options: Album, AlbumArtist,
                Artist, Budget, CommunityRating, CriticRating, DateCreated,
                DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName,
                Random, Revenue, Runtime.
            is_played (bool, optional): Optional filter by items that are
                played, or not.
            genres (list of string, optional): Optional. If specified, results
                will be filtered based on genre. This allows multiple, pipe
                delimited.
            official_ratings (list of string, optional): Optional. If
                specified, results will be filtered based on OfficialRating.
                This allows multiple, pipe delimited.
            tags (list of string, optional): Optional. If specified, results
                will be filtered based on tag. This allows multiple, pipe
                delimited.
            years (list of int, optional): Optional. If specified, results
                will be filtered based on production year. This allows
                multiple, comma delimited.
            enable_user_data (bool, optional): Optional, include user data.
            image_type_limit (int, optional): Optional, the max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            person (string, optional): Optional. If specified, results will be
                filtered to include only those containing the specified
                person.
            person_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered to include only those
                containing the specified person id.
            person_types (list of string, optional): Optional. If specified,
                along with Person, results will be filtered to include only
                those containing the specified person and PersonType. Allows
                multiple, comma-delimited.
            studios (list of string, optional): Optional. If specified,
                results will be filtered based on studio. This allows
                multiple, pipe delimited.
            artists (list of string, optional): Optional. If specified,
                results will be filtered based on artists. This allows
                multiple, pipe delimited.
            exclude_artist_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered based on artist id. This
                allows multiple, pipe delimited.
            artist_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered to include only those
                containing the specified artist id.
            album_artist_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered to include only those
                containing the specified album artist id.
            contributing_artist_ids (list of uuid|string, optional): Optional.
                If specified, results will be filtered to include only those
                containing the specified contributing artist id.
            albums (list of string, optional): Optional. If specified, results
                will be filtered based on album. This allows multiple, pipe
                delimited.
            album_ids (list of uuid|string, optional): Optional. If specified,
                results will be filtered based on album id. This allows
                multiple, pipe delimited.
            ids (list of uuid|string, optional): Optional. If specific items
                are needed, specify a list of item id's to retrieve. This
                allows multiple, comma delimited.
            video_types (list of VideoTypeEnum, optional): Optional filter by
                VideoType (videofile, dvd, bluray, iso). Allows multiple,
                comma delimited.
            min_official_rating (string, optional): Optional filter by minimum
                official rating (PG, PG-13, TV-MA, etc).
            is_locked (bool, optional): Optional filter by items that are
                locked.
            is_place_holder (bool, optional): Optional filter by items that
                are placeholders.
            has_official_rating (bool, optional): Optional filter by items
                that have official ratings.
            collapse_box_set_items (bool, optional): Whether or not to hide
                items behind their boxsets.
            min_width (int, optional): Optional. Filter by the minimum width
                of the item.
            min_height (int, optional): Optional. Filter by the minimum height
                of the item.
            max_width (int, optional): Optional. Filter by the maximum width
                of the item.
            max_height (int, optional): Optional. Filter by the maximum height
                of the item.
            is_3_d (bool, optional): Optional filter by items that are 3D, or
                not.
            series_status (list of SeriesStatusEnum, optional): Optional
                filter by Series Status. Allows multiple, comma delimited.
            name_starts_with_or_greater (string, optional): Optional filter by
                items whose name is sorted equally or greater than a given
                input string.
            name_starts_with (string, optional): Optional filter by items
                whose name is sorted equally than a given input string.
            name_less_than (string, optional): Optional filter by items whose
                name is equally or lesser than a given input string.
            studio_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered based on studio id. This
                allows multiple, pipe delimited.
            genre_ids (list of uuid|string, optional): Optional. If specified,
                results will be filtered based on genre id. This allows
                multiple, pipe delimited.
            enable_total_record_count (bool, optional): Optional. Enable the
                total record count.
            enable_images (bool, optional): Optional, include image
                information in output.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_items_by_user_id called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_items_by_user_id.")
            _url_path = "/Users/{userId}/Items"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "maxOfficialRating": max_official_rating,
                "hasThemeSong": has_theme_song,
                "hasThemeVideo": has_theme_video,
                "hasSubtitles": has_subtitles,
                "hasSpecialFeature": has_special_feature,
                "hasTrailer": has_trailer,
                "adjacentTo": adjacent_to,
                "parentIndexNumber": parent_index_number,
                "hasParentalRating": has_parental_rating,
                "isHd": is_hd,
                "is4K": is_4_k,
                "locationTypes": location_types,
                "excludeLocationTypes": exclude_location_types,
                "isMissing": is_missing,
                "isUnaired": is_unaired,
                "minCommunityRating": min_community_rating,
                "minCriticRating": min_critic_rating,
                "minPremiereDate": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, min_premiere_date
                ),
                "minDateLastSaved": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, min_date_last_saved
                ),
                "minDateLastSavedForUser": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, min_date_last_saved_for_user
                ),
                "maxPremiereDate": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, max_premiere_date
                ),
                "hasOverview": has_overview,
                "hasImdbId": has_imdb_id,
                "hasTmdbId": has_tmdb_id,
                "hasTvdbId": has_tvdb_id,
                "isMovie": is_movie,
                "isSeries": is_series,
                "isNews": is_news,
                "isKids": is_kids,
                "isSports": is_sports,
                "excludeItemIds": exclude_item_ids,
                "startIndex": start_index,
                "limit": limit,
                "recursive": recursive,
                "searchTerm": search_term,
                "sortOrder": sort_order,
                "parentId": parent_id,
                "fields": fields,
                "excludeItemTypes": exclude_item_types,
                "includeItemTypes": include_item_types,
                "filters": filters,
                "isFavorite": is_favorite,
                "mediaTypes": media_types,
                "imageTypes": image_types,
                "sortBy": sort_by,
                "isPlayed": is_played,
                "genres": genres,
                "officialRatings": official_ratings,
                "tags": tags,
                "years": years,
                "enableUserData": enable_user_data,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "person": person,
                "personIds": person_ids,
                "personTypes": person_types,
                "studios": studios,
                "artists": artists,
                "excludeArtistIds": exclude_artist_ids,
                "artistIds": artist_ids,
                "albumArtistIds": album_artist_ids,
                "contributingArtistIds": contributing_artist_ids,
                "albums": albums,
                "albumIds": album_ids,
                "ids": ids,
                "videoTypes": video_types,
                "minOfficialRating": min_official_rating,
                "isLocked": is_locked,
                "isPlaceHolder": is_place_holder,
                "hasOfficialRating": has_official_rating,
                "collapseBoxSetItems": collapse_box_set_items,
                "minWidth": min_width,
                "minHeight": min_height,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "is3D": is_3_d,
                "seriesStatus": series_status,
                "nameStartsWithOrGreater": name_starts_with_or_greater,
                "nameStartsWith": name_starts_with,
                "nameLessThan": name_less_than,
                "studioIds": studio_ids,
                "genreIds": genre_ids,
                "enableTotalRecordCount": enable_total_record_count,
                "enableImages": enable_images,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_items_by_user_id.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_items_by_user_id."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_items_by_user_id")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_items_by_user_id.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDtoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_resume_items(
        self,
        user_id,
        start_index=None,
        limit=None,
        search_term=None,
        parent_id=None,
        fields=None,
        media_types=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
        exclude_item_types=None,
        include_item_types=None,
        enable_total_record_count=True,
        enable_images=True,
        exclude_active_sessions=False,
    ):
        """Does a GET request to /Users/{userId}/Items/Resume.

        Gets items based on a query.

        Args:
            user_id (uuid|string): The user id.
            start_index (int, optional): The start index.
            limit (int, optional): The item limit.
            search_term (string, optional): The search term.
            parent_id (uuid|string, optional): Specify this to localize the
                search to a specific item or folder. Omit to use the root.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios,
                Taglines.
            media_types (list of string, optional): Optional. Filter by
                MediaType. Allows multiple, comma delimited.
            enable_user_data (bool, optional): Optional. Include user data.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            exclude_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on item type.
                This allows multiple, comma delimited.
            include_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on the item type.
                This allows multiple, comma delimited.
            enable_total_record_count (bool, optional): Optional. Enable the
                total record count.
            enable_images (bool, optional): Optional. Include image
                information in output.
            exclude_active_sessions (bool, optional): Optional. Whether to
                exclude the currently active sessions.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Items returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_resume_items called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_resume_items.")
            _url_path = "/Users/{userId}/Items/Resume"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "startIndex": start_index,
                "limit": limit,
                "searchTerm": search_term,
                "parentId": parent_id,
                "fields": fields,
                "mediaTypes": media_types,
                "enableUserData": enable_user_data,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "excludeItemTypes": exclude_item_types,
                "includeItemTypes": include_item_types,
                "enableTotalRecordCount": enable_total_record_count,
                "enableImages": enable_images,
                "excludeActiveSessions": exclude_active_sessions,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_resume_items.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_resume_items.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_resume_items")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_resume_items.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDtoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
