from services.get_date import next_wednesday, closest_wednesday
from services.get_data import player
#from services.post_stats import update_formulas
import boto3

player_table = boto3.resource('dynamodb').Table('player_table')
results_table = boto3.resource('dynamodb').Table('results_table')
dynamodb = boto3.client('dynamodb')

def wipe_tally():
    '''Wipes the tally attribute for 
    all players setting it to o'''
    players = player()
    all_players = players.all_players()
    for name,totals in all_players:
        try:
            player_table.update_item(
                Key={'Name': name},
                UpdateExpression="set Playing=:p",
                ExpressionAttributeValues={
                    ':p': 'o'},
                ReturnValues="UPDATED_NEW"
            )
        except Exception as msg:
            print(f"Oops, could not update: {msg}")
    print("Wiping tally!")
    return

def update_tally(values):
    '''Function to update the player 
    tally using the values from the index page'''
    for name in values:
        try:
            player_table.update_item(
                Key={'Name': name},
                UpdateExpression="set Playing=:p",
                ExpressionAttributeValues={
                    ':p': 'x'},
                ReturnValues="UPDATED_NEW"
            )
        except Exception as msg:
            print(f"Oops, could not update: {msg}")
    print("Updated tally!")
    return

def update_result(values):
    '''Function to update the result row 
    using the values from the results page'''
    try:
        results_table.update_item(
            Key={'Date': next_wednesday},
            UpdateExpression="set #1=:1, #2=:2, #3=:3, #4=:4, #5=:5, #6=:6, #7=:7, #8=:8, #9=:9, #10=:10, #11=:11, #12=:12, #13=:13, #14=:14, #15=:15, #16=:16",
            ExpressionAttributeNames={
                '#1': 'Team A Result?',
                '#2': 'Team B Result?',
                '#3': 'Team A Total',
                '#4': 'Team B Total',
                '#5': 'Team A Player 1',
                '#6': 'Team A Player 2',
                '#7': 'Team A Player 3',
                '#8': 'Team A Player 4',
                '#9': 'Team A Player 5',
                '#10': 'Team B Player 1',
                '#11': 'Team B Player 2',
                '#12': 'Team B Player 3',
                '#13': 'Team B Player 4',
                '#14': 'Team B Player 5',
                '#15': 'Team A Colour',
                '#16': 'Team B Colour'},
            ExpressionAttributeValues={
                ':1': values[1],
                ':2': values[2],
                ':3': values[3],
                ':4': values[4],
                ':5': values[5],
                ':6': values[6],
                ':7': values[7],
                ':8': values[8],
                ':9': values[9],
                ':10': values[10],
                ':11': values[11],
                ':12': values[12],
                ':13': values[13],
                ':14': values[14],
                ':15': values[15],
                ':16': values[16]},
            ReturnValues="UPDATED_NEW"
        )
    except Exception as msg:
        print(f"Oops, could not update: {msg}")
    wipe_tally()
    return

def append_result(values):
    '''Function to update the result 
    using the values from the results page
    Takes in values to be added 
    and returns the command for 
    appending the data'''
    try:
        results_table.put_item(
            Item={
            'Date': values[0],
            'Team A Result?': values[1],
            'Team B Result?': values[2],
            'Team A Total': values[3],
            'Team B Total': values[4],
            'Team A Player 1': values[5],
            'Team A Player 2': values[6],
            'Team A Player 3': values[7],
            'Team A Player 4': values[8],
            'Team A Player 5': values[9],
            'Team B Player 1': values[10],
            'Team B Player 2': values[11],
            'Team B Player 3': values[12],
            'Team B Player 4': values[13],
            'Team B Player 5': values[14],
            'Team A Colour': values[15],
            'Team B Colour': values[16]
            }
        )
    except Exception as msg:
        print(f"Oops, could not update: {msg}")
    wipe_tally()
    return

def update_score_result(values):
    '''Function to update the result using 
    the values from the results page
    Takes in values to be added to sheet and 
    returns the gspread command for updating row
    Updates both Score A and Score B 
    from a list of two values.'''
    try:
        results_table.update_item(   
            Key={'Date': closest_wednesday},
            UpdateExpression="set #1=:1, #2=:2",
            ConditionExpression="#1=:3",
            ExpressionAttributeNames={
                '#1': 'Team A Result?',
                '#2': 'Team B Result?'},
            ExpressionAttributeValues={
                ':1': values[0],
                ':2': values[1],
                ':3': '-'},
            ReturnValues="UPDATED_NEW"
        )
    except Exception as msg:
        print(f"Oops, could not update: {msg}")
    #update_formulas()
    return