# RgeocodeResultEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | 
**position** | [**Coordinates**](Coordinates.md) |  | 
**type** | [**RgeoEntityType**](RgeoEntityType.md) |  | 
**location** | **str** | Short label for locality of resolved entity | [optional] 
**regional_structure** | [**List[RegionalEntity]**](RegionalEntity.md) | Ordered list of parent administrative entities (smallest first). | 
**zip** | **str** | Postal code, available only in some areas and only for entity type &#x60;reg_address&#x60;) | [optional] 

## Example

```python
from mapy_cz_geocode.models.rgeocode_result_entity import RgeocodeResultEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RgeocodeResultEntity from a JSON string
rgeocode_result_entity_instance = RgeocodeResultEntity.from_json(json)
# print the JSON string representation of the object
print RgeocodeResultEntity.to_json()

# convert the object into a dict
rgeocode_result_entity_dict = rgeocode_result_entity_instance.to_dict()
# create an instance of RgeocodeResultEntity from a dict
rgeocode_result_entity_form_dict = rgeocode_result_entity.from_dict(rgeocode_result_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


