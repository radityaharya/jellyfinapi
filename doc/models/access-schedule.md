
# Access Schedule

An entity representing a user's access schedule.

## Structure

`AccessSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Gets the id of this instance. |
| `user_id` | `uuid\|string` | Optional | Gets the id of the associated user. |
| `day_of_week` | [`DynamicDayOfWeekEnum`](../../doc/models/dynamic-day-of-week-enum.md) | Optional | Gets or sets the day of week. |
| `start_hour` | `float` | Optional | Gets or sets the start hour. |
| `end_hour` | `float` | Optional | Gets or sets the end hour. |

## Example (as JSON)

```json
{
  "UserId": null,
  "DayOfWeek": null,
  "StartHour": null,
  "EndHour": null
}
```

