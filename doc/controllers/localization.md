# Localization

```python
localization_controller = client.localization
```

## Class Name

`LocalizationController`

## Methods

* [Get Countries](../../doc/controllers/localization.md#get-countries)
* [Get Cultures](../../doc/controllers/localization.md#get-cultures)
* [Get Localization Options](../../doc/controllers/localization.md#get-localization-options)
* [Get Parental Ratings](../../doc/controllers/localization.md#get-parental-ratings)


# Get Countries

Gets known countries.

```python
def get_countries(self)
```

## Response Type

[`List of CountryInfo`](../../doc/models/country-info.md)

## Example Usage

```python
result = localization_controller.get_countries()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Cultures

Gets known cultures.

```python
def get_cultures(self)
```

## Response Type

[`List of CultureDto`](../../doc/models/culture-dto.md)

## Example Usage

```python
result = localization_controller.get_cultures()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Localization Options

Gets localization options.

```python
def get_localization_options(self)
```

## Response Type

[`List of LocalizationOption`](../../doc/models/localization-option.md)

## Example Usage

```python
result = localization_controller.get_localization_options()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Parental Ratings

Gets known parental ratings.

```python
def get_parental_ratings(self)
```

## Response Type

[`List of ParentalRating`](../../doc/models/parental-rating.md)

## Example Usage

```python
result = localization_controller.get_parental_ratings()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

