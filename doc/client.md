
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `x_emby_token` | `string` | API key header parameter |

The API client can be initialized as follows:

```python
from jellyfinapi.jellyfinapi_client import JellyfinapiClient
from jellyfinapi.configuration import Environment

client = JellyfinapiClient(
    x_emby_token='X-Emby-Token',
    environment=Environment.PRODUCTION,)
```

## Jellyfin API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| activity_log | Gets ActivityLogController |
| api_key | Gets ApiKeyController |
| artists | Gets ArtistsController |
| audio | Gets AudioController |
| branding | Gets BrandingController |
| channels | Gets ChannelsController |
| client_log | Gets ClientLogController |
| collection | Gets CollectionController |
| configuration | Gets ConfigurationController |
| dashboard | Gets DashboardController |
| devices | Gets DevicesController |
| display_preferences | Gets DisplayPreferencesController |
| dlna | Gets DlnaController |
| dlna_server | Gets DlnaServerController |
| dynamic_hls | Gets DynamicHlsController |
| endpoints | Gets EndpointsController |
| environment | Gets EnvironmentController |
| filter | Gets FilterController |
| genres | Gets GenresController |
| hls_segment | Gets HlsSegmentController |
| image | Gets ImageController |
| image_by_name | Gets ImageByNameController |
| instant_mix | Gets InstantMixController |
| item_lookup | Gets ItemLookupController |
| item_refresh | Gets ItemRefreshController |
| items | Gets ItemsController |
| library | Gets LibraryController |
| item_update | Gets ItemUpdateController |
| library_structure | Gets LibraryStructureController |
| live_tv | Gets LiveTvController |
| localization | Gets LocalizationController |
| media_info | Gets MediaInfoController |
| movies | Gets MoviesController |
| music_genres | Gets MusicGenresController |
| notifications | Gets NotificationsController |
| open_subtitles | Gets OpenSubtitlesController |
| package | Gets PackageController |
| persons | Gets PersonsController |
| playlists | Gets PlaylistsController |
| playstate | Gets PlaystateController |
| plugins | Gets PluginsController |
| quick_connect | Gets QuickConnectController |
| remote_image | Gets RemoteImageController |
| scheduled_tasks | Gets ScheduledTasksController |
| search | Gets SearchController |
| session | Gets SessionController |
| startup | Gets StartupController |
| studios | Gets StudiosController |
| subtitle | Gets SubtitleController |
| suggestions | Gets SuggestionsController |
| sync_play | Gets SyncPlayController |
| system | Gets SystemController |
| time_sync | Gets TimeSyncController |
| tmdb | Gets TmdbController |
| trailers | Gets TrailersController |
| trakt | Gets TraktController |
| tv_shows | Gets TvShowsController |
| universal_audio | Gets UniversalAudioController |
| user | Gets UserController |
| user_library | Gets UserLibraryController |
| user_views | Gets UserViewsController |
| video_attachments | Gets VideoAttachmentsController |
| videos | Gets VideosController |
| years | Gets YearsController |

