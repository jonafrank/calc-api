# DefaultApi

All URIs are relative to *https://pbqnjc55c3.execute-api.us-east-1.amazonaws.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsPost**](DefaultApi.md#operationsPost) | **POST** /operations | Perform a new Operation.
[**operationsTypesGet**](DefaultApi.md#operationsTypesGet) | **GET** /operations/types | Retrieves a list of valid operations.
[**recordsGet**](DefaultApi.md#recordsGet) | **GET** /records | Get List of Records
[**usersPost**](DefaultApi.md#usersPost) | **POST** /users | Creates a New User
[**usersTokensPost**](DefaultApi.md#usersTokensPost) | **POST** /users/tokens | Creates a new Access Token for authenticated requests.


<a name="operationsPost"></a>
# **operationsPost**
> OperationResult operationsPost(xApiKey, createOperation)

Perform a new Operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pbqnjc55c3.execute-api.us-east-1.amazonaws.com/api/v1");
    
    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Api Key provided in order to integrate Apps
    CreateOperation createOperation = new CreateOperation(); // CreateOperation | 
    try {
      OperationResult result = apiInstance.operationsPost(xApiKey, createOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#operationsPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xApiKey** | **String**| Api Key provided in order to integrate Apps |
 **createOperation** | [**CreateOperation**](CreateOperation.md)|  | [optional]

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

<a name="operationsTypesGet"></a>
# **operationsTypesGet**
> OperationsSuccess operationsTypesGet(xApiKey)

Retrieves a list of valid operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pbqnjc55c3.execute-api.us-east-1.amazonaws.com/api/v1");
    
    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Api Key provided in order to integrate Apps
    try {
      OperationsSuccess result = apiInstance.operationsTypesGet(xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#operationsTypesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xApiKey** | **String**| Api Key provided in order to integrate Apps |

### Return type

[**OperationsSuccess**](OperationsSuccess.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

<a name="recordsGet"></a>
# **recordsGet**
> RecordResult recordsGet(xApiKey)

Get List of Records

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pbqnjc55c3.execute-api.us-east-1.amazonaws.com/api/v1");
    
    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Api Key provided in order to integrate Apps
    try {
      RecordResult result = apiInstance.recordsGet(xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#recordsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xApiKey** | **String**| Api Key provided in order to integrate Apps |

### Return type

[**RecordResult**](RecordResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

<a name="usersPost"></a>
# **usersPost**
> UserCreated usersPost(xApiKey, userRequest)

Creates a New User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pbqnjc55c3.execute-api.us-east-1.amazonaws.com/api/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Api Key provided in order to integrate Apps
    UserRequest userRequest = new UserRequest(); // UserRequest | User to Add to the system
    try {
      UserCreated result = apiInstance.usersPost(xApiKey, userRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#usersPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xApiKey** | **String**| Api Key provided in order to integrate Apps |
 **userRequest** | [**UserRequest**](UserRequest.md)| User to Add to the system | [optional]

### Return type

[**UserCreated**](UserCreated.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

<a name="usersTokensPost"></a>
# **usersTokensPost**
> LoginSuccess usersTokensPost(xApiKey, userRequest)

Creates a new Access Token for authenticated requests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pbqnjc55c3.execute-api.us-east-1.amazonaws.com/api/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Api Key provided in order to integrate Apps
    UserRequest userRequest = new UserRequest(); // UserRequest | 
    try {
      LoginSuccess result = apiInstance.usersTokensPost(xApiKey, userRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#usersTokensPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xApiKey** | **String**| Api Key provided in order to integrate Apps |
 **userRequest** | [**UserRequest**](UserRequest.md)|  |

### Return type

[**LoginSuccess**](LoginSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

