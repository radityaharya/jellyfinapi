# Dlna

```python
dlna_controller = client.dlna
```

## Class Name

`DlnaController`

## Methods

* [Create Profile](../../doc/controllers/dlna.md#create-profile)
* [Delete Profile](../../doc/controllers/dlna.md#delete-profile)
* [Get Default Profile](../../doc/controllers/dlna.md#get-default-profile)
* [Get Profile](../../doc/controllers/dlna.md#get-profile)
* [Get Profile Infos](../../doc/controllers/dlna.md#get-profile-infos)
* [Update Profile](../../doc/controllers/dlna.md#update-profile)


# Create Profile

Creates a profile.

```python
def create_profile(self,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceProfile`](../../doc/models/device-profile.md) | Body, Optional | Device profile. |

## Response Type

`void`

## Example Usage

```python
result = dlna_controller.create_profile()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Delete Profile

Deletes a profile.

```python
def delete_profile(self,
                  profile_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profile_id` | `string` | Template, Required | Profile id. |

## Response Type

`void`

## Example Usage

```python
profile_id = 'profileId0'

result = dlna_controller.delete_profile(profile_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Device profile not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Default Profile

Gets the default profile.

```python
def get_default_profile(self)
```

## Response Type

[`DeviceProfile`](../../doc/models/device-profile.md)

## Example Usage

```python
result = dlna_controller.get_default_profile()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Profile

Gets a single profile.

```python
def get_profile(self,
               profile_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profile_id` | `string` | Template, Required | Profile Id. |

## Response Type

[`DeviceProfile`](../../doc/models/device-profile.md)

## Example Usage

```python
profile_id = 'profileId0'

result = dlna_controller.get_profile(profile_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Device profile not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Profile Infos

Get profile infos.

```python
def get_profile_infos(self)
```

## Response Type

[`List of DeviceProfileInfo`](../../doc/models/device-profile-info.md)

## Example Usage

```python
result = dlna_controller.get_profile_infos()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Profile

Updates a profile.

```python
def update_profile(self,
                  profile_id,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profile_id` | `string` | Template, Required | Profile id. |
| `body` | [`DeviceProfile`](../../doc/models/device-profile.md) | Body, Optional | Device profile. |

## Response Type

`void`

## Example Usage

```python
profile_id = 'profileId0'

result = dlna_controller.update_profile(profile_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Device profile not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

