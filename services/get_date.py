import datetime
from datetime import date

def next_weekday(d, weekday):
    '''Takes in todays date and weekday 
    returns the required day in isoformat'''
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)
    
d = date.today()
##Games are played on wednesday 
##so returns next wednesday's date
next_wednesday = next_weekday(d, 2).isoformat()

def find_closest_wednesday(date):
    WEDNESDAY = 3
    year, week, day = date.isocalendar()
    delta = datetime.timedelta(days=WEDNESDAY-day)
    return date + delta
today = datetime.date.today()
closest_wednesday = find_closest_wednesday(today)