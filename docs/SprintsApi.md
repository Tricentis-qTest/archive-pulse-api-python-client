# swagger_client.SprintsApi

All URIs are relative to *https://pulse.qas-labs.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sprint**](SprintsApi.md#create_sprint) | **POST** /sprints | createSprint
[**delete_sprint**](SprintsApi.md#delete_sprint) | **DELETE** /sprints/{id} | deleteSprint
[**get_all_sprints**](SprintsApi.md#get_all_sprints) | **GET** /sprints | getSprints
[**get_sprint**](SprintsApi.md#get_sprint) | **GET** /sprints/{id} | getSprint
[**update_sprint**](SprintsApi.md#update_sprint) | **PUT** /sprints/{id} | updateSprint


# **create_sprint**
> Success create_sprint(body)

createSprint

Create Sprint with new data

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
api_instance = swagger_client.SprintsApi()
body = swagger_client.Sprints() # Sprints | Sprint object that needs to be added

try: 
    # createSprint
    api_response = api_instance.create_sprint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SprintsApi->create_sprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Sprints**](Sprints.md)| Sprint object that needs to be added | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sprint**
> Success delete_sprint(id)

deleteSprint

Delete data of a Sprint

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
api_instance = swagger_client.SprintsApi()
id = 'id_example' # str | Id of the Sprint.

try: 
    # deleteSprint
    api_response = api_instance.delete_sprint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SprintsApi->delete_sprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Sprint. | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sprints**
> list[Sprints] get_all_sprints()

getSprints

Get list data of Sprints

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
api_instance = swagger_client.SprintsApi()

try: 
    # getSprints
    api_response = api_instance.get_all_sprints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SprintsApi->get_all_sprints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Sprints]**](Sprints.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sprint**
> Sprints get_sprint(id)

getSprint

Get data of Sprint by Sprint's id

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
api_instance = swagger_client.SprintsApi()
id = 'id_example' # str | Id of the Sprint.

try: 
    # getSprint
    api_response = api_instance.get_sprint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SprintsApi->get_sprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Sprint. | 

### Return type

[**Sprints**](Sprints.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sprint**
> Success update_sprint(id, body)

updateSprint

Update Sprint with new data

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
api_instance = swagger_client.SprintsApi()
id = 'id_example' # str | Id of the Sprint.
body = swagger_client.Sprints() # Sprints | Sprint object that needs to be updated

try: 
    # updateSprint
    api_response = api_instance.update_sprint(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SprintsApi->update_sprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Sprint. | 
 **body** | [**Sprints**](Sprints.md)| Sprint object that needs to be updated | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

