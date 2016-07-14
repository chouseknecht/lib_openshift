# lib_openshift.OsapiApi

All URIs are relative to *https://10.0.0.51:8443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**func1**](OsapiApi.md#func1) | **GET** /osapi | list supported server API versions


# **func1**
> func1()

list supported server API versions

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OsapiApi()

try: 
    # list supported server API versions
    api_instance.func1()
except ApiException as e:
    print "Exception when calling OsapiApi->func1: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
