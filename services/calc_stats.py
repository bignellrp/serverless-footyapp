from dynamo_pandas import get_df
import pandas as pd

results_df = get_df(table="results_table")
results_df = results_df.filter(['Date',
                        'Team A Result?',
                        'Team B Result?',
                        'Team A Total',
                        'Team B Total',
                        'Team A Player 1',
                        'Team A Player 2',
                        'Team A Player 3',
                        'Team A Player 4',
                        'Team A Player 5',
                        'Team B Player 1',
                        'Team B Player 2',
                        'Team B Player 3',
                        'Team B Player 4',
                        'Team B Player 5',
                        'Team A Colour',
                        'Team B Colour'])
results_df['Date'] = pd.to_datetime(results_df.Date, 
                                format='%Y%m%d', errors='ignore')

def calc_wdl(player):
    '''Calculate wins,draws,losses for each player
    Where player is on the team and result 
    is WDL based on which team they were on'''
    df = results_df
    teama = ['Team A Player 1','Team A Player 2','Team A Player 3','Team A Player 4','Team A Player 5']
    teamb = ['Team B Player 1','Team B Player 2','Team B Player 3','Team B Player 4','Team B Player 5']
    wins = 0
    draws = 0
    losses = 0

    for team in teama:
        wins = wins + df[(df[team] == player) & (df['Team A Result?'] > df['Team B Result?'])].shape[0]
        draws = draws + df[(df[team] == player) & (df['Team A Result?'] == df['Team B Result?'])].shape[0]
        losses = losses + df[(df[team] == player) & (df['Team A Result?'] < df['Team B Result?'])].shape[0]

    for team in teamb:
        wins = wins + df[(df[team] == player) & (df['Team A Result?'] < df['Team B Result?'])].shape[0]
        draws = draws + df[(df[team] == player) & (df['Team A Result?'] == df['Team B Result?'])].shape[0]
        losses = losses + df[(df[team] == player) & (df['Team A Result?'] > df['Team B Result?'])].shape[0]
    return wins,draws,losses