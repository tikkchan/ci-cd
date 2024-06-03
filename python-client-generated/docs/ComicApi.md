# swagger_client.ComicApi

All URIs are relative to *https://comic-purchase-api.example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comics_get**](ComicApi.md#comics_get) | **GET** /comics | Get list of comics
[**comics_post**](ComicApi.md#comics_post) | **POST** /comics | Purchase a comic

# **comics_get**
> list[Comic] comics_get()

Get list of comics

Returns a list of available comics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComicApi()

try:
    # Get list of comics
    api_response = api_instance.comics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComicApi->comics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Comic]**](Comic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comics_post**
> PurchaseResponse comics_post(comic_id)

Purchase a comic

Purchase a comic by providing comic ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComicApi()
comic_id = 56 # int | ID of the comic to purchase

try:
    # Purchase a comic
    api_response = api_instance.comics_post(comic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComicApi->comics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_id** | **int**| ID of the comic to purchase | 

### Return type

[**PurchaseResponse**](PurchaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

