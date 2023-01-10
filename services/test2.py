import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('results_table')

response = table.query(
    KeyConditionExpression="Team A Player 1".eq(Player2)
    #FilterExpression=
    #ExpressionAttributeValues={}
)

print(response['Items'])
# for i in response['Items']:
#     print(i['year'], ":", i['title'])