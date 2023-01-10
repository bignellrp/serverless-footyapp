from services.get_date import next_wednesday
from services.get_spread import player,results
from services.get_stats import stats
import boto3

player_table = boto3.resource('dynamodb').Table('player_table')
results_table = boto3.resource('dynamodb').Table('results_table')
dynamodb = boto3.client('dynamodb')
get_stats = stats()
players = player()
all_players = players.all_players()

class update():
	
    def __init__(self):
        '''Initialise the class and post all
        updates to player stats'''
        
    
    def update_wins(self):
        '''Updates formulas for wins'''
        for name,total in all_players:
            print(f"Sending {name} for Win calculation.")
            calc = get_stats.calc_wins(name)
            player_table.update_item(
                Key={'Name': name},
                UpdateExpression="set Wins=:w",
                ExpressionAttributeValues={
                    ':w': calc},
                ReturnValues="UPDATED_NEW"
            )
        print("Updated Wins")
        return

    def update_draws(self):
        '''Updates formulas for draws'''
        for name,total in all_players:
            calc = get_stats.calc_draws(name)
            player_table.update_item(
                Key={'Name': name},
                UpdateExpression="set Draws=:d",
                ExpressionAttributeValues={
                    ':d': calc},
                ReturnValues="UPDATED_NEW"
            )
        print("Updated Draws")
        return

    def update_losses(self):
        '''Updates formulas for losses'''
        for name,total in all_players:
            calc = get_stats.calc_losses(name)
            player_table.update_item(
                Key={'Name': name},
                UpdateExpression="set Losses=:l",
                ExpressionAttributeValues={
                    ':l': calc},
                ReturnValues="UPDATED_NEW"
            )
        print("Updated Losses")
        return

    def update_score(self):
        '''Updates formulas for score'''
        for name,total in all_players:
            calc = get_stats.calc_score(name)
            player_table.update_item(
                Key={'Name': name},
                UpdateExpression="set Score=:s",
                ExpressionAttributeValues={
                    ':s': calc},
                ReturnValues="UPDATED_NEW"
            )
        print("Updated Score")
        return

    def update_played(self):
        '''Updates formulas for Played'''
        for name,total in all_players:
            calc = get_stats.calc_played(name)
            player_table.update_item(
                Key={'Name': name},
                UpdateExpression="set Played=:p",
                ExpressionAttributeValues={
                    ':p': calc},
                ReturnValues="UPDATED_NEW"
            )
        print("Updated Played")
        return

    def update_percent(self):
        '''Updates formulas for Percent Calc'''
        ## Win Percentage????
        # for name,total in all_players:
        #     calc = get_stats.calc_percent(name)
        #     player_table.update_item(
        #         Key={'Name': name},
        #         UpdateExpression="set Win Percentage=:wp",
        #         ExpressionAttributeValues={
        #             ':wp': calc},
        #         ReturnValues="UPDATED_NEW"
        #     )
        print("Updated Percent Calc")
        return

    def update_wpercent(self):
        '''Updates formulas for Win Percentage'''
        for name,total in all_players:
            calc = get_stats.calc_wpercent(name)
            player_table.update_item(
                Key={'Name': name},
                UpdateExpression="set Win Percentage=:wp",
                ExpressionAttributeValues={
                    ':wp': calc},
                ReturnValues="UPDATED_NEW"
            )
        print("Updated Win Percentage")
        return