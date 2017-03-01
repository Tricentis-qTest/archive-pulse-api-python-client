# swagger_client.ReleasesApi

All URIs are relative to *https://pulse.qas-labs.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_release**](ReleasesApi.md#create_release) | **POST** /releases | createRelease
[**delete_release**](ReleasesApi.md#delete_release) | **DELETE** /releases/{id} | deleteRelease
[**get_all_releases**](ReleasesApi.md#get_all_releases) | **GET** /releases | getReleases
[**get_release**](ReleasesApi.md#get_release) | **GET** /releases/{id} | getRelease
[**update_release**](ReleasesApi.md#update_release) | **PUT** /releases/{id} | updateRelease


# **create_release**
> Success create_release(body)

createRelease

Create Release with new data

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
api_instance = swagger_client.ReleasesApi()
body = swagger_client.Releases() # Releases | Release object that needs to be added

try: 
    # createRelease
    api_response = api_instance.create_release(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->create_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Releases**](Releases.md)| Release object that needs to be added | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_release**
> Success delete_release(id)

deleteRelease

Delete data of a Release

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
api_instance = swagger_client.ReleasesApi()
id = 'id_example' # str | Id of the Release.

try: 
    # deleteRelease
    api_response = api_instance.delete_release(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->delete_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Release. | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_releases**
> list[Releases] get_all_releases()

getReleases

Get list data of Releases

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
api_instance = swagger_client.ReleasesApi()

try: 
    # getReleases
    api_response = api_instance.get_all_releases()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->get_all_releases: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Releases]**](Releases.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release**
> Releases get_release(id)

getRelease

Get data of Release by Release's id

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
api_instance = swagger_client.ReleasesApi()
id = 'id_example' # str | Id of the Release.

try: 
    # getRelease
    api_response = api_instance.get_release(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->get_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Release. | 

### Return type

[**Releases**](Releases.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_release**
> Success update_release(id, body)

updateRelease

Update Release with new data

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
api_instance = swagger_client.ReleasesApi()
id = 'id_example' # str | Id of the Release.
body = swagger_client.Releases() # Releases | Release object that needs to be updated

try: 
    # updateRelease
    api_response = api_instance.update_release(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->update_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Release. | 
 **body** | [**Releases**](Releases.md)| Release object that needs to be updated | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

