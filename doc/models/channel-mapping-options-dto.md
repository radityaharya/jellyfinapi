
# Channel Mapping Options Dto

Channel mapping options dto.

## Structure

`ChannelMappingOptionsDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tuner_channels` | [`List of TunerChannelMapping`](../../doc/models/tuner-channel-mapping.md) | Optional | Gets or sets list of tuner channels. |
| `provider_channels` | [`List of NameIdPair`](../../doc/models/name-id-pair.md) | Optional | Gets or sets list of provider channels. |
| `mappings` | [`List of NameValuePair`](../../doc/models/name-value-pair.md) | Optional | Gets or sets list of mappings. |
| `provider_name` | `string` | Optional | Gets or sets provider name. |

## Example (as JSON)

```json
{
  "TunerChannels": null,
  "ProviderChannels": null,
  "Mappings": null,
  "ProviderName": null
}
```

