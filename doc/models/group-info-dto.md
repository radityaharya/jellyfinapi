
# Group Info Dto

Class GroupInfoDto.

## Structure

`GroupInfoDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group_id` | `uuid\|string` | Optional | Gets the group identifier. |
| `group_name` | `string` | Optional | Gets the group name. |
| `state` | [`GroupStateTypeEnum`](../../doc/models/group-state-type-enum.md) | Optional | Gets the group state. |
| `participants` | `List of string` | Optional | Gets the participants. |
| `last_updated_at` | `datetime` | Optional | Gets the date when this DTO has been created. |

## Example (as JSON)

```json
{
  "GroupId": null,
  "GroupName": null,
  "State": null,
  "Participants": null,
  "LastUpdatedAt": null
}
```

