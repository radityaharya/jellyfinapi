
# Trakt Sync Response

## Structure

`TraktSyncResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `added` | [`Items`](../../doc/models/items.md) | Optional | - |
| `deleted` | [`Items`](../../doc/models/items.md) | Optional | - |
| `updated` | [`Items`](../../doc/models/items.md) | Optional | - |
| `not_found` | [`NotFoundObjects`](../../doc/models/not-found-objects.md) | Optional | - |

## Example (as JSON)

```json
{
  "added": null,
  "deleted": null,
  "updated": null,
  "not_found": null
}
```

