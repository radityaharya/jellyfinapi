# Time Sync

```python
time_sync_controller = client.time_sync
```

## Class Name

`TimeSyncController`


# Get Utc Time

Gets the current UTC time.

```python
def get_utc_time(self)
```

## Response Type

[`UtcTimeResponse`](../../doc/models/utc-time-response.md)

## Example Usage

```python
result = time_sync_controller.get_utc_time()
```

