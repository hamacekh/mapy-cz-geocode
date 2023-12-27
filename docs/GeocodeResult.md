# GeocodeResult

Ordered list of matching geographical entities

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GeocodeResultEntity]**](GeocodeResultEntity.md) |  | 
**locality** | **List[object]** | Bboxes for localities used in param &#x60;locality&#x60; | [optional] [default to []]

## Example

```python
from mapy_cz_geocode.models.geocode_result import GeocodeResult

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodeResult from a JSON string
geocode_result_instance = GeocodeResult.from_json(json)
# print the JSON string representation of the object
print GeocodeResult.to_json()

# convert the object into a dict
geocode_result_dict = geocode_result_instance.to_dict()
# create an instance of GeocodeResult from a dict
geocode_result_form_dict = geocode_result.from_dict(geocode_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


