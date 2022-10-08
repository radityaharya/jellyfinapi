
# Recommendation Dto

## Structure

`RecommendationDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List of BaseItemDto`](../../doc/models/base-item-dto.md) | Optional | - |
| `recommendation_type` | [`RecommendationTypeEnum`](../../doc/models/recommendation-type-enum.md) | Optional | - |
| `baseline_item_name` | `string` | Optional | - |
| `category_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "Items": null,
  "RecommendationType": null,
  "BaselineItemName": null,
  "CategoryId": null
}
```

