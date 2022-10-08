# Video Attachments

```python
video_attachments_controller = client.video_attachments
```

## Class Name

`VideoAttachmentsController`


# Get Attachment

Get video attachment.

```python
def get_attachment(self,
                  video_id,
                  media_source_id,
                  index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `video_id` | `uuid\|string` | Template, Required | Video ID. |
| `media_source_id` | `string` | Template, Required | Media Source ID. |
| `index` | `int` | Template, Required | Attachment Index. |

## Response Type

`binary`

## Example Usage

```python
video_id = '000000b8-0000-0000-0000-000000000000'
media_source_id = 'mediaSourceId4'
index = 44

result = video_attachments_controller.get_attachment(video_id, media_source_id, index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Video or attachment not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

