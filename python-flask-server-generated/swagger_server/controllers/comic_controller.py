import connexion
import six

from swagger_server.models.comic import Comic  # noqa: E501
from swagger_server.models.purchase_response import PurchaseResponse  # noqa: E501
from swagger_server import util


def comics_get():  # noqa: E501
    """Get list of comics

    Returns a list of available comics. # noqa: E501


    :rtype: List[Comic]
    """
    return 'do some magic!'


def comics_post(comic_id):  # noqa: E501
    """Purchase a comic

    Purchase a comic by providing comic ID. # noqa: E501

    :param comic_id: ID of the comic to purchase
    :type comic_id: int

    :rtype: PurchaseResponse
    """
    return 'do some magic!'
