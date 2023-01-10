import duckdb
from dynamo_pandas import get_df
import pandas as pd

player_df = get_df(table="player_table")
player_df = player_df.sort_values(by=['Name'],ascending=True)

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

player = "Player2"

sql = f'''SELECT 
COUNT(CASE WHEN "Team A Player 1" = '{player}' AND "Team A Result?" > "Team B Result?" THEN 1 END) +
COUNT(CASE WHEN "Team A Player 2" = '{player}' AND "Team A Result?" > "Team B Result?" THEN 1 END) +
COUNT(CASE WHEN "Team A Player 3" = '{player}' AND "Team A Result?" > "Team B Result?" THEN 1 END) +
COUNT(CASE WHEN "Team A Player 4" = '{player}' AND "Team A Result?" > "Team B Result?" THEN 1 END) +
COUNT(CASE WHEN "Team A Player 5" = '{player}' AND "Team A Result?" > "Team B Result?" THEN 1 END) +
COUNT(CASE WHEN "Team B Player 1" = '{player}' AND "Team A Result?" < "Team B Result?" THEN 1 END) +
COUNT(CASE WHEN "Team B Player 2" = '{player}' AND "Team A Result?" < "Team B Result?" THEN 1 END) +
COUNT(CASE WHEN "Team B Player 3" = '{player}' AND "Team A Result?" < "Team B Result?" THEN 1 END) +
COUNT(CASE WHEN "Team B Player 4" = '{player}' AND "Team A Result?" < "Team B Result?" THEN 1 END) +
COUNT(CASE WHEN "Team B Player 5" = '{player}' AND "Team A Result?" < "Team B Result?" THEN 1 END)
    FROM results_df;'''
result = duckdb.query(sql)
result = str(result).strip()
result = result[-2:].strip()
print(f'Calulated {player}s wins as {result}')