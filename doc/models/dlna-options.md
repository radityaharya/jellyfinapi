
# Dlna Options

The DlnaOptions class contains the user definable parameters for the dlna subsystems.

## Structure

`DlnaOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_play_to` | `bool` | Optional | Gets or sets a value indicating whether gets or sets a value to indicate the status of the dlna playTo subsystem. |
| `enable_server` | `bool` | Optional | Gets or sets a value indicating whether gets or sets a value to indicate the status of the dlna server subsystem. |
| `enable_debug_log` | `bool` | Optional | Gets or sets a value indicating whether detailed dlna server logs are sent to the console/log.<br>If the setting "Emby.Dlna": "Debug" msut be set in logging.default.json for this property to work. |
| `enable_play_to_tracing` | `bool` | Optional | Gets or sets a value indicating whether whether detailed playTo debug logs are sent to the console/log.<br>If the setting "Emby.Dlna.PlayTo": "Debug" msut be set in logging.default.json for this property to work. |
| `client_discovery_interval_seconds` | `int` | Optional | Gets or sets the ssdp client discovery interval time (in seconds).<br>This is the time after which the server will send a ssdp search request. |
| `alive_message_interval_seconds` | `int` | Optional | Gets or sets the frequency at which ssdp alive notifications are transmitted. |
| `blast_alive_message_interval_seconds` | `int` | Optional | Gets or sets the frequency at which ssdp alive notifications are transmitted. MIGRATING - TO BE REMOVED ONCE WEB HAS BEEN ALTERED. |
| `default_user_id` | `string` | Optional | Gets or sets the default user account that the dlna server uses. |
| `auto_create_play_to_profiles` | `bool` | Optional | Gets or sets a value indicating whether playTo device profiles should be created. |
| `blast_alive_messages` | `bool` | Optional | Gets or sets a value indicating whether to blast alive messages. |
| `send_only_matched_host` | `bool` | Optional | gets or sets a value indicating whether to send only matched host. |

## Example (as JSON)

```json
{
  "EnablePlayTo": null,
  "EnableServer": null,
  "EnableDebugLog": null,
  "EnablePlayToTracing": null,
  "ClientDiscoveryIntervalSeconds": null,
  "AliveMessageIntervalSeconds": null,
  "BlastAliveMessageIntervalSeconds": null,
  "DefaultUserId": null,
  "AutoCreatePlayToProfiles": null,
  "BlastAliveMessages": null,
  "SendOnlyMatchedHost": null
}
```

