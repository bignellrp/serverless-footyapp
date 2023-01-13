from services.get_data import results
from services.calc_stats import calc_wdl
import boto3

player_table = boto3.resource('dynamodb').Table('player_table')
dynamodb = boto3.client('dynamodb')
result = results()
played_thisweek = result.teama() + result.teamb()

def update_formulas():
    '''Updates formulas'''
    for name in played_thisweek:
        calc = calc_wdl(name)
        wins = calc[0]
        draws = calc[1]
        losses = calc[2]
        score = int(wins) * 3 + int(draws)
        played = int(wins) + int(draws) + int(losses)
        percentage = int(wins) / int(played) * 100
        percentage = int(percentage)
        if int(wins) < 5:
            winpercentage = '0'
        else:
            winpercentage = percentage
        player_table.update_item(
            Key={'Name': name},
            UpdateExpression="set Wins=:w, Draws=:d, Losses=:l, Score=:s, Played=:p, #pc=:pc, #wp=:wp",
            ExpressionAttributeNames={
                '#pc': 'Percent Calc',
                '#wp': 'Win Percentage'},
            ExpressionAttributeValues={
                ':w': wins,
                ':d': draws,
                ':l': losses,
                ':s': score,
                ':p': played,
                ':pc': percentage,
                ':wp': winpercentage},
            ReturnValues="UPDATED_NEW"
        )
    print("Updated Formulas")
    return