# footyapp

A web app for managing a 5 a side footy team.

Select the players using the checkboxes and it should output a balanced team
for each side.

Coded using Serverless, Python, HTML and Flask using
[grayscale bootstrap template](https://startbootstrap.com/theme/grayscale)

You can test this by cloning this repo and running the following serverless commands:
You must have your aws credentials configured as serverless will build the following:
- API Gateway
- Lambda
- DynamoDB (for now you need to manually run the loader commands below to fill the db with data)

```
serverless plugin install -n serverless-wsgi
serverless plugin install -n serverless-python-requirements
serverless
Deploy Now (y)
python3 services/dynamodb_player_loader.py
python3 services/dynamodb_results_loader.py
```