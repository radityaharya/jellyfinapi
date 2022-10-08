
# Update User Password

The update user password request body.

## Structure

`UpdateUserPassword`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `current_password` | `string` | Optional | Gets or sets the current sha1-hashed password. |
| `current_pw` | `string` | Optional | Gets or sets the current plain text password. |
| `new_pw` | `string` | Optional | Gets or sets the new plain text password. |
| `reset_password` | `bool` | Optional | Gets or sets a value indicating whether to reset the password. |

## Example (as JSON)

```json
{
  "CurrentPassword": null,
  "CurrentPw": null,
  "NewPw": null,
  "ResetPassword": null
}
```

