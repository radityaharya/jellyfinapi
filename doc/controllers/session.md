# Session

```python
session_controller = client.session
```

## Class Name

`SessionController`

## Methods

* [Add User to Session](../../doc/controllers/session.md#add-user-to-session)
* [Display Content](../../doc/controllers/session.md#display-content)
* [Get Auth Providers](../../doc/controllers/session.md#get-auth-providers)
* [Get Password Reset Providers](../../doc/controllers/session.md#get-password-reset-providers)
* [Get Sessions](../../doc/controllers/session.md#get-sessions)
* [Play](../../doc/controllers/session.md#play)
* [Post Capabilities](../../doc/controllers/session.md#post-capabilities)
* [Post Full Capabilities](../../doc/controllers/session.md#post-full-capabilities)
* [Remove User From Session](../../doc/controllers/session.md#remove-user-from-session)
* [Report Session Ended](../../doc/controllers/session.md#report-session-ended)
* [Report Viewing](../../doc/controllers/session.md#report-viewing)
* [Send Full General Command](../../doc/controllers/session.md#send-full-general-command)
* [Send General Command](../../doc/controllers/session.md#send-general-command)
* [Send Message Command](../../doc/controllers/session.md#send-message-command)
* [Send Playstate Command](../../doc/controllers/session.md#send-playstate-command)
* [Send System Command](../../doc/controllers/session.md#send-system-command)


# Add User to Session

Adds an additional user to a session.

```python
def add_user_to_session(self,
                       session_id,
                       user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `string` | Template, Required | The session id. |
| `user_id` | `uuid\|string` | Template, Required | The user id. |

## Response Type

`void`

## Example Usage

```python
session_id = 'sessionId8'
user_id = '000013ec-0000-0000-0000-000000000000'

result = session_controller.add_user_to_session(session_id, user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Display Content

Instructs a session to browse to an item or view.

```python
def display_content(self,
                   session_id,
                   item_type,
                   item_id,
                   item_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `string` | Template, Required | The session Id. |
| `item_type` | [`BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Required | The type of item to browse to. |
| `item_id` | `string` | Query, Required | The Id of the item. |
| `item_name` | `string` | Query, Required | The name of the item. |

## Response Type

`void`

## Example Usage

```python
session_id = 'sessionId8'
item_type = BaseItemKindEnum.LIVETVPROGRAM
item_id = 'itemId8'
item_name = 'itemName0'

result = session_controller.display_content(session_id, item_type, item_id, item_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Auth Providers

Get all auth providers.

```python
def get_auth_providers(self)
```

## Response Type

[`List of NameIdPair`](../../doc/models/name-id-pair.md)

## Example Usage

```python
result = session_controller.get_auth_providers()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Password Reset Providers

Get all password reset providers.

```python
def get_password_reset_providers(self)
```

## Response Type

[`List of NameIdPair`](../../doc/models/name-id-pair.md)

## Example Usage

```python
result = session_controller.get_password_reset_providers()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Sessions

Gets a list of sessions.

```python
def get_sessions(self,
                controllable_by_user_id=None,
                device_id=None,
                active_within_seconds=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `controllable_by_user_id` | `uuid\|string` | Query, Optional | Filter by sessions that a given user is allowed to remote control. |
| `device_id` | `string` | Query, Optional | Filter by device Id. |
| `active_within_seconds` | `int` | Query, Optional | Optional. Filter by sessions that were active in the last n seconds. |

## Response Type

[`List of SessionInfo`](../../doc/models/session-info.md)

## Example Usage

```python
result = session_controller.get_sessions()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Play

Instructs a session to play an item.

```python
def play(self,
        session_id,
        play_command,
        item_ids,
        start_position_ticks=None,
        media_source_id=None,
        audio_stream_index=None,
        subtitle_stream_index=None,
        start_index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `string` | Template, Required | The session id. |
| `play_command` | [`PlayCommandEnum`](../../doc/models/play-command-enum.md) | Query, Required | The type of play command to issue (PlayNow, PlayNext, PlayLast). Clients who have not yet implemented play next and play last may play now. |
| `item_ids` | `List of uuid\|string` | Query, Required | The ids of the items to play, comma delimited. |
| `start_position_ticks` | `long\|int` | Query, Optional | The starting position of the first item. |
| `media_source_id` | `string` | Query, Optional | Optional. The media source id. |
| `audio_stream_index` | `int` | Query, Optional | Optional. The index of the audio stream to play. |
| `subtitle_stream_index` | `int` | Query, Optional | Optional. The index of the subtitle stream to play. |
| `start_index` | `int` | Query, Optional | Optional. The start index. |

## Response Type

`void`

## Example Usage

```python
session_id = 'sessionId8'
play_command = PlayCommandEnum.PLAYNEXT
item_ids = ['00000f27-0000-0000-0000-000000000000', '00000f28-0000-0000-0000-000000000000']

result = session_controller.play(session_id, play_command, item_ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Post Capabilities

Updates capabilities for a device.

```python
def post_capabilities(self,
                     id=None,
                     playable_media_types=None,
                     supported_commands=None,
                     supports_media_control=False,
                     supports_sync=False,
                     supports_persistent_identifier=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Query, Optional | The session id. |
| `playable_media_types` | `List of string` | Query, Optional | A list of playable media types, comma delimited. Audio, Video, Book, Photo. |
| `supported_commands` | [`List of GeneralCommandTypeEnum`](../../doc/models/general-command-type-enum.md) | Query, Optional | A list of supported remote control commands, comma delimited. |
| `supports_media_control` | `bool` | Query, Optional | Determines whether media can be played remotely..<br>**Default**: `False` |
| `supports_sync` | `bool` | Query, Optional | Determines whether sync is supported.<br>**Default**: `False` |
| `supports_persistent_identifier` | `bool` | Query, Optional | Determines whether the device supports a unique identifier.<br>**Default**: `True` |

## Response Type

`void`

## Example Usage

```python
supports_media_control = False
supports_sync = False
supports_persistent_identifier = True

result = session_controller.post_capabilities(None, None, None, supports_media_control, supports_sync, supports_persistent_identifier)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Post Full Capabilities

Updates capabilities for a device.

```python
def post_full_capabilities(self,
                          body,
                          id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ClientCapabilitiesDto`](../../doc/models/client-capabilities-dto.md) | Body, Required | The MediaBrowser.Model.Session.ClientCapabilities. |
| `id` | `string` | Query, Optional | The session id. |

## Response Type

`void`

## Example Usage

```python
body = ClientCapabilitiesDto()

result = session_controller.post_full_capabilities(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Remove User From Session

Removes an additional user from a session.

```python
def remove_user_from_session(self,
                            session_id,
                            user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `string` | Template, Required | The session id. |
| `user_id` | `uuid\|string` | Template, Required | The user id. |

## Response Type

`void`

## Example Usage

```python
session_id = 'sessionId8'
user_id = '000013ec-0000-0000-0000-000000000000'

result = session_controller.remove_user_from_session(session_id, user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Report Session Ended

Reports that a session has ended.

```python
def report_session_ended(self)
```

## Response Type

`void`

## Example Usage

```python
result = session_controller.report_session_ended()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Report Viewing

Reports that a session is viewing an item.

```python
def report_viewing(self,
                  item_id,
                  session_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `string` | Query, Required | The item id. |
| `session_id` | `string` | Query, Optional | The session id. |

## Response Type

`void`

## Example Usage

```python
item_id = 'itemId8'

result = session_controller.report_viewing(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Send Full General Command

Issues a full general command to a client.

```python
def send_full_general_command(self,
                             session_id,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `string` | Template, Required | The session id. |
| `body` | [`GeneralCommand`](../../doc/models/general-command.md) | Body, Required | The MediaBrowser.Model.Session.GeneralCommand. |

## Response Type

`void`

## Example Usage

```python
session_id = 'sessionId8'
body = GeneralCommand()

result = session_controller.send_full_general_command(session_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Send General Command

Issues a general command to a client.

```python
def send_general_command(self,
                        session_id,
                        command)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `string` | Template, Required | The session id. |
| `command` | [`GeneralCommandTypeEnum`](../../doc/models/general-command-type-enum.md) | Template, Required | The command to send. |

## Response Type

`void`

## Example Usage

```python
session_id = 'sessionId8'
command = GeneralCommandTypeEnum.SETVOLUME

result = session_controller.send_general_command(session_id, command)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Send Message Command

Issues a command to a client to display a message to the user.

```python
def send_message_command(self,
                        session_id,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `string` | Template, Required | The session id. |
| `body` | [`MessageCommand`](../../doc/models/message-command.md) | Body, Required | The MediaBrowser.Model.Session.MessageCommand object containing Header, Message Text, and TimeoutMs. |

## Response Type

`void`

## Example Usage

```python
session_id = 'sessionId8'
body = MessageCommand()
body.text = 'Text8'

result = session_controller.send_message_command(session_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Send Playstate Command

Issues a playstate command to a client.

```python
def send_playstate_command(self,
                          session_id,
                          command,
                          seek_position_ticks=None,
                          controlling_user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `string` | Template, Required | The session id. |
| `command` | [`PlaystateCommandEnum`](../../doc/models/playstate-command-enum.md) | Template, Required | The MediaBrowser.Model.Session.PlaystateCommand. |
| `seek_position_ticks` | `long\|int` | Query, Optional | The optional position ticks. |
| `controlling_user_id` | `string` | Query, Optional | The optional controlling user id. |

## Response Type

`void`

## Example Usage

```python
session_id = 'sessionId8'
command = PlaystateCommandEnum.FASTFORWARD

result = session_controller.send_playstate_command(session_id, command)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Send System Command

Issues a system command to a client.

```python
def send_system_command(self,
                       session_id,
                       command)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `string` | Template, Required | The session id. |
| `command` | [`GeneralCommandTypeEnum`](../../doc/models/general-command-type-enum.md) | Template, Required | The command to send. |

## Response Type

`void`

## Example Usage

```python
session_id = 'sessionId8'
command = GeneralCommandTypeEnum.SETVOLUME

result = session_controller.send_system_command(session_id, command)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

