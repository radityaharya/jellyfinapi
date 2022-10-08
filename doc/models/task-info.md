
# Task Info

Class TaskInfo.

## Structure

`TaskInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the name. |
| `state` | [`TaskStateEnum`](../../doc/models/task-state-enum.md) | Optional | Gets or sets the state of the task. |
| `current_progress_percentage` | `float` | Optional | Gets or sets the progress. |
| `id` | `string` | Optional | Gets or sets the id. |
| `last_execution_result` | [`TaskResult`](../../doc/models/task-result.md) | Optional | Gets or sets the last execution result. |
| `triggers` | [`List of TaskTriggerInfo`](../../doc/models/task-trigger-info.md) | Optional | Gets or sets the triggers. |
| `description` | `string` | Optional | Gets or sets the description. |
| `category` | `string` | Optional | Gets or sets the category. |
| `is_hidden` | `bool` | Optional | Gets or sets a value indicating whether this instance is hidden. |
| `key` | `string` | Optional | Gets or sets the key. |

## Example (as JSON)

```json
{
  "Name": null,
  "State": null,
  "CurrentProgressPercentage": null,
  "Id": null,
  "LastExecutionResult": null,
  "Triggers": null,
  "Description": null,
  "Category": null,
  "IsHidden": null,
  "Key": null
}
```

