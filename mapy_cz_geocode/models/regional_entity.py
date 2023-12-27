# coding: utf-8

"""
    REST API Mapy.cz geocoding methods

    Get coordinates and location for given geographic entity (e.g. address, city, WGS coordinates)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from mapy_cz_geocode.models.geocode_entity_type import GeocodeEntityType

class RegionalEntity(BaseModel):
    """
    RegionalEntity
    """
    name: StrictStr = Field(...)
    type: GeocodeEntityType = Field(...)
    iso_code: Optional[StrictStr] = Field(None, alias="isoCode", description="Iso code by ISO 3166-1 alpha-2, only for regional.country")
    __properties = ["name", "type", "isoCode"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RegionalEntity:
        """Create an instance of RegionalEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RegionalEntity:
        """Create an instance of RegionalEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegionalEntity.parse_obj(obj)

        _obj = RegionalEntity.parse_obj({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "iso_code": obj.get("isoCode")
        })
        return _obj

