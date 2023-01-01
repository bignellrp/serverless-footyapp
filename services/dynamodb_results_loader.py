import boto3
import json
#Loader file for DynamoDB
#Reference:
#https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.02.html

dynamodb = boto3.resource('dynamodb', region_name='eu-west-2', endpoint_url="https://dynamodb.eu-west-2.amazonaws.com")
table = dynamodb.Table('results_table')

with open('input_results_data.json') as json_file:
    data = json.load(json_file)
    for l in data:
        Date = l['Date']
        ResultA = l['Team A Result?']
        ResultB = l['Team B Result?']
        TeamATotal = l['Team A Total']
        TeamBTotal = l['Team B Total']
        TeamAPlayer1 = l['Team A Player 1']
        TeamAPlayer2 = l['Team A Player 2']
        TeamAPlayer3 = l['Team A Player 3']
        TeamAPlayer4 = l['Team A Player 4']
        TeamAPlayer5 = l['Team A Player 5']
        TeamBPlayer1 = l['Team B Player 1']
        TeamBPlayer2 = l['Team B Player 2']
        TeamBPlayer3 = l['Team B Player 3']
        TeamBPlayer4 = l['Team B Player 4']
        TeamBPlayer5 = l['Team B Player 5']
        TeamAColour = l['Team A Colour']
        TeamBColour = l['Team B Colour']
        response = table.put_item(
            Item = {
                'Date':Date,
                'Team A Result?':ResultA,
                'Team B Result?':ResultB,
                'Team A Total':TeamATotal,
                'Team B Total':TeamBTotal,
                'Team A Player 1':TeamAPlayer1,
                'Team A Player 2':TeamAPlayer2,
                'Team A Player 3':TeamAPlayer3,
                'Team A Player 4':TeamAPlayer4,
                'Team A Player 5':TeamAPlayer5,
                'Team B Player 1':TeamBPlayer1,
                'Team B Player 2':TeamBPlayer2,
                'Team B Player 3':TeamBPlayer3,
                'Team B Player 4':TeamBPlayer4,
                'Team B Player 5':TeamBPlayer5,
                'Team A Colour':TeamAColour,
                'Team B Colour':TeamBColour
            }
        )
        print("Put item succeeded")
        print(json.dumps(response, indent=4))