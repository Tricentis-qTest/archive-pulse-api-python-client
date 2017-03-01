# swagger_client.ComponentsApi

All URIs are relative to *https://pulse.qas-labs.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_component**](ComponentsApi.md#create_component) | **POST** /components | createComponent
[**delete_component**](ComponentsApi.md#delete_component) | **DELETE** /components/{id} | deleteComponent
[**get_all_components**](ComponentsApi.md#get_all_components) | **GET** /components | getComponents
[**get_component**](ComponentsApi.md#get_component) | **GET** /components/{id} | getComponent
[**update_component**](ComponentsApi.md#update_component) | **PUT** /components/{id} | updateComponent


# **create_component**
> Success create_component(body)

createComponent

Create Component with new data

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
api_instance = swagger_client.ComponentsApi()
body = swagger_client.Components() # Components | Component object that needs to be added

try: 
    # createComponent
    api_response = api_instance.create_component(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->create_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Components**](Components.md)| Component object that needs to be added | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_component**
> Success delete_component(id)

deleteComponent

Delete data of a Component

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
api_instance = swagger_client.ComponentsApi()
id = 'id_example' # str | Id of the Component.

try: 
    # deleteComponent
    api_response = api_instance.delete_component(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->delete_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Component. | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_components**
> list[Components] get_all_components()

getComponents

Get list data of Components

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
api_instance = swagger_client.ComponentsApi()

try: 
    # getComponents
    api_response = api_instance.get_all_components()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_all_components: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Components]**](Components.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component**
> Components get_component(id)

getComponent

Get data of Component by Component's id

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
api_instance = swagger_client.ComponentsApi()
id = 'id_example' # str | Id of the Component.

try: 
    # getComponent
    api_response = api_instance.get_component(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Component. | 

### Return type

[**Components**](Components.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_component**
> Success update_component(id, body)

updateComponent

Update Component with new data

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
api_instance = swagger_client.ComponentsApi()
id = 'id_example' # str | Id of the Component.
body = swagger_client.Components() # Components | Component object that needs to be updated

try: 
    # updateComponent
    api_response = api_instance.update_component(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->update_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Component. | 
 **body** | [**Components**](Components.md)| Component object that needs to be updated | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

