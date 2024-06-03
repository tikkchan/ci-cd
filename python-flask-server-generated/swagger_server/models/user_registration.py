# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.user_registration_address import UserRegistrationAddress  # noqa: F401,E501
from swagger_server import util


class UserRegistration(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, username: str=None, email: str=None, password: str=None, address: UserRegistrationAddress=None):  # noqa: E501
        """UserRegistration - a model defined in Swagger

        :param username: The username of this UserRegistration.  # noqa: E501
        :type username: str
        :param email: The email of this UserRegistration.  # noqa: E501
        :type email: str
        :param password: The password of this UserRegistration.  # noqa: E501
        :type password: str
        :param address: The address of this UserRegistration.  # noqa: E501
        :type address: UserRegistrationAddress
        """
        self.swagger_types = {
            'username': str,
            'email': str,
            'password': str,
            'address': UserRegistrationAddress
        }

        self.attribute_map = {
            'username': 'username',
            'email': 'email',
            'password': 'password',
            'address': 'address'
        }
        self._username = username
        self._email = email
        self._password = password
        self._address = address

    @classmethod
    def from_dict(cls, dikt) -> 'UserRegistration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserRegistration of this UserRegistration.  # noqa: E501
        :rtype: UserRegistration
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this UserRegistration.

        Username of the user  # noqa: E501

        :return: The username of this UserRegistration.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this UserRegistration.

        Username of the user  # noqa: E501

        :param username: The username of this UserRegistration.
        :type username: str
        """

        self._username = username

    @property
    def email(self) -> str:
        """Gets the email of this UserRegistration.

        Email address of the user  # noqa: E501

        :return: The email of this UserRegistration.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserRegistration.

        Email address of the user  # noqa: E501

        :param email: The email of this UserRegistration.
        :type email: str
        """

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this UserRegistration.

        Password of the user  # noqa: E501

        :return: The password of this UserRegistration.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this UserRegistration.

        Password of the user  # noqa: E501

        :param password: The password of this UserRegistration.
        :type password: str
        """

        self._password = password

    @property
    def address(self) -> UserRegistrationAddress:
        """Gets the address of this UserRegistration.


        :return: The address of this UserRegistration.
        :rtype: UserRegistrationAddress
        """
        return self._address

    @address.setter
    def address(self, address: UserRegistrationAddress):
        """Sets the address of this UserRegistration.


        :param address: The address of this UserRegistration.
        :type address: UserRegistrationAddress
        """

        self._address = address
