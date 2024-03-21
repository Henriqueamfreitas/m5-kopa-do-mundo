from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime

def data_processing(dict):
    team_titles = dict['titles']
    if team_titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

    team_first_cup_string = dict['first_cup']
    team_first_cup_date = datetime.strptime(team_first_cup_string, "%Y-%m-%d")
    team_first_cup_year = team_first_cup_date.year
    cup_years = [1930, 1934, 1938]
    sum = 0
    for i in range(1950, 2100):
        if i%4 == 2:
            cup_years.append(i)
    for i in cup_years:
        if i ==  team_first_cup_year:
            sum = sum+1
    if sum == 0:
        raise InvalidYearCupError("there was no world cup this year")

    today_year = datetime.now().year
    cup_years_till_today = [1930, 1934, 1938]
    for i in range(1950, today_year+1):
        if i%4 == 2:
            cup_years_till_today.append(i)
    team_limit_word_cups = []
    for i in cup_years_till_today:
        if i>=team_first_cup_year:
            team_limit_word_cups.append(i)
    if team_titles > len(team_limit_word_cups):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

