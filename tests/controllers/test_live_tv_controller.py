# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.listings_provider_info import ListingsProviderInfo
from jellyfinapi.models.get_programs_dto import GetProgramsDto
from jellyfinapi.models.series_timer_info_dto import SeriesTimerInfoDto
from jellyfinapi.models.timer_info_dto import TimerInfoDto
from jellyfinapi.models.tuner_host_info import TunerHostInfo


class LiveTvControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(LiveTvControllerTests, cls).setUpClass()
        cls.controller = cls.client.live_tv
        cls.response_catcher = cls.controller.http_call_back

    # Get channel mapping options.
    def test_get_channel_mapping_options(self):
        # Parameters for the API call
        provider_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_channel_mapping_options(provider_id)

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

    # Get channel mapping options.
    def test_get_channel_mapping_options_1(self):
        # Parameters for the API call
        provider_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_channel_mapping_options(provider_id)

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

    # Get channel mapping options.
    def test_get_channel_mapping_options_2(self):
        # Parameters for the API call
        provider_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_channel_mapping_options(provider_id)

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

    # Gets available live tv channels.
    def test_get_live_tv_channels(self):
        # Parameters for the API call
        mtype = None
        user_id = None
        start_index = None
        is_movie = None
        is_series = None
        is_news = None
        is_kids = None
        is_sports = None
        limit = None
        is_favorite = None
        is_liked = None
        is_disliked = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        fields = None
        enable_user_data = None
        sort_by = None
        sort_order = None
        enable_favorite_sorting = False
        add_current_program = True

        # Perform the API call through the SDK function
        result = self.controller.get_live_tv_channels(
            mtype,
            user_id,
            start_index,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            limit,
            is_favorite,
            is_liked,
            is_disliked,
            enable_images,
            image_type_limit,
            enable_image_types,
            fields,
            enable_user_data,
            sort_by,
            sort_order,
            enable_favorite_sorting,
            add_current_program,
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

    # Gets available live tv channels.
    def test_get_live_tv_channels_1(self):
        # Parameters for the API call
        mtype = None
        user_id = None
        start_index = None
        is_movie = None
        is_series = None
        is_news = None
        is_kids = None
        is_sports = None
        limit = None
        is_favorite = None
        is_liked = None
        is_disliked = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        fields = None
        enable_user_data = None
        sort_by = None
        sort_order = None
        enable_favorite_sorting = False
        add_current_program = True

        # Perform the API call through the SDK function
        result = self.controller.get_live_tv_channels(
            mtype,
            user_id,
            start_index,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            limit,
            is_favorite,
            is_liked,
            is_disliked,
            enable_images,
            image_type_limit,
            enable_image_types,
            fields,
            enable_user_data,
            sort_by,
            sort_order,
            enable_favorite_sorting,
            add_current_program,
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

    # Gets available live tv channels.
    def test_get_live_tv_channels_2(self):
        # Parameters for the API call
        mtype = None
        user_id = None
        start_index = None
        is_movie = None
        is_series = None
        is_news = None
        is_kids = None
        is_sports = None
        limit = None
        is_favorite = None
        is_liked = None
        is_disliked = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        fields = None
        enable_user_data = None
        sort_by = None
        sort_order = None
        enable_favorite_sorting = False
        add_current_program = True

        # Perform the API call through the SDK function
        result = self.controller.get_live_tv_channels(
            mtype,
            user_id,
            start_index,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            limit,
            is_favorite,
            is_liked,
            is_disliked,
            enable_images,
            image_type_limit,
            enable_image_types,
            fields,
            enable_user_data,
            sort_by,
            sort_order,
            enable_favorite_sorting,
            add_current_program,
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

    # Get guid info.
    def test_get_guide_info(self):

        # Perform the API call through the SDK function
        result = self.controller.get_guide_info()

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

    # Get guid info.
    def test_get_guide_info_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_guide_info()

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

    # Get guid info.
    def test_get_guide_info_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_guide_info()

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

    # Gets available live tv services.
    def test_get_live_tv_info(self):

        # Perform the API call through the SDK function
        result = self.controller.get_live_tv_info()

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

    # Gets available live tv services.
    def test_get_live_tv_info_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_live_tv_info()

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

    # Gets available live tv services.
    def test_get_live_tv_info_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_live_tv_info()

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

    # Adds a listings provider.
    def test_add_listing_provider(self):
        # Parameters for the API call
        pw = None
        validate_listings = False
        validate_login = False
        body = None

        # Perform the API call through the SDK function
        result = self.controller.add_listing_provider(
            pw, validate_listings, validate_login, body
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

    # Adds a listings provider.
    def test_add_listing_provider_1(self):
        # Parameters for the API call
        pw = None
        validate_listings = False
        validate_login = False
        body = None

        # Perform the API call through the SDK function
        result = self.controller.add_listing_provider(
            pw, validate_listings, validate_login, body
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

    # Adds a listings provider.
    def test_add_listing_provider_2(self):
        # Parameters for the API call
        pw = None
        validate_listings = False
        validate_login = False
        body = None

        # Perform the API call through the SDK function
        result = self.controller.add_listing_provider(
            pw, validate_listings, validate_login, body
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

    # Delete listing provider.
    def test_delete_listing_provider(self):
        # Parameters for the API call
        id = None

        # Perform the API call through the SDK function
        self.controller.delete_listing_provider(id)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets default listings provider info.
    def test_get_default_listing_provider(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_listing_provider()

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

    # Gets default listings provider info.
    def test_get_default_listing_provider_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_listing_provider()

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

    # Gets default listings provider info.
    def test_get_default_listing_provider_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_listing_provider()

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

    # Gets available lineups.
    def test_get_lineups(self):
        # Parameters for the API call
        id = None
        mtype = None
        location = None
        country = None

        # Perform the API call through the SDK function
        result = self.controller.get_lineups(id, mtype, location, country)

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

    # Gets available lineups.
    def test_get_lineups_1(self):
        # Parameters for the API call
        id = None
        mtype = None
        location = None
        country = None

        # Perform the API call through the SDK function
        result = self.controller.get_lineups(id, mtype, location, country)

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

    # Gets available lineups.
    def test_get_lineups_2(self):
        # Parameters for the API call
        id = None
        mtype = None
        location = None
        country = None

        # Perform the API call through the SDK function
        result = self.controller.get_lineups(id, mtype, location, country)

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

    # Gets available countries.
    def test_get_schedules_direct_countries(self):

        # Perform the API call through the SDK function
        result = self.controller.get_schedules_direct_countries()

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

    # Gets available live tv epgs.
    def test_get_live_tv_programs(self):
        # Parameters for the API call
        channel_ids = None
        user_id = None
        min_start_date = None
        has_aired = None
        is_airing = None
        max_start_date = None
        min_end_date = None
        max_end_date = None
        is_movie = None
        is_series = None
        is_news = None
        is_kids = None
        is_sports = None
        start_index = None
        limit = None
        sort_by = None
        sort_order = None
        genres = None
        genre_ids = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        enable_user_data = None
        series_timer_id = None
        library_series_id = None
        fields = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_live_tv_programs(
            channel_ids,
            user_id,
            min_start_date,
            has_aired,
            is_airing,
            max_start_date,
            min_end_date,
            max_end_date,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            start_index,
            limit,
            sort_by,
            sort_order,
            genres,
            genre_ids,
            enable_images,
            image_type_limit,
            enable_image_types,
            enable_user_data,
            series_timer_id,
            library_series_id,
            fields,
            enable_total_record_count,
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

    # Gets available live tv epgs.
    def test_get_live_tv_programs_1(self):
        # Parameters for the API call
        channel_ids = None
        user_id = None
        min_start_date = None
        has_aired = None
        is_airing = None
        max_start_date = None
        min_end_date = None
        max_end_date = None
        is_movie = None
        is_series = None
        is_news = None
        is_kids = None
        is_sports = None
        start_index = None
        limit = None
        sort_by = None
        sort_order = None
        genres = None
        genre_ids = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        enable_user_data = None
        series_timer_id = None
        library_series_id = None
        fields = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_live_tv_programs(
            channel_ids,
            user_id,
            min_start_date,
            has_aired,
            is_airing,
            max_start_date,
            min_end_date,
            max_end_date,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            start_index,
            limit,
            sort_by,
            sort_order,
            genres,
            genre_ids,
            enable_images,
            image_type_limit,
            enable_image_types,
            enable_user_data,
            series_timer_id,
            library_series_id,
            fields,
            enable_total_record_count,
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

    # Gets available live tv epgs.
    def test_get_live_tv_programs_2(self):
        # Parameters for the API call
        channel_ids = None
        user_id = None
        min_start_date = None
        has_aired = None
        is_airing = None
        max_start_date = None
        min_end_date = None
        max_end_date = None
        is_movie = None
        is_series = None
        is_news = None
        is_kids = None
        is_sports = None
        start_index = None
        limit = None
        sort_by = None
        sort_order = None
        genres = None
        genre_ids = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        enable_user_data = None
        series_timer_id = None
        library_series_id = None
        fields = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_live_tv_programs(
            channel_ids,
            user_id,
            min_start_date,
            has_aired,
            is_airing,
            max_start_date,
            min_end_date,
            max_end_date,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            start_index,
            limit,
            sort_by,
            sort_order,
            genres,
            genre_ids,
            enable_images,
            image_type_limit,
            enable_image_types,
            enable_user_data,
            series_timer_id,
            library_series_id,
            fields,
            enable_total_record_count,
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

    # Gets available live tv epgs.
    def test_get_programs(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        result = self.controller.get_programs(body)

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

    # Gets available live tv epgs.
    def test_get_programs_1(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        result = self.controller.get_programs(body)

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

    # Gets available live tv epgs.
    def test_get_programs_2(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        result = self.controller.get_programs(body)

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

    # Gets recommended live tv epgs.
    def test_get_recommended_programs(self):
        # Parameters for the API call
        user_id = None
        limit = None
        is_airing = None
        has_aired = None
        is_series = None
        is_movie = None
        is_news = None
        is_kids = None
        is_sports = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        genre_ids = None
        fields = None
        enable_user_data = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_recommended_programs(
            user_id,
            limit,
            is_airing,
            has_aired,
            is_series,
            is_movie,
            is_news,
            is_kids,
            is_sports,
            enable_images,
            image_type_limit,
            enable_image_types,
            genre_ids,
            fields,
            enable_user_data,
            enable_total_record_count,
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

    # Gets recommended live tv epgs.
    def test_get_recommended_programs_1(self):
        # Parameters for the API call
        user_id = None
        limit = None
        is_airing = None
        has_aired = None
        is_series = None
        is_movie = None
        is_news = None
        is_kids = None
        is_sports = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        genre_ids = None
        fields = None
        enable_user_data = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_recommended_programs(
            user_id,
            limit,
            is_airing,
            has_aired,
            is_series,
            is_movie,
            is_news,
            is_kids,
            is_sports,
            enable_images,
            image_type_limit,
            enable_image_types,
            genre_ids,
            fields,
            enable_user_data,
            enable_total_record_count,
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

    # Gets recommended live tv epgs.
    def test_get_recommended_programs_2(self):
        # Parameters for the API call
        user_id = None
        limit = None
        is_airing = None
        has_aired = None
        is_series = None
        is_movie = None
        is_news = None
        is_kids = None
        is_sports = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        genre_ids = None
        fields = None
        enable_user_data = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_recommended_programs(
            user_id,
            limit,
            is_airing,
            has_aired,
            is_series,
            is_movie,
            is_news,
            is_kids,
            is_sports,
            enable_images,
            image_type_limit,
            enable_image_types,
            genre_ids,
            fields,
            enable_user_data,
            enable_total_record_count,
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

    # Gets live tv recordings.
    def test_get_recordings(self):
        # Parameters for the API call
        channel_id = None
        user_id = None
        start_index = None
        limit = None
        status = None
        is_in_progress = None
        series_timer_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        fields = None
        enable_user_data = None
        is_movie = None
        is_series = None
        is_kids = None
        is_sports = None
        is_news = None
        is_library_item = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_recordings(
            channel_id,
            user_id,
            start_index,
            limit,
            status,
            is_in_progress,
            series_timer_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            fields,
            enable_user_data,
            is_movie,
            is_series,
            is_kids,
            is_sports,
            is_news,
            is_library_item,
            enable_total_record_count,
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

    # Gets live tv recordings.
    def test_get_recordings_1(self):
        # Parameters for the API call
        channel_id = None
        user_id = None
        start_index = None
        limit = None
        status = None
        is_in_progress = None
        series_timer_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        fields = None
        enable_user_data = None
        is_movie = None
        is_series = None
        is_kids = None
        is_sports = None
        is_news = None
        is_library_item = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_recordings(
            channel_id,
            user_id,
            start_index,
            limit,
            status,
            is_in_progress,
            series_timer_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            fields,
            enable_user_data,
            is_movie,
            is_series,
            is_kids,
            is_sports,
            is_news,
            is_library_item,
            enable_total_record_count,
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

    # Gets live tv recordings.
    def test_get_recordings_2(self):
        # Parameters for the API call
        channel_id = None
        user_id = None
        start_index = None
        limit = None
        status = None
        is_in_progress = None
        series_timer_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        fields = None
        enable_user_data = None
        is_movie = None
        is_series = None
        is_kids = None
        is_sports = None
        is_news = None
        is_library_item = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_recordings(
            channel_id,
            user_id,
            start_index,
            limit,
            status,
            is_in_progress,
            series_timer_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            fields,
            enable_user_data,
            is_movie,
            is_series,
            is_kids,
            is_sports,
            is_news,
            is_library_item,
            enable_total_record_count,
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

    # Gets recording folders.
    def test_get_recording_folders(self):
        # Parameters for the API call
        user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_recording_folders(user_id)

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

    # Gets recording folders.
    def test_get_recording_folders_1(self):
        # Parameters for the API call
        user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_recording_folders(user_id)

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

    # Gets recording folders.
    def test_get_recording_folders_2(self):
        # Parameters for the API call
        user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_recording_folders(user_id)

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

    # Gets live tv recording groups.
    def test_get_recording_groups(self):
        # Parameters for the API call
        user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_recording_groups(user_id)

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

    # Gets live tv recording groups.
    def test_get_recording_groups_1(self):
        # Parameters for the API call
        user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_recording_groups(user_id)

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

    # Gets live tv recording groups.
    def test_get_recording_groups_2(self):
        # Parameters for the API call
        user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_recording_groups(user_id)

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

    # Gets live tv recording series.
    def test_get_recordings_series(self):
        # Parameters for the API call
        channel_id = None
        user_id = None
        group_id = None
        start_index = None
        limit = None
        status = None
        is_in_progress = None
        series_timer_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        fields = None
        enable_user_data = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_recordings_series(
            channel_id,
            user_id,
            group_id,
            start_index,
            limit,
            status,
            is_in_progress,
            series_timer_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            fields,
            enable_user_data,
            enable_total_record_count,
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

    # Gets live tv recording series.
    def test_get_recordings_series_1(self):
        # Parameters for the API call
        channel_id = None
        user_id = None
        group_id = None
        start_index = None
        limit = None
        status = None
        is_in_progress = None
        series_timer_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        fields = None
        enable_user_data = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_recordings_series(
            channel_id,
            user_id,
            group_id,
            start_index,
            limit,
            status,
            is_in_progress,
            series_timer_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            fields,
            enable_user_data,
            enable_total_record_count,
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

    # Gets live tv recording series.
    def test_get_recordings_series_2(self):
        # Parameters for the API call
        channel_id = None
        user_id = None
        group_id = None
        start_index = None
        limit = None
        status = None
        is_in_progress = None
        series_timer_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        fields = None
        enable_user_data = None
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_recordings_series(
            channel_id,
            user_id,
            group_id,
            start_index,
            limit,
            status,
            is_in_progress,
            series_timer_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            fields,
            enable_user_data,
            enable_total_record_count,
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

    # Gets live tv series timers.
    def test_get_series_timers(self):
        # Parameters for the API call
        sort_by = None
        sort_order = None

        # Perform the API call through the SDK function
        result = self.controller.get_series_timers(sort_by, sort_order)

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

    # Gets live tv series timers.
    def test_get_series_timers_1(self):
        # Parameters for the API call
        sort_by = None
        sort_order = None

        # Perform the API call through the SDK function
        result = self.controller.get_series_timers(sort_by, sort_order)

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

    # Gets live tv series timers.
    def test_get_series_timers_2(self):
        # Parameters for the API call
        sort_by = None
        sort_order = None

        # Perform the API call through the SDK function
        result = self.controller.get_series_timers(sort_by, sort_order)

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

    # Creates a live tv series timer.
    def test_create_series_timer(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.create_series_timer(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets the live tv timers.
    def test_get_timers(self):
        # Parameters for the API call
        channel_id = None
        series_timer_id = None
        is_active = None
        is_scheduled = None

        # Perform the API call through the SDK function
        result = self.controller.get_timers(
            channel_id, series_timer_id, is_active, is_scheduled
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

    # Gets the live tv timers.
    def test_get_timers_1(self):
        # Parameters for the API call
        channel_id = None
        series_timer_id = None
        is_active = None
        is_scheduled = None

        # Perform the API call through the SDK function
        result = self.controller.get_timers(
            channel_id, series_timer_id, is_active, is_scheduled
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

    # Gets the live tv timers.
    def test_get_timers_2(self):
        # Parameters for the API call
        channel_id = None
        series_timer_id = None
        is_active = None
        is_scheduled = None

        # Perform the API call through the SDK function
        result = self.controller.get_timers(
            channel_id, series_timer_id, is_active, is_scheduled
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

    # Creates a live tv timer.
    def test_create_timer(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.create_timer(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets the default values for a new timer.
    def test_get_default_timer(self):
        # Parameters for the API call
        program_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_default_timer(program_id)

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

    # Gets the default values for a new timer.
    def test_get_default_timer_1(self):
        # Parameters for the API call
        program_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_default_timer(program_id)

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

    # Gets the default values for a new timer.
    def test_get_default_timer_2(self):
        # Parameters for the API call
        program_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_default_timer(program_id)

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

    # Adds a tuner host.
    def test_add_tuner_host(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        result = self.controller.add_tuner_host(body)

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

    # Adds a tuner host.
    def test_add_tuner_host_1(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        result = self.controller.add_tuner_host(body)

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

    # Adds a tuner host.
    def test_add_tuner_host_2(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        result = self.controller.add_tuner_host(body)

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

    # Deletes a tuner host.
    def test_delete_tuner_host(self):
        # Parameters for the API call
        id = None

        # Perform the API call through the SDK function
        self.controller.delete_tuner_host(id)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Get tuner host types.
    def test_get_tuner_host_types(self):

        # Perform the API call through the SDK function
        result = self.controller.get_tuner_host_types()

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

    # Get tuner host types.
    def test_get_tuner_host_types_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_tuner_host_types()

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

    # Get tuner host types.
    def test_get_tuner_host_types_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_tuner_host_types()

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

    # Discover tuners.
    def test_discover_tuners(self):
        # Parameters for the API call
        new_devices_only = False

        # Perform the API call through the SDK function
        result = self.controller.discover_tuners(new_devices_only)

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

    # Discover tuners.
    def test_discover_tuners_1(self):
        # Parameters for the API call
        new_devices_only = False

        # Perform the API call through the SDK function
        result = self.controller.discover_tuners(new_devices_only)

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

    # Discover tuners.
    def test_discover_tuners_2(self):
        # Parameters for the API call
        new_devices_only = False

        # Perform the API call through the SDK function
        result = self.controller.discover_tuners(new_devices_only)

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

    # Discover tuners.
    def test_discvover_tuners(self):
        # Parameters for the API call
        new_devices_only = False

        # Perform the API call through the SDK function
        result = self.controller.discvover_tuners(new_devices_only)

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

    # Discover tuners.
    def test_discvover_tuners_1(self):
        # Parameters for the API call
        new_devices_only = False

        # Perform the API call through the SDK function
        result = self.controller.discvover_tuners(new_devices_only)

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

    # Discover tuners.
    def test_discvover_tuners_2(self):
        # Parameters for the API call
        new_devices_only = False

        # Perform the API call through the SDK function
        result = self.controller.discvover_tuners(new_devices_only)

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
