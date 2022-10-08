# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class TrailersControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(TrailersControllerTests, cls).setUpClass()
        cls.controller = cls.client.trailers
        cls.response_catcher = cls.controller.http_call_back

    # Finds movies and trailers similar to a given trailer.
    def test_get_trailers(self):
        # Parameters for the API call
        user_id = None
        max_official_rating = None
        has_theme_song = None
        has_theme_video = None
        has_subtitles = None
        has_special_feature = None
        has_trailer = None
        adjacent_to = None
        parent_index_number = None
        has_parental_rating = None
        is_hd = None
        is_4_k = None
        location_types = None
        exclude_location_types = None
        is_missing = None
        is_unaired = None
        min_community_rating = None
        min_critic_rating = None
        min_premiere_date = None
        min_date_last_saved = None
        min_date_last_saved_for_user = None
        max_premiere_date = None
        has_overview = None
        has_imdb_id = None
        has_tmdb_id = None
        has_tvdb_id = None
        is_movie = None
        is_series = None
        is_news = None
        is_kids = None
        is_sports = None
        exclude_item_ids = None
        start_index = None
        limit = None
        recursive = None
        search_term = None
        sort_order = None
        parent_id = None
        fields = None
        exclude_item_types = None
        filters = None
        is_favorite = None
        media_types = None
        image_types = None
        sort_by = None
        is_played = None
        genres = None
        official_ratings = None
        tags = None
        years = None
        enable_user_data = None
        image_type_limit = None
        enable_image_types = None
        person = None
        person_ids = None
        person_types = None
        studios = None
        artists = None
        exclude_artist_ids = None
        artist_ids = None
        album_artist_ids = None
        contributing_artist_ids = None
        albums = None
        album_ids = None
        ids = None
        video_types = None
        min_official_rating = None
        is_locked = None
        is_place_holder = None
        has_official_rating = None
        collapse_box_set_items = None
        min_width = None
        min_height = None
        max_width = None
        max_height = None
        is_3_d = None
        series_status = None
        name_starts_with_or_greater = None
        name_starts_with = None
        name_less_than = None
        studio_ids = None
        genre_ids = None
        enable_total_record_count = True
        enable_images = True

        # Perform the API call through the SDK function
        result = self.controller.get_trailers(
            user_id,
            max_official_rating,
            has_theme_song,
            has_theme_video,
            has_subtitles,
            has_special_feature,
            has_trailer,
            adjacent_to,
            parent_index_number,
            has_parental_rating,
            is_hd,
            is_4_k,
            location_types,
            exclude_location_types,
            is_missing,
            is_unaired,
            min_community_rating,
            min_critic_rating,
            min_premiere_date,
            min_date_last_saved,
            min_date_last_saved_for_user,
            max_premiere_date,
            has_overview,
            has_imdb_id,
            has_tmdb_id,
            has_tvdb_id,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            exclude_item_ids,
            start_index,
            limit,
            recursive,
            search_term,
            sort_order,
            parent_id,
            fields,
            exclude_item_types,
            filters,
            is_favorite,
            media_types,
            image_types,
            sort_by,
            is_played,
            genres,
            official_ratings,
            tags,
            years,
            enable_user_data,
            image_type_limit,
            enable_image_types,
            person,
            person_ids,
            person_types,
            studios,
            artists,
            exclude_artist_ids,
            artist_ids,
            album_artist_ids,
            contributing_artist_ids,
            albums,
            album_ids,
            ids,
            video_types,
            min_official_rating,
            is_locked,
            is_place_holder,
            has_official_rating,
            collapse_box_set_items,
            min_width,
            min_height,
            max_width,
            max_height,
            is_3_d,
            series_status,
            name_starts_with_or_greater,
            name_starts_with,
            name_less_than,
            studio_ids,
            genre_ids,
            enable_total_record_count,
            enable_images,
        )

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = "application/json"

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )

    # Finds movies and trailers similar to a given trailer.
    def test_get_trailers_1(self):
        # Parameters for the API call
        user_id = None
        max_official_rating = None
        has_theme_song = None
        has_theme_video = None
        has_subtitles = None
        has_special_feature = None
        has_trailer = None
        adjacent_to = None
        parent_index_number = None
        has_parental_rating = None
        is_hd = None
        is_4_k = None
        location_types = None
        exclude_location_types = None
        is_missing = None
        is_unaired = None
        min_community_rating = None
        min_critic_rating = None
        min_premiere_date = None
        min_date_last_saved = None
        min_date_last_saved_for_user = None
        max_premiere_date = None
        has_overview = None
        has_imdb_id = None
        has_tmdb_id = None
        has_tvdb_id = None
        is_movie = None
        is_series = None
        is_news = None
        is_kids = None
        is_sports = None
        exclude_item_ids = None
        start_index = None
        limit = None
        recursive = None
        search_term = None
        sort_order = None
        parent_id = None
        fields = None
        exclude_item_types = None
        filters = None
        is_favorite = None
        media_types = None
        image_types = None
        sort_by = None
        is_played = None
        genres = None
        official_ratings = None
        tags = None
        years = None
        enable_user_data = None
        image_type_limit = None
        enable_image_types = None
        person = None
        person_ids = None
        person_types = None
        studios = None
        artists = None
        exclude_artist_ids = None
        artist_ids = None
        album_artist_ids = None
        contributing_artist_ids = None
        albums = None
        album_ids = None
        ids = None
        video_types = None
        min_official_rating = None
        is_locked = None
        is_place_holder = None
        has_official_rating = None
        collapse_box_set_items = None
        min_width = None
        min_height = None
        max_width = None
        max_height = None
        is_3_d = None
        series_status = None
        name_starts_with_or_greater = None
        name_starts_with = None
        name_less_than = None
        studio_ids = None
        genre_ids = None
        enable_total_record_count = True
        enable_images = True

        # Perform the API call through the SDK function
        result = self.controller.get_trailers(
            user_id,
            max_official_rating,
            has_theme_song,
            has_theme_video,
            has_subtitles,
            has_special_feature,
            has_trailer,
            adjacent_to,
            parent_index_number,
            has_parental_rating,
            is_hd,
            is_4_k,
            location_types,
            exclude_location_types,
            is_missing,
            is_unaired,
            min_community_rating,
            min_critic_rating,
            min_premiere_date,
            min_date_last_saved,
            min_date_last_saved_for_user,
            max_premiere_date,
            has_overview,
            has_imdb_id,
            has_tmdb_id,
            has_tvdb_id,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            exclude_item_ids,
            start_index,
            limit,
            recursive,
            search_term,
            sort_order,
            parent_id,
            fields,
            exclude_item_types,
            filters,
            is_favorite,
            media_types,
            image_types,
            sort_by,
            is_played,
            genres,
            official_ratings,
            tags,
            years,
            enable_user_data,
            image_type_limit,
            enable_image_types,
            person,
            person_ids,
            person_types,
            studios,
            artists,
            exclude_artist_ids,
            artist_ids,
            album_artist_ids,
            contributing_artist_ids,
            albums,
            album_ids,
            ids,
            video_types,
            min_official_rating,
            is_locked,
            is_place_holder,
            has_official_rating,
            collapse_box_set_items,
            min_width,
            min_height,
            max_width,
            max_height,
            is_3_d,
            series_status,
            name_starts_with_or_greater,
            name_starts_with,
            name_less_than,
            studio_ids,
            genre_ids,
            enable_total_record_count,
            enable_images,
        )

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = 'application/json; profile="CamelCase"'

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )

    # Finds movies and trailers similar to a given trailer.
    def test_get_trailers_2(self):
        # Parameters for the API call
        user_id = None
        max_official_rating = None
        has_theme_song = None
        has_theme_video = None
        has_subtitles = None
        has_special_feature = None
        has_trailer = None
        adjacent_to = None
        parent_index_number = None
        has_parental_rating = None
        is_hd = None
        is_4_k = None
        location_types = None
        exclude_location_types = None
        is_missing = None
        is_unaired = None
        min_community_rating = None
        min_critic_rating = None
        min_premiere_date = None
        min_date_last_saved = None
        min_date_last_saved_for_user = None
        max_premiere_date = None
        has_overview = None
        has_imdb_id = None
        has_tmdb_id = None
        has_tvdb_id = None
        is_movie = None
        is_series = None
        is_news = None
        is_kids = None
        is_sports = None
        exclude_item_ids = None
        start_index = None
        limit = None
        recursive = None
        search_term = None
        sort_order = None
        parent_id = None
        fields = None
        exclude_item_types = None
        filters = None
        is_favorite = None
        media_types = None
        image_types = None
        sort_by = None
        is_played = None
        genres = None
        official_ratings = None
        tags = None
        years = None
        enable_user_data = None
        image_type_limit = None
        enable_image_types = None
        person = None
        person_ids = None
        person_types = None
        studios = None
        artists = None
        exclude_artist_ids = None
        artist_ids = None
        album_artist_ids = None
        contributing_artist_ids = None
        albums = None
        album_ids = None
        ids = None
        video_types = None
        min_official_rating = None
        is_locked = None
        is_place_holder = None
        has_official_rating = None
        collapse_box_set_items = None
        min_width = None
        min_height = None
        max_width = None
        max_height = None
        is_3_d = None
        series_status = None
        name_starts_with_or_greater = None
        name_starts_with = None
        name_less_than = None
        studio_ids = None
        genre_ids = None
        enable_total_record_count = True
        enable_images = True

        # Perform the API call through the SDK function
        result = self.controller.get_trailers(
            user_id,
            max_official_rating,
            has_theme_song,
            has_theme_video,
            has_subtitles,
            has_special_feature,
            has_trailer,
            adjacent_to,
            parent_index_number,
            has_parental_rating,
            is_hd,
            is_4_k,
            location_types,
            exclude_location_types,
            is_missing,
            is_unaired,
            min_community_rating,
            min_critic_rating,
            min_premiere_date,
            min_date_last_saved,
            min_date_last_saved_for_user,
            max_premiere_date,
            has_overview,
            has_imdb_id,
            has_tmdb_id,
            has_tvdb_id,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            exclude_item_ids,
            start_index,
            limit,
            recursive,
            search_term,
            sort_order,
            parent_id,
            fields,
            exclude_item_types,
            filters,
            is_favorite,
            media_types,
            image_types,
            sort_by,
            is_played,
            genres,
            official_ratings,
            tags,
            years,
            enable_user_data,
            image_type_limit,
            enable_image_types,
            person,
            person_ids,
            person_types,
            studios,
            artists,
            exclude_artist_ids,
            artist_ids,
            album_artist_ids,
            contributing_artist_ids,
            albums,
            album_ids,
            ids,
            video_types,
            min_official_rating,
            is_locked,
            is_place_holder,
            has_official_rating,
            collapse_box_set_items,
            min_width,
            min_height,
            max_width,
            max_height,
            is_3_d,
            series_status,
            name_starts_with_or_greater,
            name_starts_with,
            name_less_than,
            studio_ids,
            genre_ids,
            enable_total_record_count,
            enable_images,
        )

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = 'application/json; profile="PascalCase"'

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )
