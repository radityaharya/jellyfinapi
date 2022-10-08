# Scheduled Tasks

```python
scheduled_tasks_controller = client.scheduled_tasks
```

## Class Name

`ScheduledTasksController`

## Methods

* [Get Task](../../doc/controllers/scheduled-tasks.md#get-task)
* [Get Tasks](../../doc/controllers/scheduled-tasks.md#get-tasks)
* [Start Task](../../doc/controllers/scheduled-tasks.md#start-task)
* [Stop Task](../../doc/controllers/scheduled-tasks.md#stop-task)
* [Update Task](../../doc/controllers/scheduled-tasks.md#update-task)


# Get Task

Get task by id.

```python
def get_task(self,
            task_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `task_id` | `string` | Template, Required | Task Id. |

## Response Type

[`TaskInfo`](../../doc/models/task-info.md)

## Example Usage

```python
task_id = 'taskId4'

result = scheduled_tasks_controller.get_task(task_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Task not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Tasks

Get tasks.

```python
def get_tasks(self,
             is_hidden=None,
             is_enabled=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_hidden` | `bool` | Query, Optional | Optional filter tasks that are hidden, or not. |
| `is_enabled` | `bool` | Query, Optional | Optional filter tasks that are enabled, or not. |

## Response Type

[`List of TaskInfo`](../../doc/models/task-info.md)

## Example Usage

```python
result = scheduled_tasks_controller.get_tasks()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Start Task

Start specified task.

```python
def start_task(self,
              task_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `task_id` | `string` | Template, Required | Task Id. |

## Response Type

`void`

## Example Usage

```python
task_id = 'taskId4'

result = scheduled_tasks_controller.start_task(task_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Task not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Stop Task

Stop specified task.

```python
def stop_task(self,
             task_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `task_id` | `string` | Template, Required | Task Id. |

## Response Type

`void`

## Example Usage

```python
task_id = 'taskId4'

result = scheduled_tasks_controller.stop_task(task_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Task not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Update Task

Update specified task triggers.

```python
def update_task(self,
               task_id,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `task_id` | `string` | Template, Required | Task Id. |
| `body` | [`List of TaskTriggerInfo`](../../doc/models/task-trigger-info.md) | Body, Required | Triggers. |

## Response Type

`void`

## Example Usage

```python
task_id = 'taskId4'
body = []

body.append(TaskTriggerInfo())

body.append(TaskTriggerInfo())


result = scheduled_tasks_controller.update_task(task_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Task not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

