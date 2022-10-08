
# Person Lookup Info Remote Search Query

## Structure

`PersonLookupInfoRemoteSearchQuery`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search_info` | [`PersonLookupInfo`](../../doc/models/person-lookup-info.md) | Optional | - |
| `item_id` | `uuid\|string` | Optional | - |
| `search_provider_name` | `string` | Optional | Gets or sets the provider name to search within if set. |
| `include_disabled_providers` | `bool` | Optional | Gets or sets a value indicating whether disabled providers should be included. |

## Example (as JSON)

```json
{
  "SearchInfo": null,
  "ItemId": null,
  "SearchProviderName": null,
  "IncludeDisabledProviders": null
}
```

