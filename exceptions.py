from datetime import datetime

class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message

def validate_titles(titles):
    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")


class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message

def validate_year_cup(year_cup):
    cup_years = [1930, 1934, 1938]
    sum = 0
    for i in range(1950, 2100):
        if i%4 == 2:
            cup_years.append(i)
    for i in cup_years:
        if i ==  year_cup:
            sum = sum+1
    if sum == 0:
        raise InvalidYearCupError("there was no world cup this year")


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message

def validate_number_of_titles(number_of_titles):
    today_year = datetime.now().year
    cup_years_till_today = [1930, 1934, 1938]
    for i in range(1950, today_year):
        if i%4 == 2:
            cup_years_till_today.append(i)
    if number_of_titles > len(cup_years_till_today):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")


