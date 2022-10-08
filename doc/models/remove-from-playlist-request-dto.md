
# Remove From Playlist Request Dto

Class RemoveFromPlaylistRequestDto.

## Structure

`RemoveFromPlaylistRequestDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_item_ids` | `List of uuid\|string` | Optional | Gets or sets the playlist identifiers ot the items. Ignored when clearing the playlist. |
| `clear_playlist` | `bool` | Optional | Gets or sets a value indicating whether the entire playlist should be cleared. |
| `clear_playing_item` | `bool` | Optional | Gets or sets a value indicating whether the playing item should be removed as well. Used only when clearing the playlist. |

## Example (as JSON)

```json
{
  "PlaylistItemIds": null,
  "ClearPlaylist": null,
  "ClearPlayingItem": null
}
```

