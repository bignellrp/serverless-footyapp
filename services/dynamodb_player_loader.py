import boto3
import json
#Loader file for DynamoDB
#Reference:
#https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.02.html

dynamodb = boto3.resource('dynamodb', region_name='eu-west-2', endpoint_url="https://dynamodb.eu-west-2.amazonaws.com")
table = dynamodb.Table('player_table')

with open('input_player_data.json') as json_file:
    data = json.load(json_file)
    for l in data:
        Name = l['Name']
        Total = l['Total']
        Wins = l['Wins']
        Draws = l['Draws']
        Losses = l['Losses']
        Score = l['Score']
        Playing = l['Playing']
        Played = l['Played']
        PercentCalc = l['Percent Calc']
        WinPercentage = l['Win Percentage']
        response = table.put_item(
            Item = {
                'Name':{"S": Name},
                'Total':{"N":Total},
                'Wins':{"N":Wins},
                'Draws':{"N":Draws},
                'Losses':{"N":Losses},
                'Score':{"N":Score},
                'Playing':{"S":Playing},
                'Played':{"N":Played},
                'Percent Calc':{"N":PercentCalc},
                'Win Percentage':{"N":WinPercentage}
            }
        )
        print("Put item succeeded")
        print(json.dumps(response, indent=4))