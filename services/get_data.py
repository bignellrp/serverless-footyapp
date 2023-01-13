import pandas as pd
from dynamo_pandas import get_df

class player():
	
    def __init__(self):
        '''Initialise the class and get all the 
        values from the players table'''
        self.df = get_df(table="player_table")
        self.df = self.df.sort_values(by=['Name'],ascending=True)

    def player_names(self):
        '''Filter Names and convert to list'''
        self.player_names = self.df.filter(['Name','Playing'])
        ##Convert from df to list without index to be used in forms
        self.player_names = self.player_names.to_records(index=False)
        self.player_names = list(self.player_names)
        return self.player_names
		
    def all_players(self):
        '''Filter All Players'''
        self.all_players = self.df.filter(['Name','Total'])
        ##Convert Total column to numeric so they can be added up
        self.all_players['Total'] = pd.to_numeric(self.all_players['Total'])
        ##Convert from df to list without index to be used in forms
        self.all_players = self.all_players.to_records(index=False)
        self.all_players = list(self.all_players)
        return self.all_players

    def player_stats(self):
        '''Filter Player Stats'''
        self.player_stats = self.df.filter(
                ['Name','Wins','Draws','Losses','Score','Win Percentage'])
        ##Convert multiple columns to numeric
        self.player_stats[['Wins','Draws',
                           'Losses','Score',
                           'Win Percentage']] = self.player_stats[['Wins',
                           'Draws','Losses','Score',
                           'Win Percentage']].apply(pd.to_numeric)
        ##Sort by Score
        self.player_stats = self.player_stats.sort_values(by=['Score'],
                                                          ascending=False)
        ##Convert from df to list without index to be used in forms
        self.player_stats = self.player_stats.to_records(index=False)
        self.player_stats = list(self.player_stats)
        return self.player_stats

    def leaderboard(self):
        '''Filter Game Stats for Leaderboard'''
        self.leaderboard = self.df.filter(['Name','Score'])
        ##Convert Score column to numeric so they can be added up
        self.leaderboard['Score'] = pd.to_numeric(self.leaderboard['Score'])
        self.leaderboard = self.leaderboard.sort_values(by=['Score'],
                                                        ascending=False)
        ##Head the top10
        self.leaderboard = self.leaderboard.head(10)
        ##Convert from df to list without index to be used in forms
        self.leaderboard = self.leaderboard.to_records(index=False)
        self.leaderboard = list(self.leaderboard)
        return self.leaderboard

    def winpercentage(self):
        '''Filter Game Stats for winpercentage'''
        self.winpercentage = self.df.filter(['Name','Win Percentage'])
        ##Convert Score column to numeric so they can be added up
        self.winpercentage['Win Percentage'] = pd.to_numeric(
                self.winpercentage['Win Percentage'])
        self.winpercentage = self.winpercentage.sort_values(
                by=['Win Percentage'],ascending=False)
        ##Head the top10
        self.winpercentage = self.winpercentage.head(10)
        ##Convert from df to list without index to be used in forms
        self.winpercentage = self.winpercentage.to_records(index=False)
        self.winpercentage = list(self.winpercentage)
        return self.winpercentage

    def player_count(self):
        '''Count the number of players in tally'''
        game_tally = []
        game_player_tally = []
        player_names = self.df.filter(['Name','Playing'])
        ##Convert from df to list without index to be used in forms
        player_names = player_names.to_records(index=False)
        player_names = list(player_names)
        for row in player_names:
            '''Takes in row of player_names
            and outputs a just the tally column'''
            game_player_tally.append((row[0]))
            game_tally.append((row[1]))
        self.player_count = 10 - game_tally.count("x")
        return self.player_count
    
    def game_player_tally(self):
        '''List of player names playing'''
        game_player_tally = []
        player_names = self.df.filter(['Name','Playing'])
        ##Convert from df to list without index to be used in forms
        player_names = player_names.to_records(index=False)
        player_names = list(player_names)
        for row in player_names:
            '''Takes in row of player names 
            and returns a tally of those players
            that are available this week'''
            if row[1] == "x":
                game_player_tally.append((row[0]))
        self.game_player_tally = game_player_tally
        return self.game_player_tally
    
    def game_player_tally_with_index(self):
        '''List of player names playing
        with index'''
        game_player_tally = []
        player_names = self.df.filter(['Name','Playing'])
        ##Convert from df to list without index to be used in forms
        player_names = player_names.to_records(index=False)
        player_names = list(player_names)
        for row in player_names:
            '''Takes in row of player names 
            and returns a tally of those players
            that are available this week'''
            if row[1] == "x":
                game_player_tally.append((row[0]))
        self.game_player_tally_with_index = enumerate(game_player_tally, 
                                                      start=1)
        return self.game_player_tally_with_index

    def game_player_tally_with_score(self):
        '''List of player names playing
        with score'''
        game_player_tally = []
        player_names = self.df.filter(['Name','Total','Playing'])
        ##Convert from df to list without index to be used in forms
        player_names = player_names.to_records(index=False)
        player_names = list(player_names)
        for row in player_names:
            '''Takes in row of player names 
            and returns a tally of those players
            that are available this week'''
            if row[2] == "x":
                game_player_tally.append((row[0] , int(row[1])))
        self.game_player_tally_with_score = game_player_tally
        return self.game_player_tally_with_score

    def game_player_tally_with_score_and_index(self):
        '''List of player names playing'''
        game_player_tally = []
        player_names = self.df.filter(['Name','Total','Playing'])
        ##Convert from df to list without index to be used in forms
        player_names = player_names.to_records(index=False)
        player_names = list(player_names)
        num=1
        for row in player_names:
            '''Takes in row of player names 
            and returns a tally of those players
            that are available this week'''
            if row[2] == "x":
                game_player_tally.append((num, row[0] , int(row[1])))
                num=num+1
        self.game_player_tally_with_score_and_index = game_player_tally
        return self.game_player_tally_with_score_and_index

class results():

    def __init__(self):
        '''Initialise the class and get 
        all the values from the results table'''
        self.df = get_df(table="results_table")
        ##Filter the data into a certain order to use iloc later
        self.df = self.df.filter(['Date',
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
        self.df['Date'] = pd.to_datetime(self.df.Date, format='%Y%m%d', errors='ignore')
        self.df = self.df.sort_values(by=['Date'], ascending=True)

    def all_results(self):
        '''Get all results including column names'''
        self.all_results = self.df
        return self.all_results

    def game_stats(self):
        '''Get all stats for stats page'''
        ##Filter All Players
        self.game_stats = self.df.filter(['Date','Team A Result?',
                                          'Team B Result?'])
        ##Take only the last 10 games
        self.game_stats = self.game_stats.tail(10)
        ##Sort by date
        self.game_stats = self.game_stats.sort_values(by=['Date'],
                                                      ascending=False)
        ##Convert from df to list without index to be used in forms
        self.game_stats = self.game_stats.to_records(index=False)
        self.game_stats = list(self.game_stats)
        return self.game_stats
    
    def teama(self):
        '''Use iloc to get last row and 
        columns for teama,
        teamb,scorea,scoreb and date
        iloc takes the row as the first 
        value and column's' 
        as the second value'''
        self.teama = self.df.iloc[-1,5:10]
        self.teama = list(self.teama)
        return self.teama

    def teamb(self):
        '''Use iloc to get last row and columns for teama,
        teamb,scorea,scoreb and date
        iloc takes the row as the first value and 
        column's' as the second value'''
        self.teamb = self.df.iloc[-1,10:15]
        self.teamb = list(self.teamb)
        return self.teamb

    def scorea(self):
        '''Use iloc to get last row and columns for 
        teama,teamb,scorea,scoreb and date
        iloc takes the row as the first value
        and column's' as the second value'''
        self.scorea = self.df.iloc[-1,1]
        return self.scorea
    
    def scoreb(self):
        '''Use iloc to get last row and columns for 
        teama,teamb,scorea,scoreb and date
        iloc takes the row as the first value 
        and column's' as the second value'''
        self.scoreb = self.df.iloc[-1,2]
        return self.scoreb

    def date(self):
        '''Use iloc to get last row and columns for 
        teama,teamb,scorea,scoreb and date
        iloc takes the row as the first value 
        and column's' as the second value'''
        self.date = self.df.iloc[-1,0]
        return self.date

    def totala(self):
        '''Use iloc to get last row and columns for 
        teama,teamb,scorea,scoreb and date
        iloc takes the row as the first value 
        and column's' as the second value'''
        self.totala = self.df.iloc[-1,3]
        return self.totala
    
    def totalb(self):
        '''Use iloc to get last row and columns for 
        teama,teamb,scorea,scoreb and date
        iloc takes the row as the first value 
        and column's' as the second value'''
        self.totalb = self.df.iloc[-1,4]
        return self.totalb

    def coloura(self):
        '''Use iloc to get last row and columns for 
        teama,teamb,scorea,scoreb and date
        iloc takes the row as the first value 
        and column's' as the second value'''
        self.coloura = self.df.iloc[-1,15]
        return self.coloura
    
    def colourb(self):
        '''Use iloc to get last row and columns for 
        teama,teamb,scorea,scoreb and date
        iloc takes the row as the first value 
        and column's' as the second value'''
        self.colourb = self.df.iloc[-1,16]
        return self.colourb