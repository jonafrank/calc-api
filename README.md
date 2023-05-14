# Calc API

API that performs simple calc operations:
* Addition 
* Subtraction 
* Multiplication
* Division 
* Square Root
* Random String

In order to check a detailed API documentation go to

https://calc-api-doc.s3.amazonaws.com/index.html

When a new User is created automatically is assigned a balance of 100 points and each operation discount from this value.

## Technologies Used

* Serverless Framework
* AWS Lambda
* AWS DynamoDB
* AWS Cognito
* AWS CloudFront V2
* AWS Secret Manager
* Python
* Python unittest

## Deploy

You can deploy the application to a new AWS account within a free tier. Or an existing.

You will need to create in your AWS account a Secret Manager Vault and store a secret named API_KEY and then tore the arn in the `.env` file

### Requirements

* AWS CLI V2
* Serverless Framework installed globally.
* python3
* node.js >= v18

### Steps

1. `git clone git@github.com:jonafrank/calc-api.git`
2. `cd calc-api`
3. `aws configure`
4. `npm install`
5. `sls deploy`

## Local Development
### Requirements

* python3 
* localstack premium account

### How To

1. Run `python -m pip install -r requirements.dev.txt`

2. You can deploy the application to [LocalStack](https://localstack.cloud/) But you  will need a premium account since the AWS CloudFront V2 is a premium feature to run it locally.

Or you can deploy the Resources to AWS and run the Flask API locally with the next command

`sls wsgi serve`

More about WSGI (https://www.serverless.com/plugins/serverless-wsgi)

### Unit Tests

In order to run the unit tests locally run

`python -m coverage run -m unittest `

If you want to generate a html coverage report run 

`python -m coverage html`

