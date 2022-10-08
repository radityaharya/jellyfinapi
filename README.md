
# Jellyfin API Client

Python interface to Jellyfin Instance

## Installation

### 1. Clone Project

Clone the project from GitHub:

```bash 
git clone https://github.com/radityaharya/jellyfinapi
```

### 2. Change Directory
```bash
cd jellyfinapi
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Package
```bash
pip install .
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

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
    x_emby_token='api key',
    server_url="your jellyfin server url",)
```

## Authorization

This API uses `X-Emby-Token` header.

## List of APIs

* [Activity Log](doc/controllers/activity-log.md)
* [Api Key](doc/controllers/api-key.md)
* [Artists](doc/controllers/artists.md)
* [Audio](doc/controllers/audio.md)
* [Branding](doc/controllers/branding.md)
* [Channels](doc/controllers/channels.md)
* [Client Log](doc/controllers/client-log.md)
* [Collection](doc/controllers/collection.md)
* [Configuration](doc/controllers/configuration.md)
* [Dashboard](doc/controllers/dashboard.md)
* [Devices](doc/controllers/devices.md)
* [Display Preferences](doc/controllers/display-preferences.md)
* [Dlna](doc/controllers/dlna.md)
* [Dlna Server](doc/controllers/dlna-server.md)
* [Dynamic Hls](doc/controllers/dynamic-hls.md)
* [Endpoints](doc/controllers/endpoints.md)
* [Environment](doc/controllers/environment.md)
* [Filter](doc/controllers/filter.md)
* [Genres](doc/controllers/genres.md)
* [Hls Segment](doc/controllers/hls-segment.md)
* [Image](doc/controllers/image.md)
* [Image by Name](doc/controllers/image-by-name.md)
* [Instant Mix](doc/controllers/instant-mix.md)
* [Item Lookup](doc/controllers/item-lookup.md)
* [Item Refresh](doc/controllers/item-refresh.md)
* [Items](doc/controllers/items.md)
* [Item Update](doc/controllers/item-update.md)
* [Library](doc/controllers/library.md)
* [Library Structure](doc/controllers/library-structure.md)
* [Live Tv](doc/controllers/live-tv.md)
* [Localization](doc/controllers/localization.md)
* [Media Info](doc/controllers/media-info.md)
* [Movies](doc/controllers/movies.md)
* [Music Genres](doc/controllers/music-genres.md)
* [Notifications](doc/controllers/notifications.md)
* [Open Subtitles](doc/controllers/open-subtitles.md)
* [Package](doc/controllers/package.md)
* [Persons](doc/controllers/persons.md)
* [Playlists](doc/controllers/playlists.md)
* [Playstate](doc/controllers/playstate.md)
* [Plugins](doc/controllers/plugins.md)
* [Quick Connect](doc/controllers/quick-connect.md)
* [Remote Image](doc/controllers/remote-image.md)
* [Scheduled Tasks](doc/controllers/scheduled-tasks.md)
* [Search](doc/controllers/search.md)
* [Session](doc/controllers/session.md)
* [Startup](doc/controllers/startup.md)
* [Studios](doc/controllers/studios.md)
* [Subtitle](doc/controllers/subtitle.md)
* [Suggestions](doc/controllers/suggestions.md)
* [Sync Play](doc/controllers/sync-play.md)
* [System](doc/controllers/system.md)
* [Time Sync](doc/controllers/time-sync.md)
* [Tmdb](doc/controllers/tmdb.md)
* [Trailers](doc/controllers/trailers.md)
* [Trakt](doc/controllers/trakt.md)
* [Tv Shows](doc/controllers/tv-shows.md)
* [Universal Audio](doc/controllers/universal-audio.md)
* [User](doc/controllers/user.md)
* [User Library](doc/controllers/user-library.md)
* [User Views](doc/controllers/user-views.md)
* [Video Attachments](doc/controllers/video-attachments.md)
* [Videos](doc/controllers/videos.md)
* [Years](doc/controllers/years.md)

## Classes Documentation

* [Utility Classes](doc/utility-classes.md)
* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

