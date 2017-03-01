# swagger_client.LoginLogoutApi

All URIs are relative to *https://pulse.qas-labs.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](LoginLogoutApi.md#login) | **POST** /login | login
[**logout**](LoginLogoutApi.md#logout) | **POST** /logout | logout


# **login**
> InlineResponse200 login(domain, username, password)

login

Get Pulse user token.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginLogoutApi()
domain = 'domain_example' # str | Domain name of user
username = 'username_example' # str | Username of user
password = 'password_example' # str | Password of user

try: 
    # login
    api_response = api_instance.login(domain, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginLogoutApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name of user | 
 **username** | **str**| Username of user | 
 **password** | **str**| Password of user | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> InlineResponse2001 logout(api_token)

logout

Logout user from Pulse

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginLogoutApi()
api_token = 'api_token_example' # str | 

try: 
    # logout
    api_response = api_instance.logout(api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginLogoutApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

