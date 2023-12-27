# mapy_cz_geocode.GeocodingApi

All URIs are relative to *https://api.mapy.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_geocode_v1_geocode_get**](GeocodingApi.md#api_geocode_v1_geocode_get) | **GET** /v1/geocode | Find entities for given search query
[**api_rgeocode_v1_rgeocode_get**](GeocodingApi.md#api_rgeocode_v1_rgeocode_get) | **GET** /v1/rgeocode | Get regional entities for coordinates
[**api_suggest_v1_suggest_get**](GeocodingApi.md#api_suggest_v1_suggest_get) | **GET** /v1/suggest | Suggest entities while typing a query


# **api_geocode_v1_geocode_get**
> GeocodeResult api_geocode_v1_geocode_get(query=query, lang=lang, limit=limit, type=type, locality=locality, prefer_b_box=prefer_b_box, prefer_near=prefer_near, prefer_near_precision=prefer_near_precision)

Find entities for given search query

Obtains coordinates and additional information (like surrounding regional structure) based on textual location query (addresses, streets, cities, ...). Rate limit is 100 requests per second per API key

### Example

* Api Key Authentication (headerApiKey):
* Api Key Authentication (queryApiKey):

```python
import time
import os
import mapy_cz_geocode
from mapy_cz_geocode.models.geocode_entity_type import GeocodeEntityType
from mapy_cz_geocode.models.geocode_result import GeocodeResult
from mapy_cz_geocode.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mapy.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = mapy_cz_geocode.Configuration(
    host = "https://api.mapy.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: headerApiKey
configuration.api_key['headerApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['headerApiKey'] = 'Bearer'

# Configure API key authorization: queryApiKey
configuration.api_key['queryApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['queryApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with mapy_cz_geocode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mapy_cz_geocode.GeocodingApi(api_client)
    query = '' # str | Geographic entity name to resolve (optional) (default to '')
    lang = mapy_cz_geocode.Language() # Language | Preferred language for result entity names (optional)
    limit = 5 # int | Maximum number of results (default 5, upper limit 15) (optional) (default to 5)
    type = ["regional","poi"] # List[GeocodeEntityType] | Return selected entity types only (optional) (default to ["regional","poi"])
    locality = ['locality_example'] # List[str] | Return results only from these localities. It may be in form of comma-separated locality names (e. g. `Praha 5`, `Lhota u Kolína`), country codes (cz, gb, us, ...) or rectangles `BOX({minLon},{minLat},{maxLon},{maxLat})` or a mix of them. Location names (except country codes) are internally converted to bounding boxes, so using box arguments is preferred to avoid ambiguities - resolved boxes for locality names are returned in response (or \"Not found!\" for unknown localities) to help with this. On the other hand, country codes are preferred over their bounding boxes, because they allow precise filtering and avoid enge-cases near the date-line.  (optional)
    prefer_b_box = [3.4] # List[float] | Prefer results from this box (not a filter). Conflicts with `near`. If neither `box` nor `near` is specified, defaults to Czech Republic. Format `{minLon},{minLat},{maxLon},{maxLat}` (optional)
    prefer_near = [3.4] # List[float] | Prefer results near this position (not a filter). Conflicts with `box`. If neither `box` nor `near` is specified, defaults to Czech Republic. Format `{lon}, {lat}` (optional)
    prefer_near_precision = 3.4 # float | Precision of parameter `near` in meters (use to prefer results from a circle) (optional)

    try:
        # Find entities for given search query
        api_response = api_instance.api_geocode_v1_geocode_get(query=query, lang=lang, limit=limit, type=type, locality=locality, prefer_b_box=prefer_b_box, prefer_near=prefer_near, prefer_near_precision=prefer_near_precision)
        print("The response of GeocodingApi->api_geocode_v1_geocode_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->api_geocode_v1_geocode_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Geographic entity name to resolve | [optional] [default to &#39;&#39;]
 **lang** | [**Language**](.md)| Preferred language for result entity names | [optional] 
 **limit** | **int**| Maximum number of results (default 5, upper limit 15) | [optional] [default to 5]
 **type** | [**List[GeocodeEntityType]**](GeocodeEntityType.md)| Return selected entity types only | [optional] [default to [&quot;regional&quot;,&quot;poi&quot;]]
 **locality** | [**List[str]**](str.md)| Return results only from these localities. It may be in form of comma-separated locality names (e. g. &#x60;Praha 5&#x60;, &#x60;Lhota u Kolína&#x60;), country codes (cz, gb, us, ...) or rectangles &#x60;BOX({minLon},{minLat},{maxLon},{maxLat})&#x60; or a mix of them. Location names (except country codes) are internally converted to bounding boxes, so using box arguments is preferred to avoid ambiguities - resolved boxes for locality names are returned in response (or \&quot;Not found!\&quot; for unknown localities) to help with this. On the other hand, country codes are preferred over their bounding boxes, because they allow precise filtering and avoid enge-cases near the date-line.  | [optional] 
 **prefer_b_box** | [**List[float]**](float.md)| Prefer results from this box (not a filter). Conflicts with &#x60;near&#x60;. If neither &#x60;box&#x60; nor &#x60;near&#x60; is specified, defaults to Czech Republic. Format &#x60;{minLon},{minLat},{maxLon},{maxLat}&#x60; | [optional] 
 **prefer_near** | [**List[float]**](float.md)| Prefer results near this position (not a filter). Conflicts with &#x60;box&#x60;. If neither &#x60;box&#x60; nor &#x60;near&#x60; is specified, defaults to Czech Republic. Format &#x60;{lon}, {lat}&#x60; | [optional] 
 **prefer_near_precision** | **float**| Precision of parameter &#x60;near&#x60; in meters (use to prefer results from a circle) | [optional] 

### Return type

[**GeocodeResult**](GeocodeResult.md)

### Authorization

[headerApiKey](../README.md#headerApiKey), [queryApiKey](../README.md#queryApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request succeeded |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_rgeocode_v1_rgeocode_get**
> RgeocodeResult api_rgeocode_v1_rgeocode_get(lon, lat, lang=lang)

Get regional entities for coordinates

Reverse geocode - get regional entities for given location coordinates. Rate limit is 200 requests per second per API key.

### Example

* Api Key Authentication (headerApiKey):
* Api Key Authentication (queryApiKey):

```python
import time
import os
import mapy_cz_geocode
from mapy_cz_geocode.models.rgeocode_result import RgeocodeResult
from mapy_cz_geocode.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mapy.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = mapy_cz_geocode.Configuration(
    host = "https://api.mapy.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: headerApiKey
configuration.api_key['headerApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['headerApiKey'] = 'Bearer'

# Configure API key authorization: queryApiKey
configuration.api_key['queryApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['queryApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with mapy_cz_geocode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mapy_cz_geocode.GeocodingApi(api_client)
    lon = 14.42212 # float | Location longitude in degrees (decimal point is \".\"). Positive means east, negative west.
    lat = 50.08861 # float | Location latitude in degrees (decimal point is \".\"). Positive means north, negative south.
    lang = mapy_cz_geocode.Language() # Language | Preferred language for result entity names (optional)

    try:
        # Get regional entities for coordinates
        api_response = api_instance.api_rgeocode_v1_rgeocode_get(lon, lat, lang=lang)
        print("The response of GeocodingApi->api_rgeocode_v1_rgeocode_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->api_rgeocode_v1_rgeocode_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lon** | **float**| Location longitude in degrees (decimal point is \&quot;.\&quot;). Positive means east, negative west. | 
 **lat** | **float**| Location latitude in degrees (decimal point is \&quot;.\&quot;). Positive means north, negative south. | 
 **lang** | [**Language**](.md)| Preferred language for result entity names | [optional] 

### Return type

[**RgeocodeResult**](RgeocodeResult.md)

### Authorization

[headerApiKey](../README.md#headerApiKey), [queryApiKey](../README.md#queryApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request succeeded |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_suggest_v1_suggest_get**
> GeocodeResult api_suggest_v1_suggest_get(query=query, lang=lang, limit=limit, type=type, locality=locality, prefer_b_box=prefer_b_box, prefer_near=prefer_near, prefer_near_precision=prefer_near_precision)

Suggest entities while typing a query

Suggest works similarly to geocoding, but it accounts for incomplete queries, so it can be used to suggest matching entities while user is writing the location query. Rate limit is 100 requests per second per API key

### Example

* Api Key Authentication (headerApiKey):
* Api Key Authentication (queryApiKey):

```python
import time
import os
import mapy_cz_geocode
from mapy_cz_geocode.models.geocode_entity_type import GeocodeEntityType
from mapy_cz_geocode.models.geocode_result import GeocodeResult
from mapy_cz_geocode.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mapy.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = mapy_cz_geocode.Configuration(
    host = "https://api.mapy.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: headerApiKey
configuration.api_key['headerApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['headerApiKey'] = 'Bearer'

# Configure API key authorization: queryApiKey
configuration.api_key['queryApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['queryApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with mapy_cz_geocode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mapy_cz_geocode.GeocodingApi(api_client)
    query = '' # str | Geographic entity name to resolve (optional) (default to '')
    lang = mapy_cz_geocode.Language() # Language | Preferred language for result entity names (optional)
    limit = 5 # int | Maximum number of results (default 5, upper limit 15) (optional) (default to 5)
    type = [regional, poi] # List[GeocodeEntityType] | Return selected entity types only (optional) (default to [regional, poi])
    locality = ['locality_example'] # List[str] | Return results only from these localities. It may be in form of comma-separated locality names (e. g. `Praha 5`, `Lhota u Kolína`), country codes (cz, gb, us, ...) or rectangles `BOX({minLon},{minLat},{maxLon},{maxLat})` or a mix of them. Location names (except country codes) are internally converted to bounding boxes, so using box arguments is preferred to avoid ambiguities - resolved boxes for locality names are returned in response (or \"Not found!\" for unknown localities) to help with this. On the other hand, country codes are preferred over their bounding boxes, because they allow precise filtering and avoid enge-cases near the date-line.  (optional)
    prefer_b_box = [3.4] # List[float] | Prefer results from this box (not a filter). Conflicts with `near`. If neither `box` nor `near` is specified, defaults to Czech Republic. Format `{minLon},{minLat},{maxLon},{maxLat}` (optional)
    prefer_near = [3.4] # List[float] | Prefer results near this position (not a filter). Conflicts with `box`. If neither `box` nor `near` is specified, defaults to Czech Republic. Format `{lon}, {lat}` (optional)
    prefer_near_precision = 3.4 # float | Precision of parameter `near` in meters (use to prefer results from a circle) (optional)

    try:
        # Suggest entities while typing a query
        api_response = api_instance.api_suggest_v1_suggest_get(query=query, lang=lang, limit=limit, type=type, locality=locality, prefer_b_box=prefer_b_box, prefer_near=prefer_near, prefer_near_precision=prefer_near_precision)
        print("The response of GeocodingApi->api_suggest_v1_suggest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->api_suggest_v1_suggest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Geographic entity name to resolve | [optional] [default to &#39;&#39;]
 **lang** | [**Language**](.md)| Preferred language for result entity names | [optional] 
 **limit** | **int**| Maximum number of results (default 5, upper limit 15) | [optional] [default to 5]
 **type** | [**List[GeocodeEntityType]**](GeocodeEntityType.md)| Return selected entity types only | [optional] [default to [regional, poi]]
 **locality** | [**List[str]**](str.md)| Return results only from these localities. It may be in form of comma-separated locality names (e. g. &#x60;Praha 5&#x60;, &#x60;Lhota u Kolína&#x60;), country codes (cz, gb, us, ...) or rectangles &#x60;BOX({minLon},{minLat},{maxLon},{maxLat})&#x60; or a mix of them. Location names (except country codes) are internally converted to bounding boxes, so using box arguments is preferred to avoid ambiguities - resolved boxes for locality names are returned in response (or \&quot;Not found!\&quot; for unknown localities) to help with this. On the other hand, country codes are preferred over their bounding boxes, because they allow precise filtering and avoid enge-cases near the date-line.  | [optional] 
 **prefer_b_box** | [**List[float]**](float.md)| Prefer results from this box (not a filter). Conflicts with &#x60;near&#x60;. If neither &#x60;box&#x60; nor &#x60;near&#x60; is specified, defaults to Czech Republic. Format &#x60;{minLon},{minLat},{maxLon},{maxLat}&#x60; | [optional] 
 **prefer_near** | [**List[float]**](float.md)| Prefer results near this position (not a filter). Conflicts with &#x60;box&#x60;. If neither &#x60;box&#x60; nor &#x60;near&#x60; is specified, defaults to Czech Republic. Format &#x60;{lon}, {lat}&#x60; | [optional] 
 **prefer_near_precision** | **float**| Precision of parameter &#x60;near&#x60; in meters (use to prefer results from a circle) | [optional] 

### Return type

[**GeocodeResult**](GeocodeResult.md)

### Authorization

[headerApiKey](../README.md#headerApiKey), [queryApiKey](../README.md#queryApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request succeeded |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

