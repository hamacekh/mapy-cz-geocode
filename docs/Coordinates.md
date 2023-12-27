# Coordinates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lon** | **float** | Location longitude in degrees (decimal point is \&quot;.\&quot;). Positive means east, negative west. | 
**lat** | **float** | Location latitude in degrees (decimal point is \&quot;.\&quot;). Positive means north, negative south. | 

## Example

```python
from mapy_cz_geocode.models.coordinates import Coordinates

# TODO update the JSON string below
json = "{}"
# create an instance of Coordinates from a JSON string
coordinates_instance = Coordinates.from_json(json)
# print the JSON string representation of the object
print Coordinates.to_json()

# convert the object into a dict
coordinates_dict = coordinates_instance.to_dict()
# create an instance of Coordinates from a dict
coordinates_form_dict = coordinates.from_dict(coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


