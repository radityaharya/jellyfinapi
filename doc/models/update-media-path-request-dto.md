
# Update Media Path Request Dto

Update library options dto.

## Structure

`UpdateMediaPathRequestDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | Gets or sets the library name. |
| `path_info` | [`MediaPathInfo`](../../doc/models/media-path-info.md) | Required | Gets or sets library folder path information. |

## Example (as JSON)

```json
{
  "Name": "Name0",
  "PathInfo": {
    "Path": null,
    "NetworkPath": null
  }
}
```

