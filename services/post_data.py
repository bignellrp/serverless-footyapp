from services.get_date import next_wednesday
from services.get_data import player
from services.post_stats import update_formulas
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
        player_table.update_item(
            Key={'Name': name},
            UpdateExpression="set Playing=:p",
            ExpressionAttributeValues={
                ':p': 'o'},
            ReturnValues="UPDATED_NEW"
        )
    print("Wiping tally!")
    return

def update_tally(values):
    '''Function to update the player 
    tally using the values from the index page'''
    for name in values:
        player_table.update_item(
            Key={'Name': name},
            UpdateExpression="set Playing=:p",
            ExpressionAttributeValues={
                ':p': 'x'},
            ReturnValues="UPDATED_NEW"
        )
    print("Updated tally!")
    return

def update_result(values):
    '''Function to update the result row 
    using the values from the results page'''
    results_table.update_item(   
        Key={'Date': next_wednesday},
        AttributeUpdates={
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
        },
    )
    wipe_tally()
    update_formulas()
    return

def append_result(values):
    '''Function to update the result 
    using the values from the results page
    Takes in values to be added 
    and returns the command for 
    appending the data'''
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
    wipe_tally()
    update_formulas()
    return

def update_score_result(values):
    '''Function to update the result using 
    the values from the results page
    Takes in values to be added to sheet and 
    returns the gspread command for updating row
    Updates both Score A and Score B 
    from a list of two values.'''
    results_table.update_item(   
        Key={'Date': next_wednesday, 'Team A Result?': '-'},
        AttributeUpdates={
            'Team A Result?': values[0],
            'Team B Result?': values[1]}
    )
    update_formulas()
    return

def update_scorea(value):
    '''Function to update the result using 
    the values from the results page
    Takes in value to be added to the table updates item'''
    results_table.update_item(   
        Key={'Date': next_wednesday, 'Team A Result?': '-'},
        AttributeUpdates={
            'Team A Result?': value}
    )
    update_formulas()
    return

def update_scoreb(value):
    '''Function to update the result using 
    the values from the results page
    Takes in value to be added to the table updates item'''
    results_table.update_item(   
        Key={'Date': next_wednesday, 'Team A Result?': '-'},
        AttributeUpdates={
            'Team B Result?': value}
    )
    update_formulas()
    return

def update_coloura(value):
    '''Function to update the result using 
    the values from the results page
    Takes in value to be added to the table updates item'''
    results_table.update_item(   
        Key={'Date': next_wednesday, 'Team A Result?': '-'},
        AttributeUpdates={
            'Team A Colour': value}
    )
    return

def update_colourb(value):
    '''Function to update the result using 
    the values from the results page
    Takes in value to be added to the table updates item'''
    results_table.update_item(   
        Key={'Date': next_wednesday, 'Team A Result?': '-'},
        AttributeUpdates={
            'Team B Colour': value}
    )
    return

def update_playing_status(player):
    '''Takes in a player 
    and adds x into the playing column'''
    player_table.update_item(
        Key={'Name': player},
        UpdateExpression="set Playing=:p",
        ExpressionAttributeValues={
            ':p': 'x'},
        ReturnValues="UPDATED_NEW"
    )
    print("Updated playing status for:",player)
    return

def modify_playing_status(player):
    '''Takes in a player
    and adds o into the playing column'''
    player_table.update_item(
        Key={'Name': player},
        UpdateExpression="set Playing=:p",
        ExpressionAttributeValues={
            ':p': 'o'},
        ReturnValues="UPDATED_NEW"
    )
    print("Modified playing status for:",player)
    return

def add_new_player(player):
    '''Appends New Row with a new 
    player and generic score'''
    new_player = [player,int(77)] 

    player_table.update_item(
        Key={'Name': player},
        UpdateExpression="set Name=:n, Total=:t",
        ExpressionAttributeValues={
            ':n': new_player[0],
            ':t': new_player[1]},
        ReturnValues="UPDATED_NEW"
    )
    print("Added new player called:",player)
    return

def remove_player(player):
    '''Deletes player from player table'''
    player_table.delete_item(
        Key={'Name': player}
    )
    print("Deleted",player)
    return