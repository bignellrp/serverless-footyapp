import duckdb
from dynamo_pandas import get_df
import pandas as pd

player_df = get_df(table="player_table")
player_df = player_df.filter(
                ['Name','Wins','Draws','Losses','Score','Win Percentage'])
##Convert multiple columns to numeric
player_df[['Wins','Draws',
            'Losses','Score',
            'Win Percentage']] = player_df[['Wins',
            'Draws','Losses','Score',
            'Win Percentage']].apply(pd.to_numeric)
##Sort by Score
player_df = player_df.sort_values(by=['Score'],
                                        ascending=False)

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
results_df['Date'] = pd.to_datetime(results_df.Date, format='%Y%m%d', errors='ignore')

player = 'Player2'
# test2 = duckdb.query(f'''SELECT * FROM results_df WHERE "Team A Player 1"= '{player}' AND "Team A Result?" < "Team B Result?"''').df()
# test = duckdb.query(f'''SELECT Wins,Draws FROM player_df''').df()

sql = f'''SELECT (Wins * 3 + Draws) 
        FROM player_df
        WHERE Name = '{player}';'''

result = duckdb.query(sql).df()
result.to_records(index=False)

print(f'Calulated {player}s score as {result}')