# coding: utf-8

"""
    Онлайн-магазин комиксов API

    This is an API specification for a comic purchase application. Users can browse, search, and purchase comics through this API.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Comic(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'title': 'str',
        'author': 'str',
        'price': 'float',
        'genre': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'author': 'author',
        'price': 'price',
        'genre': 'genre'
    }

    def __init__(self, id=None, title=None, author=None, price=None, genre=None):  # noqa: E501
        """Comic - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._author = None
        self._price = None
        self._genre = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if price is not None:
            self.price = price
        if genre is not None:
            self.genre = genre

    @property
    def id(self):
        """Gets the id of this Comic.  # noqa: E501

        Unique identifier of the comic  # noqa: E501

        :return: The id of this Comic.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comic.

        Unique identifier of the comic  # noqa: E501

        :param id: The id of this Comic.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Comic.  # noqa: E501

        Title of the comic  # noqa: E501

        :return: The title of this Comic.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Comic.

        Title of the comic  # noqa: E501

        :param title: The title of this Comic.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def author(self):
        """Gets the author of this Comic.  # noqa: E501

        Author of the comic  # noqa: E501

        :return: The author of this Comic.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Comic.

        Author of the comic  # noqa: E501

        :param author: The author of this Comic.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def price(self):
        """Gets the price of this Comic.  # noqa: E501

        Price of the comic  # noqa: E501

        :return: The price of this Comic.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Comic.

        Price of the comic  # noqa: E501

        :param price: The price of this Comic.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def genre(self):
        """Gets the genre of this Comic.  # noqa: E501

        Genre of the comic  # noqa: E501

        :return: The genre of this Comic.  # noqa: E501
        :rtype: str
        """
        return self._genre

    @genre.setter
    def genre(self, genre):
        """Sets the genre of this Comic.

        Genre of the comic  # noqa: E501

        :param genre: The genre of this Comic.  # noqa: E501
        :type: str
        """

        self._genre = genre

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Comic, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Comic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
