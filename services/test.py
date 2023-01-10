import boto3
import json
import decimal

dynamodb = boto3.client('dynamodb')

player = 'Player2'
sql1 = f"""SELECT "Wins","Draws" FROM "player_table" WHERE "Name" = '{player}';"""

response1 = dynamodb.execute_statement(Statement= sql1)

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

for i in response1[u'Items']:
    d = json.dumps(i, cls=DecimalEncoder)

print(d["S"])