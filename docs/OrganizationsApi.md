# swagger_client.OrganizationsApi

All URIs are relative to *https://pulse.qas-labs.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_organizations**](OrganizationsApi.md#get_all_organizations) | **GET** /organizations | getOrganizations
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /organizations/{id} | getOrganization


# **get_all_organizations**
> list[Organizations] get_all_organizations()

getOrganizations

Get list data of Organizations

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiHeaderToken
swagger_client.configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()

try: 
    # getOrganizations
    api_response = api_instance.get_all_organizations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_all_organizations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Organizations]**](Organizations.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> Organizations get_organization(id)

getOrganization

Get data of Organization by Organization's id

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiHeaderToken
swagger_client.configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api-token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
id = 'id_example' # str | Id of the Organization.

try: 
    # getOrganization
    api_response = api_instance.get_organization(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Organization. | 

### Return type

[**Organizations**](Organizations.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

