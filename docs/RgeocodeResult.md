# RgeocodeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RgeocodeResultEntity]**](RgeocodeResultEntity.md) |  | 
**location_boxes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from mapy_cz_geocode.models.rgeocode_result import RgeocodeResult

# TODO update the JSON string below
json = "{}"
# create an instance of RgeocodeResult from a JSON string
rgeocode_result_instance = RgeocodeResult.from_json(json)
# print the JSON string representation of the object
print RgeocodeResult.to_json()

# convert the object into a dict
rgeocode_result_dict = rgeocode_result_instance.to_dict()
# create an instance of RgeocodeResult from a dict
rgeocode_result_form_dict = rgeocode_result.from_dict(rgeocode_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


