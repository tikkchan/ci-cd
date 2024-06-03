import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_registration import UserRegistration  # noqa: E501
from swagger_server import util


def users_post(body):  # noqa: E501
    """Register a new user

    Register a new user with the application. # noqa: E501

    :param body: User registration details
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = UserRegistration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
