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


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.OneOfintegerstring;

/**
 * RecordResultAttributes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-05-13T21:51:33.934795-03:00[America/Argentina/Buenos_Aires]")
public class RecordResultAttributes {
  public static final String SERIALIZED_NAME_OPERATION_ID = "operation_id";
  @SerializedName(SERIALIZED_NAME_OPERATION_ID)
  private Integer operationId;

  public static final String SERIALIZED_NAME_USER_ID = "user_id";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private String userId;

  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Integer amount;

  public static final String SERIALIZED_NAME_USER_BALANCE = "user_balance";
  @SerializedName(SERIALIZED_NAME_USER_BALANCE)
  private Integer userBalance;

  public static final String SERIALIZED_NAME_OPERATION_RESPONSE = "operation_response";
  @SerializedName(SERIALIZED_NAME_OPERATION_RESPONSE)
  private OneOfintegerstring operationResponse = null;

  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;


  public RecordResultAttributes operationId(Integer operationId) {
    
    this.operationId = operationId;
    return this;
  }

   /**
   * Get operationId
   * @return operationId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getOperationId() {
    return operationId;
  }


  public void setOperationId(Integer operationId) {
    this.operationId = operationId;
  }


  public RecordResultAttributes userId(String userId) {
    
    this.userId = userId;
    return this;
  }

   /**
   * Get userId
   * @return userId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getUserId() {
    return userId;
  }


  public void setUserId(String userId) {
    this.userId = userId;
  }


  public RecordResultAttributes amount(Integer amount) {
    
    this.amount = amount;
    return this;
  }

   /**
   * Get amount
   * @return amount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getAmount() {
    return amount;
  }


  public void setAmount(Integer amount) {
    this.amount = amount;
  }


  public RecordResultAttributes userBalance(Integer userBalance) {
    
    this.userBalance = userBalance;
    return this;
  }

   /**
   * Get userBalance
   * @return userBalance
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getUserBalance() {
    return userBalance;
  }


  public void setUserBalance(Integer userBalance) {
    this.userBalance = userBalance;
  }


  public RecordResultAttributes operationResponse(OneOfintegerstring operationResponse) {
    
    this.operationResponse = operationResponse;
    return this;
  }

   /**
   * Get operationResponse
   * @return operationResponse
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public OneOfintegerstring getOperationResponse() {
    return operationResponse;
  }


  public void setOperationResponse(OneOfintegerstring operationResponse) {
    this.operationResponse = operationResponse;
  }


  public RecordResultAttributes date(String date) {
    
    this.date = date;
    return this;
  }

   /**
   * Get date
   * @return date
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDate() {
    return date;
  }


  public void setDate(String date) {
    this.date = date;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RecordResultAttributes recordResultAttributes = (RecordResultAttributes) o;
    return Objects.equals(this.operationId, recordResultAttributes.operationId) &&
        Objects.equals(this.userId, recordResultAttributes.userId) &&
        Objects.equals(this.amount, recordResultAttributes.amount) &&
        Objects.equals(this.userBalance, recordResultAttributes.userBalance) &&
        Objects.equals(this.operationResponse, recordResultAttributes.operationResponse) &&
        Objects.equals(this.date, recordResultAttributes.date);
  }

  @Override
  public int hashCode() {
    return Objects.hash(operationId, userId, amount, userBalance, operationResponse, date);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RecordResultAttributes {\n");
    sb.append("    operationId: ").append(toIndentedString(operationId)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    userBalance: ").append(toIndentedString(userBalance)).append("\n");
    sb.append("    operationResponse: ").append(toIndentedString(operationResponse)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

