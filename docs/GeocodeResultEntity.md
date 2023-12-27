# GeocodeResultEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | 
**position** | [**Coordinates**](Coordinates.md) |  | 
**type** | [**GeocodeEntityType**](GeocodeEntityType.md) |  | 
**location** | **str** | Short label for locality of resolved entity | [optional] 
**regional_structure** | [**List[RegionalEntity]**](RegionalEntity.md) | Ordered list of parent administrative entities (smallest first). | 
**zip** | **str** | Postal code, available only in some areas and only for entity type &#x60;reg_address&#x60;) | [optional] 

## Example

```python
from mapy_cz_geocode.models.geocode_result_entity import GeocodeResultEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodeResultEntity from a JSON string
geocode_result_entity_instance = GeocodeResultEntity.from_json(json)
# print the JSON string representation of the object
print GeocodeResultEntity.to_json()

# convert the object into a dict
geocode_result_entity_dict = geocode_result_entity_instance.to_dict()
# create an instance of GeocodeResultEntity from a dict
geocode_result_entity_form_dict = geocode_result_entity.from_dict(geocode_result_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


