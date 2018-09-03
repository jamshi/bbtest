# BetBright Take home test
# Candidate Name: Jamsheed BP
"""

This is an alternative implementation of datecalculation function. This
does the same functionality as in datecalculation.py. This implementaion
follows a different algorithm.
"""
import datetime
import cProfile

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

    def _next_dest(dest):
        _nxt = dest - week_day
        _nxt = 7 + _nxt if _nxt <= 0 else _nxt
        return _nxt

    _nxt_wed = _next_dest(WED) #days left for next wed
    _nxt_sat = _next_dest(SAT) #days left for next sat
    # take min of both
    _days_left = min(_nxt_wed, _nxt_sat) 

    _date = curr_date + datetime.timedelta(days=_days_left)
    return _date.replace(hour=20, minute=0, second=0, microsecond=0)


