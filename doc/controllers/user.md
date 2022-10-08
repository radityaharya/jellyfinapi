# User

```python
user_controller = client.user
```

## Class Name

`UserController`

## Methods

* [Authenticate User](../../doc/controllers/user.md#authenticate-user)
* [Authenticate User by Name](../../doc/controllers/user.md#authenticate-user-by-name)
* [Authenticate With Quick Connect](../../doc/controllers/user.md#authenticate-with-quick-connect)
* [Create User by Name](../../doc/controllers/user.md#create-user-by-name)
* [Delete User](../../doc/controllers/user.md#delete-user)
* [Forgot Password](../../doc/controllers/user.md#forgot-password)
* [Forgot Password Pin](../../doc/controllers/user.md#forgot-password-pin)
* [Get Current User](../../doc/controllers/user.md#get-current-user)
* [Get Public Users](../../doc/controllers/user.md#get-public-users)
* [Get User by Id](../../doc/controllers/user.md#get-user-by-id)
* [Get Users](../../doc/controllers/user.md#get-users)
* [Update User](../../doc/controllers/user.md#update-user)
* [Update User Configuration](../../doc/controllers/user.md#update-user-configuration)
* [Update User Easy Password](../../doc/controllers/user.md#update-user-easy-password)
* [Update User Password](../../doc/controllers/user.md#update-user-password)
* [Update User Policy](../../doc/controllers/user.md#update-user-policy)


# Authenticate User

Authenticates a user.

```python
def authenticate_user(self,
                     user_id,
                     pw,
                     password=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | The user id. |
| `pw` | `string` | Query, Required | The password as plain text. |
| `password` | `string` | Query, Optional | The password sha1-hash. |

## Response Type

[`AuthenticationResult`](../../doc/models/authentication-result.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
pw = 'pw0'

result = user_controller.authenticate_user(user_id, pw)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Sha1-hashed password only is not allowed. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 404 | User not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Authenticate User by Name

Authenticates a user by name.

```python
def authenticate_user_by_name(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AuthenticateUserByName`](../../doc/models/authenticate-user-by-name.md) | Body, Required | The M:Jellyfin.Api.Controllers.UserController.AuthenticateUserByName(Jellyfin.Api.Models.UserDtos.AuthenticateUserByName) request. |

## Response Type

[`AuthenticationResult`](../../doc/models/authentication-result.md)

## Example Usage

```python
body = AuthenticateUserByName()

result = user_controller.authenticate_user_by_name(body)
```


# Authenticate With Quick Connect

Authenticates a user with quick connect.

```python
def authenticate_with_quick_connect(self,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`QuickConnectDto`](../../doc/models/quick-connect-dto.md) | Body, Required | The Jellyfin.Api.Models.UserDtos.QuickConnectDto request. |

## Response Type

[`AuthenticationResult`](../../doc/models/authentication-result.md)

## Example Usage

```python
body = QuickConnectDto()
body.secret = 'Secret6'

result = user_controller.authenticate_with_quick_connect(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Missing token. | `APIException` |


# Create User by Name

Creates a user.

```python
def create_user_by_name(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateUserByName`](../../doc/models/create-user-by-name.md) | Body, Required | The create user by name request body. |

## Response Type

[`UserDto`](../../doc/models/user-dto.md)

## Example Usage

```python
body = CreateUserByName()

result = user_controller.create_user_by_name(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Delete User

Deletes a user.

```python
def delete_user(self,
               user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | The user id. |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'

result = user_controller.delete_user(user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | User not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Forgot Password

Initiates the forgot password process for a local user.

```python
def forgot_password(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ForgotPasswordDto`](../../doc/models/forgot-password-dto.md) | Body, Required | The forgot password request containing the entered username. |

## Response Type

[`ForgotPasswordResult`](../../doc/models/forgot-password-result.md)

## Example Usage

```python
body = ForgotPasswordDto()
body.entered_username = 'EnteredUsername0'

result = user_controller.forgot_password(body)
```


# Forgot Password Pin

Redeems a forgot password pin.

```python
def forgot_password_pin(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ForgotPasswordPinDto`](../../doc/models/forgot-password-pin-dto.md) | Body, Required | The forgot password pin request containing the entered pin. |

## Response Type

[`PinRedeemResult`](../../doc/models/pin-redeem-result.md)

## Example Usage

```python
body = ForgotPasswordPinDto()
body.pin = 'Pin0'

result = user_controller.forgot_password_pin(body)
```


# Get Current User

Gets the user based on auth token.

```python
def get_current_user(self)
```

## Response Type

[`UserDto`](../../doc/models/user-dto.md)

## Example Usage

```python
result = user_controller.get_current_user()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Token is not owned by a user. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Public Users

Gets a list of publicly visible users for display on a login screen.

```python
def get_public_users(self)
```

## Response Type

[`List of UserDto`](../../doc/models/user-dto.md)

## Example Usage

```python
result = user_controller.get_public_users()
```


# Get User by Id

Gets a user by Id.

```python
def get_user_by_id(self,
                  user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | The user id. |

## Response Type

[`UserDto`](../../doc/models/user-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'

result = user_controller.get_user_by_id(user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | User not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Users

Gets a list of users.

```python
def get_users(self,
             is_hidden=None,
             is_disabled=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_hidden` | `bool` | Query, Optional | Optional filter by IsHidden=true or false. |
| `is_disabled` | `bool` | Query, Optional | Optional filter by IsDisabled=true or false. |

## Response Type

[`List of UserDto`](../../doc/models/user-dto.md)

## Example Usage

```python
result = user_controller.get_users()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update User

Updates a user.

```python
def update_user(self,
               user_id,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | The user id. |
| `body` | [`UserDto`](../../doc/models/user-dto.md) | Body, Required | The updated user model. |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
body = UserDto()

result = user_controller.update_user(user_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | User information was not supplied. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | Unauthorized | `APIException` |
| 403 | User update forbidden. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Update User Configuration

Updates a user configuration.

```python
def update_user_configuration(self,
                             user_id,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | The user id. |
| `body` | [`UserConfiguration`](../../doc/models/user-configuration.md) | Body, Required | The new user configuration. |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
body = UserConfiguration()

result = user_controller.update_user_configuration(user_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | User configuration update forbidden. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Update User Easy Password

Updates a user's easy password.

```python
def update_user_easy_password(self,
                             user_id,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | The user id. |
| `body` | [`UpdateUserEasyPassword`](../../doc/models/update-user-easy-password.md) | Body, Required | The M:Jellyfin.Api.Controllers.UserController.UpdateUserEasyPassword(System.Guid,Jellyfin.Api.Models.UserDtos.UpdateUserEasyPassword) request. |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
body = UpdateUserEasyPassword()

result = user_controller.update_user_easy_password(user_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | User is not allowed to update the password. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 404 | User not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Update User Password

Updates a user's password.

```python
def update_user_password(self,
                        user_id,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | The user id. |
| `body` | [`UpdateUserPassword`](../../doc/models/update-user-password.md) | Body, Required | The M:Jellyfin.Api.Controllers.UserController.UpdateUserPassword(System.Guid,Jellyfin.Api.Models.UserDtos.UpdateUserPassword) request. |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
body = UpdateUserPassword()

result = user_controller.update_user_password(user_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | User is not allowed to update the password. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 404 | User not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Update User Policy

Updates a user policy.

```python
def update_user_policy(self,
                      user_id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | The user id. |
| `body` | [`UserPolicy`](../../doc/models/user-policy.md) | Body, Required | The new user policy. |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
body = UserPolicy()

result = user_controller.update_user_policy(user_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | User policy was not supplied. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | Unauthorized | `APIException` |
| 403 | User policy update forbidden. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

