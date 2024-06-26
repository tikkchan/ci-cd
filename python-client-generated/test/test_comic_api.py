# coding: utf-8

"""
    Онлайн-магазин комиксов API

    This is an API specification for a comic purchase application. Users can browse, search, and purchase comics through this API.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.comic_api import ComicApi  # noqa: E501
from swagger_client.rest import ApiException


class TestComicApi(unittest.TestCase):
    """ComicApi unit test stubs"""

    def setUp(self):
        self.api = ComicApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_comics_get(self):
        """Test case for comics_get

        Get list of comics  # noqa: E501
        """
        pass

    def test_comics_post(self):
        """Test case for comics_post

        Purchase a comic  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
