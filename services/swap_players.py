from services.get_date import next_wednesday
from services.get_spread import player,results
import boto3

player_table = boto3.resource('dynamodb').Table('player_table')
results_table = boto3.resource('dynamodb').Table('results_table')
dynamodb = boto3.client('dynamodb')

# def swap_player(players):
#     '''Takes in a list of two players
#     finds their score and swaps them 
#     in the results table'''

#     # result = results()
#     # df = result.all_results()
#     # last_row = df.loc[df['Date'] == next_wednesday]
#     # result = df.loc[df['Team A Player 1'].str.contains(pat = 'Bernard')]
#     # print(result)

#     c = conn.cursor()
#     #Find the Current Players name and the row
#     #player_current = ws_players.find(player[0])
#     player_current = players[0]

#     #Find the New Players name and the row
#     #player_new = ws_players.find(player[1]) 
#     player_new = players[1]

#     #Find the Total column
#     #clm_total = ws_players.find('Total')

#     #Convert Total Col Number to a Letter
#     #clm_total = colnum_string(clm_total.col) 

#     #Combine Col letter and row num into range
#     #player_current_range = str(clm_total)+str(player_current.row)

#     #Combine Col letter and row num into range
#     #player_new_range = str(clm_total)+str(player_new.row) 

#     #Grab score cell using range
#     #player_current_score = ws_players.acell(player_current_range).value 
#     player_current_score = c.execute(
#         'SELECT "Total" FROM players WHERE "Name" = ?;', (players[0], ))
#     player_current_score = c.fetchone()
#     player_current_score = player_current_score[0]
#     #Grab score cell using range
#     #player_new_score = ws_players.acell(player_new_range).value 
#     player_new_score = c.execute(
#         'SELECT "Total" FROM players WHERE "Name" = ?;', (players[1], ))
#     player_new_score = c.fetchone()
#     player_new_score = player_new_score[0]
#     #Work out difference between player scores
#     player_score_difference = int(player_current_score) \
#                                   - int(player_new_score)

#     # print(f"The difference between player \
#     #     scores is {player_score_difference}")
#     #row = ws_results.find('-') #Find the row with dash

#     #Find the Current Players name on the row with a dash
#     #player_current = ws_results.find(player[0], in_row=row.row) 

#     #If player col number > 10 E.g. above J then team is B  
#     # if player_current.col > 10 : 
#     #     team = "B"
#     # else:
#     #     team = "A"
#     result = results()
#     teamb = result.teamb()
#     if player_current in teamb : 
#         team = "B"
#     else:
#         team = "A"
#     #Find the column with the score from Team A or B
#     #col_result_num = ws_results.find('Team ' + team + ' Total')
#     #col_result_num = f'"Team " + {team} + " Total"'
#     col_result_num = f'Team {team} Total'
#     col_player1 = f'Team {team} Player 1'
#     col_player2 = f'Team {team} Player 2'
#     col_player3 = f'Team {team} Player 3'
#     col_player4 = f'Team {team} Player 4'
#     col_player5 = f'Team {team} Player 5'

#     #Convert Col Number to a Letter
#     #col_result = colnum_string(col_result_num.col) 

#     #Combine Col letter and row num into range
#     #team_result_range = str(col_result)+str(row.row) 

#     #Grab current score for Team A or B
#     #team_result = ws_results.acell(team_result_range).value

#     team_result = c.execute(
#         f'SELECT "{col_result_num}" FROM results WHERE "Date" = "{next_wednesday}"')
#     team_result = c.fetchone()
#     team_result = team_result[0]
#     #New Result is current result minus difference
#     new_result = int(team_result) - player_score_difference 

#     ##Update cell with new score,
#     ##using the row with the dash,
#     ##and column with Team Result
#     #ws_results.update_cell(row.row, col_result_num.col, new_result)
#     c.execute(f'UPDATE results SET "{col_result_num}" = {new_result} WHERE "Date" = "{next_wednesday}"')

#     ##Update cell with new player,
#     ##using the row with the dash,
#     ##and column with Player Current
#     #ws_results.update_cell(row.row, player_current.col, player[1])
#     c.execute(f'UPDATE results SET "{col_player1}" = "{player_new}" WHERE "Date" = "{next_wednesday}" AND "{col_player1}" = "{player_current}"')
#     c.execute(f'UPDATE results SET "{col_player2}" = "{player_new}" WHERE "Date" = "{next_wednesday}" AND "{col_player2}" = "{player_current}"')
#     c.execute(f'UPDATE results SET "{col_player3}" = "{player_new}" WHERE "Date" = "{next_wednesday}" AND "{col_player3}" = "{player_current}"')
#     c.execute(f'UPDATE results SET "{col_player4}" = "{player_new}" WHERE "Date" = "{next_wednesday}" AND "{col_player4}" = "{player_current}"')
#     c.execute(f'UPDATE results SET "{col_player5}" = "{player_new}" WHERE "Date" = "{next_wednesday}" AND "{col_player5}" = "{player_current}"')

#     print("Swapped player and updated score")
#     return

# def swap_existing_player(players):
#     '''Takes in a list of two players
#     finds their score and swaps them 
#     in the results table if players
#     are both playing'''

#     c = conn.cursor()
#     #Find the Current Players name and the row
#     #player_current = ws_players.find(player[0])
#     player_current = players[0]

#     #Find the New Players name and the row
#     #player_new = ws_players.find(player[1])
#     player_new = players[1]

#     #Find the Total column
#     #clm_total = ws_players.find('Total')

#     #Convert Total Col Number to a Letter
#     #clm_total = colnum_string(clm_total.col) 

#     #Combine Col letter and row num into range
#     #player_current_range = str(clm_total)+str(player_current.row)

#     #Combine Col letter and row num into range
#     #player_new_range = str(clm_total)+str(player_new.row) 

#     #Grab score cell using range
#     #player_current_score = ws_players.acell(player_current_range).value 

#     #Grab score cell using range
#     #player_new_score = ws_players.acell(player_new_range).value 

#     #Work out difference between player scores
#     #player_score_difference = int(player_current_score) \
#     #                              - int(player_new_score)

#     #print(f"The difference between player \
#     #    scores is {player_score_difference}")
#     #row = ws_results.find('-') #Find the row with dash

#     # #Find the Current Players name on the row with a dash
#     # player_current = ws_results.find(player[0], in_row=row.row) 

#     # #Find the New Players name on the row with a dash
#     # player_new = ws_results.find(player[1], in_row=row.row) 

#     #Grab score cell using range
#     #player_current_score = ws_players.acell(player_current_range).value 
#     player_current_score = c.execute(
#         'SELECT "Total" FROM players WHERE "Name" = ?;', (players[0], ))
#     player_current_score = c.fetchone()
#     player_current_score = player_current_score[0]
#     #Grab score cell using range
#     #player_new_score = ws_players.acell(player_new_range).value 
#     player_new_score = c.execute(
#         'SELECT "Total" FROM players WHERE "Name" = ?;', (players[1], ))
#     player_new_score = c.fetchone()
#     player_new_score = player_new_score[0]
#     #Work out difference between player scores
#     player_score_difference = int(player_current_score) \
#                                   - int(player_new_score)

#     # #If player col number > 10 E.g. above J then team is B  
#     # if player_current.col > 10 : 
#     #     team_curr = "B"
#     #     team_new = "A"
#     # else:
#     #     team_curr = "A"
#     #     team_new = "B"

#     result = results()
#     teamb = result.teamb()
#     if player_current in teamb : 
#         team_curr = "B"
#         team_new = "A"
#     else:
#         team_curr = "A"
#         team_new = "B"

#     curr_player1 = f'Team {team_curr} Player 1'
#     curr_player2 = f'Team {team_curr} Player 2'
#     curr_player3 = f'Team {team_curr} Player 3'
#     curr_player4 = f'Team {team_curr} Player 4'
#     curr_player5 = f'Team {team_curr} Player 5'
#     new_player1 = f'Team {team_new} Player 1'
#     new_player2 = f'Team {team_new} Player 2'
#     new_player3 = f'Team {team_new} Player 3'
#     new_player4 = f'Team {team_new} Player 4'
#     new_player5 = f'Team {team_new} Player 5'

#     # #Find the column with the score from Team A or B
#     # col_result_num_a = ws_results.find('Team ' + team_curr + ' Total')

#     # #Find the column with the score from Team A or B
#     # col_result_num_b = ws_results.find('Team ' + team_new + ' Total') 

#     # #Convert Col Number to a Letter
#     # col_result_a = colnum_string(col_result_num_a.col)

#     # #Convert Col Number to a Letter
#     # col_result_b = colnum_string(col_result_num_b.col)

#     # #Combine Col letter and row num into range
#     # team_result_range_a = str(col_result_a)+str(row.row)

#     # #Combine Col letter and row num into range
#     # team_result_range_b = str(col_result_b)+str(row.row)

#     # #Grab current score for Team A
#     # team_result_a = ws_results.acell(team_result_range_a).value
#     team_result_a = c.execute(
#         f'SELECT "Team A Total" FROM results WHERE "Date" = "{next_wednesday}"')
#     team_result_a = c.fetchone()
#     team_result_a = team_result_a[0]

#     # #Grab current score for Team B
#     # team_result_b = ws_results.acell(team_result_range_b).value
#     team_result_b = c.execute(
#         f'SELECT "Team B Total" FROM results WHERE "Date" = "{next_wednesday}"')
#     team_result_b = c.fetchone()
#     team_result_b = team_result_b[0]

#     # #New Result is current result minus difference
#     new_result_a = int(team_result_a) - player_score_difference

#     # #New Result is current result minus difference
#     new_result_b = int(team_result_b) - player_score_difference

#     # ##Update cell with new score,
#     # ##using the row with the dash,
#     # ##and column with Team Result
#     # ws_results.update_cell(row.row, col_result_num_a.col, new_result_a)
#     # ws_results.update_cell(row.row, col_result_num_b.col, new_result_b)
#     c.execute(f'UPDATE results SET "Team A Total" = {new_result_a} WHERE "Date" = "{next_wednesday}"')
#     c.execute(f'UPDATE results SET "Team B Total" = {new_result_b} WHERE "Date" = "{next_wednesday}"')

#     # ##Update cell with new player,
#     # ##using the row with the dash,
#     # ##and column with Player Current/New
#     # ws_results.update_cell(row.row, player_current.col, player[1])
#     # ws_results.update_cell(row.row, player_new.col, player[0])
#     c.execute(f'UPDATE results SET "{curr_player1}" = "{player_new}" WHERE "Date" = "{next_wednesday}" AND "{curr_player1}" = "{player_current}"')
#     c.execute(f'UPDATE results SET "{curr_player2}" = "{player_new}" WHERE "Date" = "{next_wednesday}" AND "{curr_player2}" = "{player_current}"')
#     c.execute(f'UPDATE results SET "{curr_player3}" = "{player_new}" WHERE "Date" = "{next_wednesday}" AND "{curr_player3}" = "{player_current}"')
#     c.execute(f'UPDATE results SET "{curr_player4}" = "{player_new}" WHERE "Date" = "{next_wednesday}" AND "{curr_player4}" = "{player_current}"')
#     c.execute(f'UPDATE results SET "{curr_player5}" = "{player_new}" WHERE "Date" = "{next_wednesday}" AND "{curr_player5}" = "{player_current}"')
#     c.execute(f'UPDATE results SET "{new_player1}" = "{player_current}" WHERE "Date" = "{next_wednesday}" AND "{new_player1}" = "{player_new}"')
#     c.execute(f'UPDATE results SET "{new_player2}" = "{player_current}" WHERE "Date" = "{next_wednesday}" AND "{new_player2}" = "{player_new}"')
#     c.execute(f'UPDATE results SET "{new_player3}" = "{player_current}" WHERE "Date" = "{next_wednesday}" AND "{new_player3}" = "{player_new}"')
#     c.execute(f'UPDATE results SET "{new_player4}" = "{player_current}" WHERE "Date" = "{next_wednesday}" AND "{new_player4}" = "{player_new}"')
#     c.execute(f'UPDATE results SET "{new_player5}" = "{player_current}" WHERE "Date" = "{next_wednesday}" AND "{new_player5}" = "{player_new}"')
#     print("Swapped player and updated score")
#     return