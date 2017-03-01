# swagger_client.ProjectsApi

All URIs are relative to *https://pulse.qas-labs.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects | createProject
[**get_all_projects**](ProjectsApi.md#get_all_projects) | **GET** /projects | getProjects
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects/{id} | getProject
[**update_project**](ProjectsApi.md#update_project) | **PUT** /projects/{id} | updateProject


# **create_project**
> Success create_project(body)

createProject

Create Project with new data

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
api_instance = swagger_client.ProjectsApi()
body = swagger_client.Projects() # Projects | Project object that needs to be added

try: 
    # createProject
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Projects**](Projects.md)| Project object that needs to be added | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> list[Projects] get_all_projects()

getProjects

Get list data of Projects

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
api_instance = swagger_client.ProjectsApi()

try: 
    # getProjects
    api_response = api_instance.get_all_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_all_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Projects]**](Projects.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Projects get_project(id)

getProject

Get data of Project by Project's id

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
api_instance = swagger_client.ProjectsApi()
id = 'id_example' # str | Id of the Project.

try: 
    # getProject
    api_response = api_instance.get_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Project. | 

### Return type

[**Projects**](Projects.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Success update_project(id, body)

updateProject

Update Project with new data

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
api_instance = swagger_client.ProjectsApi()
id = 'id_example' # str | Id of the Project.
body = swagger_client.Projects() # Projects | Project object that needs to be updated

try: 
    # updateProject
    api_response = api_instance.update_project(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Project. | 
 **body** | [**Projects**](Projects.md)| Project object that needs to be updated | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

