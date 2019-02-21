#!/usr/bin/env python3
"""
    Library for Manipulating Datetime and Date objects
    in Python
"""

# Python Library Imports
from datetime import datetime, date, timedelta
import operator


def add_or_subtract_days_from_date(base_date, number_of_days, op='addition'):
    """
    Purpose:
        Adds or subtracts a number of days to a given date
        Useful for data sources that use different date structures
        Default operator is addition
    Args:
        base_date (str, datetime obj): Date to mutate
        number_of_days (int): Number of days to add or subtract
        op (str): operator to overload. 'addition' or 'subtraction'
    Returns:
        new_date (Date): Updated date based on function
    """

    operators = {
        'addition': operator.add,
        'subtraction': operator.sub,
    }
    date_function = operators[op]

    if not isinstance(base_date, datetime) and not\
        isinstance(base_date, date):
        base_date = datetime.strptime(base_date, '%Y-%m-%d')

    return date_function(base_date, timedelta(days=number_of_days))
