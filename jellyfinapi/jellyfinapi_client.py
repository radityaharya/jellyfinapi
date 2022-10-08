# -*- coding: utf-8 -*-


from jellyfinapi.decorators import lazy_property
from jellyfinapi.configuration import Configuration
from jellyfinapi.configuration import Environment
from jellyfinapi.http.auth.custom_header_authentication import (
    CustomHeaderAuthentication,
)
from jellyfinapi.controllers.activity_log_controller import ActivityLogController
from jellyfinapi.controllers.api_key_controller import ApiKeyController
from jellyfinapi.controllers.artists_controller import ArtistsController
from jellyfinapi.controllers.audio_controller import AudioController
from jellyfinapi.controllers.branding_controller import BrandingController
from jellyfinapi.controllers.channels_controller import ChannelsController
from jellyfinapi.controllers.client_log_controller import ClientLogController
from jellyfinapi.controllers.collection_controller import CollectionController
from jellyfinapi.controllers.configuration_controller import ConfigurationController
from jellyfinapi.controllers.dashboard_controller import DashboardController
from jellyfinapi.controllers.devices_controller import DevicesController
from jellyfinapi.controllers.display_preferences_controller import (
    DisplayPreferencesController,
)
from jellyfinapi.controllers.dlna_controller import DlnaController
from jellyfinapi.controllers.dlna_server_controller import DlnaServerController
from jellyfinapi.controllers.dynamic_hls_controller import DynamicHlsController
from jellyfinapi.controllers.endpoints_controller import EndpointsController
from jellyfinapi.controllers.environment_controller import EnvironmentController
from jellyfinapi.controllers.filter_controller import FilterController
from jellyfinapi.controllers.genres_controller import GenresController
from jellyfinapi.controllers.hls_segment_controller import HlsSegmentController
from jellyfinapi.controllers.image_controller import ImageController
from jellyfinapi.controllers.image_by_name_controller import ImageByNameController
from jellyfinapi.controllers.instant_mix_controller import InstantMixController
from jellyfinapi.controllers.item_lookup_controller import ItemLookupController
from jellyfinapi.controllers.item_refresh_controller import ItemRefreshController
from jellyfinapi.controllers.items_controller import ItemsController
from jellyfinapi.controllers.library_controller import LibraryController
from jellyfinapi.controllers.item_update_controller import ItemUpdateController
from jellyfinapi.controllers.library_structure_controller import (
    LibraryStructureController,
)
from jellyfinapi.controllers.live_tv_controller import LiveTvController
from jellyfinapi.controllers.localization_controller import LocalizationController
from jellyfinapi.controllers.media_info_controller import MediaInfoController
from jellyfinapi.controllers.movies_controller import MoviesController
from jellyfinapi.controllers.music_genres_controller import MusicGenresController
from jellyfinapi.controllers.notifications_controller import NotificationsController
from jellyfinapi.controllers.open_subtitles_controller import OpenSubtitlesController
from jellyfinapi.controllers.package_controller import PackageController
from jellyfinapi.controllers.persons_controller import PersonsController
from jellyfinapi.controllers.playlists_controller import PlaylistsController
from jellyfinapi.controllers.playstate_controller import PlaystateController
from jellyfinapi.controllers.plugins_controller import PluginsController
from jellyfinapi.controllers.quick_connect_controller import QuickConnectController
from jellyfinapi.controllers.remote_image_controller import RemoteImageController
from jellyfinapi.controllers.scheduled_tasks_controller import ScheduledTasksController
from jellyfinapi.controllers.search_controller import SearchController
from jellyfinapi.controllers.session_controller import SessionController
from jellyfinapi.controllers.startup_controller import StartupController
from jellyfinapi.controllers.studios_controller import StudiosController
from jellyfinapi.controllers.subtitle_controller import SubtitleController
from jellyfinapi.controllers.suggestions_controller import SuggestionsController
from jellyfinapi.controllers.sync_play_controller import SyncPlayController
from jellyfinapi.controllers.system_controller import SystemController
from jellyfinapi.controllers.time_sync_controller import TimeSyncController
from jellyfinapi.controllers.tmdb_controller import TmdbController
from jellyfinapi.controllers.trailers_controller import TrailersController
from jellyfinapi.controllers.trakt_controller import TraktController
from jellyfinapi.controllers.tv_shows_controller import TvShowsController
from jellyfinapi.controllers.universal_audio_controller import UniversalAudioController
from jellyfinapi.controllers.user_controller import UserController
from jellyfinapi.controllers.user_library_controller import UserLibraryController
from jellyfinapi.controllers.user_views_controller import UserViewsController
from jellyfinapi.controllers.video_attachments_controller import (
    VideoAttachmentsController,
)
from jellyfinapi.controllers.videos_controller import VideosController
from jellyfinapi.controllers.years_controller import YearsController
from jellyfinapi.configuration import Server, Environment

class JellyfinapiClient(object):
    @lazy_property
    def activity_log(self):
        return ActivityLogController(self.config, self.auth_managers)

    @lazy_property
    def api_key(self):
        return ApiKeyController(self.config, self.auth_managers)

    @lazy_property
    def artists(self):
        return ArtistsController(self.config, self.auth_managers)

    @lazy_property
    def audio(self):
        return AudioController(self.config, self.auth_managers)

    @lazy_property
    def branding(self):
        return BrandingController(self.config, self.auth_managers)

    @lazy_property
    def channels(self):
        return ChannelsController(self.config, self.auth_managers)

    @lazy_property
    def client_log(self):
        return ClientLogController(self.config, self.auth_managers)

    @lazy_property
    def collection(self):
        return CollectionController(self.config, self.auth_managers)

    @lazy_property
    def configuration(self):
        return ConfigurationController(self.config, self.auth_managers)

    @lazy_property
    def dashboard(self):
        return DashboardController(self.config, self.auth_managers)

    @lazy_property
    def devices(self):
        return DevicesController(self.config, self.auth_managers)

    @lazy_property
    def display_preferences(self):
        return DisplayPreferencesController(self.config, self.auth_managers)

    @lazy_property
    def dlna(self):
        return DlnaController(self.config, self.auth_managers)

    @lazy_property
    def dlna_server(self):
        return DlnaServerController(self.config, self.auth_managers)

    @lazy_property
    def dynamic_hls(self):
        return DynamicHlsController(self.config, self.auth_managers)

    @lazy_property
    def endpoints(self):
        return EndpointsController(self.config, self.auth_managers)

    @lazy_property
    def environment(self):
        return EnvironmentController(self.config, self.auth_managers)

    @lazy_property
    def filter(self):
        return FilterController(self.config, self.auth_managers)

    @lazy_property
    def genres(self):
        return GenresController(self.config, self.auth_managers)

    @lazy_property
    def hls_segment(self):
        return HlsSegmentController(self.config, self.auth_managers)

    @lazy_property
    def image(self):
        return ImageController(self.config, self.auth_managers)

    @lazy_property
    def image_by_name(self):
        return ImageByNameController(self.config, self.auth_managers)

    @lazy_property
    def instant_mix(self):
        return InstantMixController(self.config, self.auth_managers)

    @lazy_property
    def item_lookup(self):
        return ItemLookupController(self.config, self.auth_managers)

    @lazy_property
    def item_refresh(self):
        return ItemRefreshController(self.config, self.auth_managers)

    @lazy_property
    def items(self):
        return ItemsController(self.config, self.auth_managers)

    @lazy_property
    def library(self):
        return LibraryController(self.config, self.auth_managers)

    @lazy_property
    def item_update(self):
        return ItemUpdateController(self.config, self.auth_managers)

    @lazy_property
    def library_structure(self):
        return LibraryStructureController(self.config, self.auth_managers)

    @lazy_property
    def live_tv(self):
        return LiveTvController(self.config, self.auth_managers)

    @lazy_property
    def localization(self):
        return LocalizationController(self.config, self.auth_managers)

    @lazy_property
    def media_info(self):
        return MediaInfoController(self.config, self.auth_managers)

    @lazy_property
    def movies(self):
        return MoviesController(self.config, self.auth_managers)

    @lazy_property
    def music_genres(self):
        return MusicGenresController(self.config, self.auth_managers)

    @lazy_property
    def notifications(self):
        return NotificationsController(self.config, self.auth_managers)

    @lazy_property
    def open_subtitles(self):
        return OpenSubtitlesController(self.config, self.auth_managers)

    @lazy_property
    def package(self):
        return PackageController(self.config, self.auth_managers)

    @lazy_property
    def persons(self):
        return PersonsController(self.config, self.auth_managers)

    @lazy_property
    def playlists(self):
        return PlaylistsController(self.config, self.auth_managers)

    @lazy_property
    def playstate(self):
        return PlaystateController(self.config, self.auth_managers)

    @lazy_property
    def plugins(self):
        return PluginsController(self.config, self.auth_managers)

    @lazy_property
    def quick_connect(self):
        return QuickConnectController(self.config, self.auth_managers)

    @lazy_property
    def remote_image(self):
        return RemoteImageController(self.config, self.auth_managers)

    @lazy_property
    def scheduled_tasks(self):
        return ScheduledTasksController(self.config, self.auth_managers)

    @lazy_property
    def search(self):
        return SearchController(self.config, self.auth_managers)

    @lazy_property
    def session(self):
        return SessionController(self.config, self.auth_managers)

    @lazy_property
    def startup(self):
        return StartupController(self.config, self.auth_managers)

    @lazy_property
    def studios(self):
        return StudiosController(self.config, self.auth_managers)

    @lazy_property
    def subtitle(self):
        return SubtitleController(self.config, self.auth_managers)

    @lazy_property
    def suggestions(self):
        return SuggestionsController(self.config, self.auth_managers)

    @lazy_property
    def sync_play(self):
        return SyncPlayController(self.config, self.auth_managers)

    @lazy_property
    def system(self):
        return SystemController(self.config, self.auth_managers)

    @lazy_property
    def time_sync(self):
        return TimeSyncController(self.config, self.auth_managers)

    @lazy_property
    def tmdb(self):
        return TmdbController(self.config, self.auth_managers)

    @lazy_property
    def trailers(self):
        return TrailersController(self.config, self.auth_managers)

    @lazy_property
    def trakt(self):
        return TraktController(self.config, self.auth_managers)

    @lazy_property
    def tv_shows(self):
        return TvShowsController(self.config, self.auth_managers)

    @lazy_property
    def universal_audio(self):
        return UniversalAudioController(self.config, self.auth_managers)

    @lazy_property
    def user(self):
        return UserController(self.config, self.auth_managers)

    @lazy_property
    def user_library(self):
        return UserLibraryController(self.config, self.auth_managers)

    @lazy_property
    def user_views(self):
        return UserViewsController(self.config, self.auth_managers)

    @lazy_property
    def video_attachments(self):
        return VideoAttachmentsController(self.config, self.auth_managers)

    @lazy_property
    def videos(self):
        return VideosController(self.config, self.auth_managers)

    @lazy_property
    def years(self):
        return YearsController(self.config, self.auth_managers)

    def __init__(
        self,
        http_client_instance=None,
        override_http_client_configuration=False,
        http_call_back=None,
        timeout=60,
        max_retries=0,
        backoff_factor=2,
        retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
        retry_methods=["GET", "PUT"],
        environment=Environment.PRODUCTION,
        server_url = None,
        x_emby_token=None,
        config=None,
    ):
        if config is None:
            
            self.config = Configuration(
                http_client_instance=http_client_instance,
                override_http_client_configuration=override_http_client_configuration,
                http_call_back=http_call_back,
                timeout=timeout,
                max_retries=max_retries,
                backoff_factor=backoff_factor,
                retry_statuses=retry_statuses,
                retry_methods=retry_methods,
                environment=environment,
                server_url=server_url,
                x_emby_token=x_emby_token,
            )
        else:
            self.config = config
        self.initialize_auth_managers(self.config)

    def initialize_auth_managers(self, config):
        self.auth_managers = {key: None for key in ["global"]}
        self.auth_managers["global"] = CustomHeaderAuthentication(config.x_emby_token)
        return self.auth_managers
