from services.get_date import next_wednesday
from services.get_data import player,results
import boto3

player_table = boto3.resource('dynamodb').Table('player_table')
results_table = boto3.resource('dynamodb').Table('results_table')
dynamodb = boto3.client('dynamodb')
player_class = player()
result = results()

def swap_player(players):
    '''Takes in a list of two players
    finds their score and swaps them 
    in the results table'''
    all_players = player_class.all_players
    player_current = players[0]
    player_new = players[1]

    for name, total in all_players:
        if name == player_current:
            player_current_score = total

    for name, total in all_players:
        if name == player_new:
            player_new_score = total

    #Work out difference between player scores
    player_score_difference = int(player_current_score) \
                                  - int(player_new_score)
    
    teamb = result.teamb()
    if player_current in teamb : 
        team = "B"
        team_result = result.totalb
        index = result.teamb
    else:
        team = "A"
        team_result = result.totala
        index = result.teama

    #Find index of player in team
    index = index.index(player_current)
    index = int(index) + 1

    #Find the score from Team A or B
    col_result_num = f'Team {team} Total'
    col_player = f'Team {team} Player {index}'

    #New Result is current result minus difference
    new_result = int(team_result) - player_score_difference 

    ##Update values with new player and new score,
    ##using date as the key

    results_table.update_item(   
        Key={'Date': next_wednesday},
        AttributeUpdates={
            col_result_num: new_result,
            col_player: player_new,
        },
    )
    print("Swapped player and updated score")
    return

def swap_existing_player(players):
    '''Takes in a list of two players
    finds their score and swaps them 
    in the results table if players
    are both playing'''

    all_players = player_class.all_players
    player_current = players[0]
    player_new = players[1]

    for name, total in all_players:
        if name == player_current:
            player_current_score = total

    for name, total in all_players:
        if name == player_new:
            player_new_score = total

    #Work out difference between player scores
    player_score_difference = int(player_current_score) \
                                  - int(player_new_score)

    teamb = result.teamb()
    if player_current in teamb : 
        team_curr = "B"
        team_new = "A"
        current_index = result.teamb()
        new_index = result.teama()
    else:
        team_curr = "A"
        team_new = "B"
        current_index = result.teama()
        new_index = result.teamb()

    #Find index of player in team
    current_index = current_index.index(player_current)
    current_index = int(current_index) + 1
    new_index = new_index.index(player_new)
    new_index = int(new_index) + 1

    #Constructing the Attribute Name
    curr_player = f'Team {team_curr} Player {current_index}'
    new_player = f'Team {team_new} Player {new_index}'

    #New Result is current result minus difference
    new_result_a = int(result.totala) - player_score_difference

    #New Result is current result minus difference
    new_result_b = int(result.totalb) - player_score_difference

    #Update values with new player and new score,
    #using date as the key
    #and with curr player swapped with new player

    results_table.update_item(   
        Key={'Date': next_wednesday},
        AttributeUpdates={
            'Team A Total': new_result_a,
            'Team B Total': new_result_b,
            curr_player: player_new,
            new_player: player_current,
        },
    )
    print("Swapped player and updated score")
    return