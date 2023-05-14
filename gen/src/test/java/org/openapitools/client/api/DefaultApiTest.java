/*
 * Calc API
 * Calc api for truenorth challenge
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CreateOperation;
import org.openapitools.client.model.LoginSuccess;
import org.openapitools.client.model.OperationResult;
import org.openapitools.client.model.OperationsSuccess;
import org.openapitools.client.model.RecordResult;
import org.openapitools.client.model.UserCreated;
import org.openapitools.client.model.UserRequest;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Ignore
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    
    /**
     * Perform a new Operation.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void operationsPostTest() throws ApiException {
        String xApiKey = null;
        CreateOperation createOperation = null;
        OperationResult response = api.operationsPost(xApiKey, createOperation);

        // TODO: test validations
    }
    
    /**
     * Retrieves a list of valid operations.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void operationsTypesGetTest() throws ApiException {
        String xApiKey = null;
        OperationsSuccess response = api.operationsTypesGet(xApiKey);

        // TODO: test validations
    }
    
    /**
     * Get List of Records
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void recordsGetTest() throws ApiException {
        String xApiKey = null;
        RecordResult response = api.recordsGet(xApiKey);

        // TODO: test validations
    }
    
    /**
     * Creates a New User
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void usersPostTest() throws ApiException {
        String xApiKey = null;
        UserRequest userRequest = null;
        UserCreated response = api.usersPost(xApiKey, userRequest);

        // TODO: test validations
    }
    
    /**
     * Creates a new Access Token for authenticated requests.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void usersTokensPostTest() throws ApiException {
        String xApiKey = null;
        UserRequest userRequest = null;
        LoginSuccess response = api.usersTokensPost(xApiKey, userRequest);

        // TODO: test validations
    }
    
}