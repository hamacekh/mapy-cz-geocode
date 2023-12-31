# coding: utf-8

"""
    REST API Mapy.cz geocoding methods

    Get coordinates and location for given geographic entity (e.g. address, city, WGS coordinates)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class GeocodeEntityType(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    REGIONAL = 'regional'
    REGIONAL_DOT_COUNTRY = 'regional.country'
    REGIONAL_DOT_REGION = 'regional.region'
    REGIONAL_DOT_MUNICIPALITY = 'regional.municipality'
    REGIONAL_DOT_MUNICIPALITY_PART = 'regional.municipality_part'
    REGIONAL_DOT_STREET = 'regional.street'
    REGIONAL_DOT_ADDRESS = 'regional.address'
    POI = 'poi'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GeocodeEntityType from a JSON string"""
        return cls(json.loads(json_str))


