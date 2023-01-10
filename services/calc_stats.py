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

def calc_wins(player):
    '''Calculate wins for each player
    Where player is on the team and result 
    is < OR > opposite result'''
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
    return result

def calc_draws(player):
    '''Calculate draws for each player
    Where player is on the team and result 
    is < OR > opposite result'''
    sql = f'''SELECT 
    COUNT(CASE WHEN "Team A Player 1" = '{player}' AND "Team A Result?" = "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team A Player 2" = '{player}' AND "Team A Result?" = "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team A Player 3" = '{player}' AND "Team A Result?" = "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team A Player 4" = '{player}' AND "Team A Result?" = "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team A Player 5" = '{player}' AND "Team A Result?" = "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team B Player 1" = '{player}' AND "Team A Result?" = "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team B Player 2" = '{player}' AND "Team A Result?" = "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team B Player 3" = '{player}' AND "Team A Result?" = "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team B Player 4" = '{player}' AND "Team A Result?" = "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team B Player 5" = '{player}' AND "Team A Result?" = "Team B Result?" THEN 1 END)
        FROM results_df;'''
    result = duckdb.query(sql)
    result = str(result).strip()
    result = result[-2:].strip()
    print(f'Calulated {player}s draws as {result}')
    return result

def calc_losses(player):
    '''Calculate losses for each player
    Where player is on the team and result 
    is < OR > opposite result'''
    sql = f'''SELECT 
    COUNT(CASE WHEN "Team A Player 1" = '{player}' AND "Team A Result?" < "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team A Player 2" = '{player}' AND "Team A Result?" < "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team A Player 3" = '{player}' AND "Team A Result?" < "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team A Player 4" = '{player}' AND "Team A Result?" < "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team A Player 5" = '{player}' AND "Team A Result?" < "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team B Player 1" = '{player}' AND "Team A Result?" > "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team B Player 2" = '{player}' AND "Team A Result?" > "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team B Player 3" = '{player}' AND "Team A Result?" > "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team B Player 4" = '{player}' AND "Team A Result?" > "Team B Result?" THEN 1 END) +
    COUNT(CASE WHEN "Team B Player 5" = '{player}' AND "Team A Result?" > "Team B Result?" THEN 1 END)
        FROM results_df;'''
    result = duckdb.query(sql)
    result = str(result).strip()
    result = result[-2:].strip()
    print(f'Calulated {player}s losses as {result}')
    return result

def calc_score(player):
    '''Calculate score by Adding Wins to Draws'''
    sql = f'''SELECT (Wins * 3 + Draws) 
            FROM player_df
            WHERE Name = '{player}';'''
    result = duckdb.query(sql)
    result = str(result).strip()
    result = result[-2:].strip()
    print(f'Calulated {player}s score as {result}')
    return result

def calc_played(player):
    '''Calculate Played by Adding Wins to Draws to Losses'''
    sql = f'''SELECT (Wins + Draws + Losses) 
            FROM player_df
            WHERE Name = '{player}';'''
    result = duckdb.query(sql)
    result = str(result).strip()
    result = result[-2:].strip()
    print(f'Calulated {player}s games played as {result}')
    return result

def calc_percent(player):
    '''Calculate Percentage Calc'''
    sql = f'''SELECT (Wins / Played * 100) 
            FROM players
            WHERE Name = '{player}';'''
    result = duckdb.query(sql)
    result = str(result).strip()
    result = result[-2:].strip()
    print(f'Calulated {player}s percent calc as {result}')
    return result

def calc_wpercent(player):
    '''Calculate Win Percentage'''
    sql = f'''SELECT 
        CASE WHEN Wins < 5 THEN 0 ELSE (Wins / Played * 100) END
            FROM player_df
            WHERE Name = '{player}';'''
    result = duckdb.query(sql)
    result = str(result).strip()
    result = result[-2:].strip()
    print(f'Calulated {player}s win percentage as {result}')
    return result #All results seem to be zero