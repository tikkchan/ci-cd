# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.comic import Comic  # noqa: E501
from swagger_server.models.purchase_response import PurchaseResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestComicController(BaseTestCase):
    """ComicController integration test stubs"""

    def test_comics_get(self):
        """Test case for comics_get

        Get list of comics
        """
        response = self.client.open(
            '/api/v1/comics',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_comics_post(self):
        """Test case for comics_post

        Purchase a comic
        """
        query_string = [('comic_id', 56)]
        response = self.client.open(
            '/api/v1/comics',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
