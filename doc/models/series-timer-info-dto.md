
# Series Timer Info Dto

Class SeriesTimerInfoDto.

## Structure

`SeriesTimerInfoDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Gets or sets the Id of the recording. |
| `mtype` | `string` | Optional | - |
| `server_id` | `string` | Optional | Gets or sets the server identifier. |
| `external_id` | `string` | Optional | Gets or sets the external identifier. |
| `channel_id` | `uuid\|string` | Optional | Gets or sets the channel id of the recording. |
| `external_channel_id` | `string` | Optional | Gets or sets the external channel identifier. |
| `channel_name` | `string` | Optional | Gets or sets the channel name of the recording. |
| `channel_primary_image_tag` | `string` | Optional | - |
| `program_id` | `string` | Optional | Gets or sets the program identifier. |
| `external_program_id` | `string` | Optional | Gets or sets the external program identifier. |
| `name` | `string` | Optional | Gets or sets the name of the recording. |
| `overview` | `string` | Optional | Gets or sets the description of the recording. |
| `start_date` | `datetime` | Optional | Gets or sets the start date of the recording, in UTC. |
| `end_date` | `datetime` | Optional | Gets or sets the end date of the recording, in UTC. |
| `service_name` | `string` | Optional | Gets or sets the name of the service. |
| `priority` | `int` | Optional | Gets or sets the priority. |
| `pre_padding_seconds` | `int` | Optional | Gets or sets the pre padding seconds. |
| `post_padding_seconds` | `int` | Optional | Gets or sets the post padding seconds. |
| `is_pre_padding_required` | `bool` | Optional | Gets or sets a value indicating whether this instance is pre padding required. |
| `parent_backdrop_item_id` | `string` | Optional | Gets or sets the Id of the Parent that has a backdrop if the item does not have one. |
| `parent_backdrop_image_tags` | `List of string` | Optional | Gets or sets the parent backdrop image tags. |
| `is_post_padding_required` | `bool` | Optional | Gets or sets a value indicating whether this instance is post padding required. |
| `keep_until` | [`KeepUntilEnum`](../../doc/models/keep-until-enum.md) | Optional | - |
| `record_any_time` | `bool` | Optional | Gets or sets a value indicating whether [record any time]. |
| `skip_episodes_in_library` | `bool` | Optional | - |
| `record_any_channel` | `bool` | Optional | Gets or sets a value indicating whether [record any channel]. |
| `keep_up_to` | `int` | Optional | - |
| `record_new_only` | `bool` | Optional | Gets or sets a value indicating whether [record new only]. |
| `days` | [`List of DayOfWeekEnum`](../../doc/models/day-of-week-enum.md) | Optional | Gets or sets the days. |
| `day_pattern` | [`DayPatternEnum`](../../doc/models/day-pattern-enum.md) | Optional | Gets or sets the day pattern. |
| `image_tags` | `dict` | Optional | Gets or sets the image tags. |
| `parent_thumb_item_id` | `string` | Optional | Gets or sets the parent thumb item id. |
| `parent_thumb_image_tag` | `string` | Optional | Gets or sets the parent thumb image tag. |
| `parent_primary_image_item_id` | `string` | Optional | Gets or sets the parent primary image item identifier. |
| `parent_primary_image_tag` | `string` | Optional | Gets or sets the parent primary image tag. |

## Example (as JSON)

```json
{
  "Id": null,
  "Type": null,
  "ServerId": null,
  "ExternalId": null,
  "ChannelId": null,
  "ExternalChannelId": null,
  "ChannelName": null,
  "ChannelPrimaryImageTag": null,
  "ProgramId": null,
  "ExternalProgramId": null,
  "Name": null,
  "Overview": null,
  "StartDate": null,
  "EndDate": null,
  "ServiceName": null,
  "Priority": null,
  "PrePaddingSeconds": null,
  "PostPaddingSeconds": null,
  "IsPrePaddingRequired": null,
  "ParentBackdropItemId": null,
  "ParentBackdropImageTags": null,
  "IsPostPaddingRequired": null,
  "KeepUntil": null,
  "RecordAnyTime": null,
  "SkipEpisodesInLibrary": null,
  "RecordAnyChannel": null,
  "KeepUpTo": null,
  "RecordNewOnly": null,
  "Days": null,
  "DayPattern": null,
  "ImageTags": null,
  "ParentThumbItemId": null,
  "ParentThumbImageTag": null,
  "ParentPrimaryImageItemId": null,
  "ParentPrimaryImageTag": null
}
```

