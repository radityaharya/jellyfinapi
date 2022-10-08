
# Version Info

Defines the MediaBrowser.Model.Updates.VersionInfo class.

## Structure

`VersionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `string` | Optional | Gets or sets the version. |
| `version_number` | `string` | Optional | Gets the version as a System.Version. |
| `changelog` | `string` | Optional | Gets or sets the changelog for this version. |
| `target_abi` | `string` | Optional | Gets or sets the ABI that this version was built against. |
| `source_url` | `string` | Optional | Gets or sets the source URL. |
| `checksum` | `string` | Optional | Gets or sets a checksum for the binary. |
| `timestamp` | `string` | Optional | Gets or sets a timestamp of when the binary was built. |
| `repository_name` | `string` | Optional | Gets or sets the repository name. |
| `repository_url` | `string` | Optional | Gets or sets the repository url. |

## Example (as JSON)

```json
{
  "version": null,
  "changelog": null,
  "targetAbi": null,
  "sourceUrl": null,
  "checksum": null,
  "timestamp": null,
  "repositoryName": null,
  "repositoryUrl": null
}
```

