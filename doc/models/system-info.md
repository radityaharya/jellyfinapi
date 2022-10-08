
# System Info

Class SystemInfo.

## Structure

`SystemInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `local_address` | `string` | Optional | Gets or sets the local address. |
| `server_name` | `string` | Optional | Gets or sets the name of the server. |
| `version` | `string` | Optional | Gets or sets the server version. |
| `product_name` | `string` | Optional | Gets or sets the product name. This is the AssemblyProduct name. |
| `operating_system` | `string` | Optional | Gets or sets the operating system. |
| `id` | `string` | Optional | Gets or sets the id. |
| `startup_wizard_completed` | `bool` | Optional | Gets or sets a value indicating whether the startup wizard is completed. |
| `operating_system_display_name` | `string` | Optional | Gets or sets the display name of the operating system. |
| `package_name` | `string` | Optional | Gets or sets the package name. |
| `has_pending_restart` | `bool` | Optional | Gets or sets a value indicating whether this instance has pending restart. |
| `is_shutting_down` | `bool` | Optional | - |
| `supports_library_monitor` | `bool` | Optional | Gets or sets a value indicating whether [supports library monitor]. |
| `web_socket_port_number` | `int` | Optional | Gets or sets the web socket port number. |
| `completed_installations` | [`List of InstallationInfo`](../../doc/models/installation-info.md) | Optional | Gets or sets the completed installations. |
| `can_self_restart` | `bool` | Optional | Gets or sets a value indicating whether this instance can self restart. |
| `can_launch_web_browser` | `bool` | Optional | - |
| `program_data_path` | `string` | Optional | Gets or sets the program data path. |
| `web_path` | `string` | Optional | Gets or sets the web UI resources path. |
| `items_by_name_path` | `string` | Optional | Gets or sets the items by name path. |
| `cache_path` | `string` | Optional | Gets or sets the cache path. |
| `log_path` | `string` | Optional | Gets or sets the log path. |
| `internal_metadata_path` | `string` | Optional | Gets or sets the internal metadata path. |
| `transcoding_temp_path` | `string` | Optional | Gets or sets the transcode path. |
| `has_update_available` | `bool` | Optional | Gets or sets a value indicating whether this instance has update available. |
| `encoder_location` | [`FFmpegLocationEnum`](../../doc/models/f-fmpeg-location-enum.md) | Optional | Enum describing the location of the FFmpeg tool. |
| `system_architecture` | [`ArchitectureEnum`](../../doc/models/architecture-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "LocalAddress": null,
  "ServerName": null,
  "Version": null,
  "ProductName": null,
  "OperatingSystem": null,
  "Id": null,
  "StartupWizardCompleted": null,
  "OperatingSystemDisplayName": null,
  "PackageName": null,
  "HasPendingRestart": null,
  "IsShuttingDown": null,
  "SupportsLibraryMonitor": null,
  "WebSocketPortNumber": null,
  "CompletedInstallations": null,
  "CanSelfRestart": null,
  "CanLaunchWebBrowser": null,
  "ProgramDataPath": null,
  "WebPath": null,
  "ItemsByNamePath": null,
  "CachePath": null,
  "LogPath": null,
  "InternalMetadataPath": null,
  "TranscodingTempPath": null,
  "HasUpdateAvailable": null,
  "EncoderLocation": null,
  "SystemArchitecture": null
}
```

