
# Timer Info Dto

## Structure

`TimerInfoDto`

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
| `status` | [`RecordingStatusEnum`](../../doc/models/recording-status-enum.md) | Optional | Gets or sets the status. |
| `series_timer_id` | `string` | Optional | Gets or sets the series timer identifier. |
| `external_series_timer_id` | `string` | Optional | Gets or sets the external series timer identifier. |
| `run_time_ticks` | `long\|int` | Optional | Gets or sets the run time ticks. |
| `program_info` | [`BaseItemDto`](../../doc/models/base-item-dto.md) | Optional | Gets or sets the program information. |

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
  "Status": null,
  "SeriesTimerId": null,
  "ExternalSeriesTimerId": null,
  "RunTimeTicks": null,
  "ProgramInfo": null
}
```

