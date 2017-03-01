# swagger_client.WorkItemsApi

All URIs are relative to *https://pulse.qas-labs.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_work_item**](WorkItemsApi.md#create_work_item) | **POST** /work-items | createWorkItem
[**delete_work_item**](WorkItemsApi.md#delete_work_item) | **DELETE** /work-items/{id} | deleteWorkItem
[**get_all_work_items**](WorkItemsApi.md#get_all_work_items) | **GET** /work-items | getWorkItems
[**get_work_item**](WorkItemsApi.md#get_work_item) | **GET** /work-items/{id} | getWorkItem
[**update_work_item**](WorkItemsApi.md#update_work_item) | **PUT** /work-items/{id} | updateWorkItem


# **create_work_item**
> Success create_work_item(body)

createWorkItem

Create WorkItem with new data

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
api_instance = swagger_client.WorkItemsApi()
body = swagger_client.WorkItems() # WorkItems | WorkItem object that needs to be added

try: 
    # createWorkItem
    api_response = api_instance.create_work_item(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkItemsApi->create_work_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkItems**](WorkItems.md)| WorkItem object that needs to be added | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_item**
> Success delete_work_item(id)

deleteWorkItem

Delete data of a WorkItem

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
api_instance = swagger_client.WorkItemsApi()
id = 'id_example' # str | Id of the WorkItem.

try: 
    # deleteWorkItem
    api_response = api_instance.delete_work_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkItemsApi->delete_work_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the WorkItem. | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_work_items**
> list[WorkItems] get_all_work_items()

getWorkItems

Get list data of WorkItems

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
api_instance = swagger_client.WorkItemsApi()

try: 
    # getWorkItems
    api_response = api_instance.get_all_work_items()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkItemsApi->get_all_work_items: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WorkItems]**](WorkItems.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_item**
> WorkItems get_work_item(id)

getWorkItem

Get data of WorkItem by WorkItem's id

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
api_instance = swagger_client.WorkItemsApi()
id = 'id_example' # str | Id of the WorkItem.

try: 
    # getWorkItem
    api_response = api_instance.get_work_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkItemsApi->get_work_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the WorkItem. | 

### Return type

[**WorkItems**](WorkItems.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_work_item**
> Success update_work_item(id, body)

updateWorkItem

Update WorkItem with new data

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
api_instance = swagger_client.WorkItemsApi()
id = 'id_example' # str | Id of the WorkItem.
body = swagger_client.WorkItems() # WorkItems | WorkItem object that needs to be updated

try: 
    # updateWorkItem
    api_response = api_instance.update_work_item(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkItemsApi->update_work_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the WorkItem. | 
 **body** | [**WorkItems**](WorkItems.md)| WorkItem object that needs to be updated | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

