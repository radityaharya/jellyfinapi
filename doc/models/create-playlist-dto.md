
# Create Playlist Dto

Create new playlist dto.

## Structure

`CreatePlaylistDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the name of the new playlist. |
| `ids` | `List of uuid\|string` | Optional | Gets or sets item ids to add to the playlist. |
| `user_id` | `uuid\|string` | Optional | Gets or sets the user id. |
| `media_type` | `string` | Optional | Gets or sets the media type. |

## Example (as JSON)

```json
{
  "Name": null,
  "Ids": null,
  "UserId": null,
  "MediaType": null
}
```

