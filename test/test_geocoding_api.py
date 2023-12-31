# coding: utf-8

"""
    REST API Mapy.cz geocoding methods

    Get coordinates and location for given geographic entity (e.g. address, city, WGS coordinates)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from mapy_cz_geocode.api.geocoding_api import GeocodingApi  # noqa: E501


class TestGeocodingApi(unittest.TestCase):
    """GeocodingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GeocodingApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_api_geocode_v1_geocode_get(self) -> None:
        """Test case for api_geocode_v1_geocode_get

        Find entities for given search query  # noqa: E501
        """
        pass

    def test_api_rgeocode_v1_rgeocode_get(self) -> None:
        """Test case for api_rgeocode_v1_rgeocode_get

        Get regional entities for coordinates  # noqa: E501
        """
        pass

    def test_api_suggest_v1_suggest_get(self) -> None:
        """Test case for api_suggest_v1_suggest_get

        Suggest entities while typing a query  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
