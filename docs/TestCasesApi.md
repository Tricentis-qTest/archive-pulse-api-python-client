# swagger_client.TestCasesApi

All URIs are relative to *https://pulse.qas-labs.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_case**](TestCasesApi.md#create_test_case) | **POST** /test-cases | createTestCase
[**delete_test_case**](TestCasesApi.md#delete_test_case) | **DELETE** /test-cases/{id} | deleteTestCase
[**get_all_test_cases**](TestCasesApi.md#get_all_test_cases) | **GET** /test-cases | getTestCases
[**get_test_case**](TestCasesApi.md#get_test_case) | **GET** /test-cases/{id} | getTestCase
[**update_test_case**](TestCasesApi.md#update_test_case) | **PUT** /test-cases/{id} | updateTestCase


# **create_test_case**
> Success create_test_case(body)

createTestCase

Create TestCase with new data

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
api_instance = swagger_client.TestCasesApi()
body = swagger_client.TestCases() # TestCases | TestCase object that needs to be added

try: 
    # createTestCase
    api_response = api_instance.create_test_case(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCasesApi->create_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TestCases**](TestCases.md)| TestCase object that needs to be added | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_case**
> Success delete_test_case(id)

deleteTestCase

Delete data of a TestCase

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
api_instance = swagger_client.TestCasesApi()
id = 'id_example' # str | Id of the TestCase.

try: 
    # deleteTestCase
    api_response = api_instance.delete_test_case(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCasesApi->delete_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the TestCase. | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_test_cases**
> list[TestCases] get_all_test_cases()

getTestCases

Get list data of TestCases

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
api_instance = swagger_client.TestCasesApi()

try: 
    # getTestCases
    api_response = api_instance.get_all_test_cases()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCasesApi->get_all_test_cases: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TestCases]**](TestCases.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_case**
> TestCases get_test_case(id)

getTestCase

Get data of TestCase by TestCase's id

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
api_instance = swagger_client.TestCasesApi()
id = 'id_example' # str | Id of the TestCase.

try: 
    # getTestCase
    api_response = api_instance.get_test_case(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCasesApi->get_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the TestCase. | 

### Return type

[**TestCases**](TestCases.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_case**
> Success update_test_case(id, body)

updateTestCase

Update TestCase with new data

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
api_instance = swagger_client.TestCasesApi()
id = 'id_example' # str | Id of the TestCase.
body = swagger_client.TestCases() # TestCases | TestCase object that needs to be updated

try: 
    # updateTestCase
    api_response = api_instance.update_test_case(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCasesApi->update_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the TestCase. | 
 **body** | [**TestCases**](TestCases.md)| TestCase object that needs to be updated | 

### Return type

[**Success**](Success.md)

### Authorization

[apiHeaderToken](../README.md#apiHeaderToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

