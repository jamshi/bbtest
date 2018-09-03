# BetBright Take home test
# Candidate Name: Jamsheed BP
"""
The Irish lottery draw takes place twice weekly on a
Wednesday and a Saturday at 8pm. Write a function that calculates
and returns the next valid draw
date based on an optional supplied date time parameter.
If no supplied date is provided, assume current date time
"""
import datetime

WED = 2
SAT = 5

def next_draw_date(curr_date=datetime.datetime.now()):
    """ Calculates the next irish lottery draw date based on the input.
    Args:
        curr_date: Datetime object of which nearest draw date has to be calculated.
                   default is current datetime
    Returns:
        datetime.datetime: the nearest calculated draw date.
    """
    week_day = curr_date.weekday()
    # Check if draw date is on same day and not lapsed(ie 8pm)
    if week_day in [WED, SAT] and curr_date.hour < 20:
        return curr_date.replace(hour=20, minute=0, second=0, microsecond=0)

    _date = curr_date + datetime.timedelta(days=1)
    while _date.weekday() not in (WED, SAT):
        _date = _date + datetime.timedelta(days=1)
    return _date.replace(hour=20, minute=0, second=0, microsecond=0)
