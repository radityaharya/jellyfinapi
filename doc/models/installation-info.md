
# Installation Info

Class InstallationInfo.

## Structure

`InstallationInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `guid` | `uuid\|string` | Optional | Gets or sets the Id. |
| `name` | `string` | Optional | Gets or sets the name. |
| `version` | `string` | Optional | Gets or sets the version. |
| `changelog` | `string` | Optional | Gets or sets the changelog for this version. |
| `source_url` | `string` | Optional | Gets or sets the source URL. |
| `checksum` | `string` | Optional | Gets or sets a checksum for the binary. |
| `package_info` | [`PackageInfo`](../../doc/models/package-info.md) | Optional | Gets or sets package information for the installation. |

## Example (as JSON)

```json
{
  "Guid": null,
  "Name": null,
  "Version": null,
  "Changelog": null,
  "SourceUrl": null,
  "Checksum": null,
  "PackageInfo": null
}
```

