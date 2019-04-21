# Christopher H. Todd's Python Library For Interacting With Datetime Objects in Python

The ctodd-python-lib-datetime project is responsible for interacting with date, time, timezones, and other time related shenanigans in the Python languages.

## Table of Contents

- [Dependencies](#dependencies)
- [Libraries](#libraries)
- [Example Scripts](#example-scripts)
- [Notes](#notes)
- [TODO](#todo)

## Dependencies

### Python Packages

-

## Libraries

### [date_manipulation_helpers.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-datetime/blob/master/datetime_helpers/date_manipulation_helpers.py)

Library for Manipulating Datetime and Date objects in Python

Functions:

```
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
```

## Example Scripts

Example executable Python scripts/modules for testing and interacting with the library. These show example use-cases for the libraries and can be used as templates for developing with the libraries or to use as one-off development efforts.

### N/A
## Notes

 - Relies on f-string notation, which is limited to Python3.6.  A refactor to remove these could allow for development with Python3.0.x through 3.5.x

## TODO

 - Unittest framework in place, but lacking tests
