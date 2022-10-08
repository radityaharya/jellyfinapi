# Display Preferences

```python
display_preferences_controller = client.display_preferences
```

## Class Name

`DisplayPreferencesController`

## Methods

* [Get Display Preferences](../../doc/controllers/display-preferences.md#get-display-preferences)
* [Update Display Preferences](../../doc/controllers/display-preferences.md#update-display-preferences)


# Get Display Preferences

Get Display Preferences.

```python
def get_display_preferences(self,
                           display_preferences_id,
                           user_id,
                           client)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_preferences_id` | `string` | Template, Required | Display preferences id. |
| `user_id` | `uuid\|string` | Query, Required | User id. |
| `client` | `string` | Query, Required | Client. |

## Response Type

[`DisplayPreferencesDto`](../../doc/models/display-preferences-dto.md)

## Example Usage

```python
display_preferences_id = 'displayPreferencesId6'
user_id = '000013ec-0000-0000-0000-000000000000'
client = 'client8'

result = display_preferences_controller.get_display_preferences(display_preferences_id, user_id, client)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Display Preferences

Update Display Preferences.

```python
def update_display_preferences(self,
                              display_preferences_id,
                              user_id,
                              client,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_preferences_id` | `string` | Template, Required | Display preferences id. |
| `user_id` | `uuid\|string` | Query, Required | User Id. |
| `client` | `string` | Query, Required | Client. |
| `body` | [`DisplayPreferencesDto`](../../doc/models/display-preferences-dto.md) | Body, Required | New Display Preferences object. |

## Response Type

`void`

## Example Usage

```python
display_preferences_id = 'displayPreferencesId6'
user_id = '000013ec-0000-0000-0000-000000000000'
client = 'client8'
body = DisplayPreferencesDto()

result = display_preferences_controller.update_display_preferences(display_preferences_id, user_id, client, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

