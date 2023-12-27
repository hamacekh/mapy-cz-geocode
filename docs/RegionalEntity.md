# RegionalEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**GeocodeEntityType**](GeocodeEntityType.md) |  | 
**iso_code** | **str** | Iso code by ISO 3166-1 alpha-2, only for regional.country | [optional] 

## Example

```python
from mapy_cz_geocode.models.regional_entity import RegionalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalEntity from a JSON string
regional_entity_instance = RegionalEntity.from_json(json)
# print the JSON string representation of the object
print RegionalEntity.to_json()

# convert the object into a dict
regional_entity_dict = regional_entity_instance.to_dict()
# create an instance of RegionalEntity from a dict
regional_entity_form_dict = regional_entity.from_dict(regional_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


