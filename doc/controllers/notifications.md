# Notifications

```python
notifications_controller = client.notifications
```

## Class Name

`NotificationsController`

## Methods

* [Create Admin Notification](../../doc/controllers/notifications.md#create-admin-notification)
* [Get Notification Services](../../doc/controllers/notifications.md#get-notification-services)
* [Get Notification Types](../../doc/controllers/notifications.md#get-notification-types)
* [Get Notifications](../../doc/controllers/notifications.md#get-notifications)
* [Get Notifications Summary](../../doc/controllers/notifications.md#get-notifications-summary)
* [Set Read](../../doc/controllers/notifications.md#set-read)
* [Set Unread](../../doc/controllers/notifications.md#set-unread)


# Create Admin Notification

Sends a notification to all admins.

```python
def create_admin_notification(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AdminNotificationDto`](../../doc/models/admin-notification-dto.md) | Body, Required | The notification request. |

## Response Type

`void`

## Example Usage

```python
body = AdminNotificationDto()

result = notifications_controller.create_admin_notification(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Notification Services

Gets notification services.

```python
def get_notification_services(self)
```

## Response Type

[`List of NameIdPair`](../../doc/models/name-id-pair.md)

## Example Usage

```python
result = notifications_controller.get_notification_services()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Notification Types

Gets notification types.

```python
def get_notification_types(self)
```

## Response Type

[`List of NotificationTypeInfo`](../../doc/models/notification-type-info.md)

## Example Usage

```python
result = notifications_controller.get_notification_types()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Notifications

Gets a user's notifications.

```python
def get_notifications(self,
                     user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `string` | Template, Required | - |

## Response Type

[`NotificationResultDto`](../../doc/models/notification-result-dto.md)

## Example Usage

```python
user_id = 'userId0'

result = notifications_controller.get_notifications(user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Notifications Summary

Gets a user's notification summary.

```python
def get_notifications_summary(self,
                             user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `string` | Template, Required | - |

## Response Type

[`NotificationsSummaryDto`](../../doc/models/notifications-summary-dto.md)

## Example Usage

```python
user_id = 'userId0'

result = notifications_controller.get_notifications_summary(user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Set Read

Sets notifications as read.

```python
def set_read(self,
            user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
user_id = 'userId0'

result = notifications_controller.set_read(user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Set Unread

Sets notifications as unread.

```python
def set_unread(self,
              user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
user_id = 'userId0'

result = notifications_controller.set_unread(user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

