# swagger_client.UserApi

All URIs are relative to *https://comic-purchase-api.example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_post**](UserApi.md#users_post) | **POST** /users | Register a new user

# **users_post**
> User users_post(body)

Register a new user

Register a new user with the application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.UserRegistration() # UserRegistration | User registration details

try:
    # Register a new user
    api_response = api_instance.users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRegistration**](UserRegistration.md)| User registration details | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

