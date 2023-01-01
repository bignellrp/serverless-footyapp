import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'results_table'
#existing_tables = dynamodb.list_tables()['TableNames']

#if table_name not in existing_tables:
# try:
response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'Date',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Date',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 2,
        'WriteCapacityUnits': 1
    }
)
# except dynamodb.exceptions.ResourceInUseException:
#     print("Table Exists!")
#     pass