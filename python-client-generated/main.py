from __future__ import print_function

import logging
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.host = 'http://localhost:8080/api/v1/'
api_instance = swagger_client.ComicApi(swagger_client.ApiClient(configuration))

# Настройка логгера
logging.basicConfig(filename='./var/log/123.log', level=logging.INFO)

try:
    # Get list of comics
    api_response = api_instance.comics_get()
    pprint(api_response)
    logging.info('list of comics received successfully')
except ApiException as e:
    print("Exception when calling ComicApi->comics_get: %s\n" % e)
    logging.error("Exception when calling ComicApi->comics_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ComicApi(swagger_client.ApiClient(configuration))
comic_id = 56 # int | ID of the comic to purchase

try:
    # Purchase a comic
    api_response = api_instance.comics_post(comic_id)
    pprint(api_response)
    logging.info('Purchase a comic page loaded successfully')
except ApiException as e:
    print("Exception when calling ComicApi->comics_post: %s\n" % e)
    logging.error("Exception when calling ComicApi->comics_post: %s\n" % e)
