# Dashboard

```python
dashboard_controller = client.dashboard
```

## Class Name

`DashboardController`

## Methods

* [Get Configuration Pages](../../doc/controllers/dashboard.md#get-configuration-pages)
* [Get Dashboard Configuration Page](../../doc/controllers/dashboard.md#get-dashboard-configuration-page)


# Get Configuration Pages

Gets the configuration pages.

```python
def get_configuration_pages(self,
                           enable_in_main_menu=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_in_main_menu` | `bool` | Query, Optional | Whether to enable in the main menu. |

## Response Type

[`List of ConfigurationPageInfo`](../../doc/models/configuration-page-info.md)

## Example Usage

```python
result = dashboard_controller.get_configuration_pages()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Server still loading. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Dashboard Configuration Page

Gets a dashboard configuration page.

```python
def get_dashboard_configuration_page(self,
                                    name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Query, Optional | The name of the page. |

## Response Type

`binary`

## Example Usage

```python
result = dashboard_controller.get_dashboard_configuration_page()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Plugin configuration page not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

