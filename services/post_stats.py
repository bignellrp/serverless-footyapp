from services.get_data import player
from services.calc_stats import *
import boto3

player_table = boto3.resource('dynamodb').Table('player_table')
results_table = boto3.resource('dynamodb').Table('results_table')
dynamodb = boto3.client('dynamodb')
players = player()
all_players = players.all_players()

def update_formulas():
    '''Updates all forumulas'''
    update_wins()
    update_draws()
    update_losses()
    update_score()
    update_percent()
    update_wpercent()
    print("Updated all formulas")
    return

def update_wins():
    '''Updates formulas for wins'''
    for name,total in all_players:
        print(f"Sending {name} for Win calculation.")
        calc = calc_wins(name)
        player_table.update_item(
            Key={'Name': name},
            UpdateExpression="set Wins=:w",
            ExpressionAttributeValues={
                ':w': calc},
            ReturnValues="UPDATED_NEW"
        )
    print("Updated Wins")
    return

def update_draws():
    '''Updates formulas for draws'''
    for name,total in all_players:
        calc = calc_draws(name)
        player_table.update_item(
            Key={'Name': name},
            UpdateExpression="set Draws=:d",
            ExpressionAttributeValues={
                ':d': calc},
            ReturnValues="UPDATED_NEW"
        )
    print("Updated Draws")
    return

def update_losses():
    '''Updates formulas for losses'''
    for name,total in all_players:
        calc = calc_losses(name)
        player_table.update_item(
            Key={'Name': name},
            UpdateExpression="set Losses=:l",
            ExpressionAttributeValues={
                ':l': calc},
            ReturnValues="UPDATED_NEW"
        )
    print("Updated Losses")
    return

def update_score():
    '''Updates formulas for score'''
    for name,total in all_players:
        calc = calc_score(name)
        player_table.update_item(
            Key={'Name': name},
            UpdateExpression="set Score=:s",
            ExpressionAttributeValues={
                ':s': calc},
            ReturnValues="UPDATED_NEW"
        )
    print("Updated Score")
    return

def update_played():
    '''Updates formulas for Played'''
    for name,total in all_players:
        calc = calc_played(name)
        player_table.update_item(
            Key={'Name': name},
            UpdateExpression="set Played=:p",
            ExpressionAttributeValues={
                ':p': calc},
            ReturnValues="UPDATED_NEW"
        )
    print("Updated Played")
    return

def update_percent():
    '''Updates formulas for Percent Calc'''
    for name,total in all_players:
        calc = calc_percent(name)
        player_table.update_item(
            Key={'Name': name},
            UpdateExpression="set Percent Calc=:pc",
            ExpressionAttributeValues={
                ':pc': calc},
            ReturnValues="UPDATED_NEW"
        )
    print("Updated Percent Calc")
    return

def update_wpercent():
    '''Updates formulas for Win Percentage'''
    for name,total in all_players:
        calc = calc_wpercent(name)
        player_table.update_item(
            Key={'Name': name},
            UpdateExpression="set Win Percentage=:wp",
            ExpressionAttributeValues={
                ':wp': calc},
            ReturnValues="UPDATED_NEW"
        )
    print("Updated Win Percentage")
    return