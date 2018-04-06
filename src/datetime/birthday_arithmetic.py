
import datetime

class DateInFutureException(Exception):
    pass

def ask_birthday():
    while True:
        user_input = raw_input("Enter a date of birth (yyyy/mm/dd): ")
        try:
            birthday = parse_and_validate_birthday(user_input)
            return birthday
        except ValueError as e:
            print e
        except DateInFutureException as e:
            print ""
            print e
            print ""

def ask_to_continue():
    while True:
        user_answer = (raw_input("Find days remaining to another birthday? (Y/N): ")).lower()
        if user_answer == "y":
            return True
        elif user_answer == "n":
            return False
        else:
            print ""
            print "Sorry, invalid input"
            print ""

def parse_and_validate_birthday(user_input):
    """
    Parses and validates given string for a date and returns a datetime object.
    
    Args:
        user_input (str): The string to parse
    
    Returns:
        birthday: A datetime object for the given date
    
    Raises:
        ValueError: If the date format of the input string is invalid
        DateInFutureException: If the date format is valid but the date is in the future

    Examples:
        A valid input string
        >>> parse_and_validate_birthday('2012/07/23')
        datetime.datetime(2012, 7, 23, 0, 0)

        Invalid input string - letters instead of a date
        >>> parse_and_validate_birthday('abcd')
        Traceback (most recent call last):
        ...
        ValueError: time data 'abcd' does not match format '%Y/%m/%d'

        A valid input string but date in future
        >>> parse_and_validate_birthday('2018/12/23')
        Traceback (most recent call last):
        ...
        DateInFutureException: This birthday is in the future! Enter a valid date of birth.
    """
    birthday = datetime.datetime.strptime(user_input, '%Y/%m/%d')
    
    if birthday > datetime.datetime.today():
        raise DateInFutureException("This birthday is in the future! Enter a valid date of birth.")
    
    return birthday


def days_to_birthday(birthday):
    """
    Returns a tuple of number of days remaining for a given birthday, day of the week, and the age of the person.
    
    Args:
        birthday: A datetime object for the birthday
    
    Returns:
        A tuple of (days, weekday, age)
        days (int): Returns number of days remaining for the next birthday
        weekday (str): Returns the day of the week on which the birthday falls
        age (int): Returns the age of the person with the given birthday

    Note:
        The doctests in the Examples section will fail in future because answers correspond to today's date.

    Examples:
        A birthday in future
        >>> days_to_birthday(datetime.datetime(1978, 7, 21))
        (105, 'Saturday', 40)

        A birthday in the past, same month
        >>> days_to_birthday(datetime.datetime(1975, 4, 1))
        (359, 'Monday', 44)

        A birthday in future, same month
        >>> days_to_birthday(datetime.datetime(1975, 4, 21))
        (14, 'Saturday', 43)

        A birthday in future, another month
        >>> days_to_birthday(datetime.datetime(1978, 1, 21))
        (289, 'Monday', 41)
    """
    # creating a datetime object for today's date
    dt_today = datetime.datetime.today()
    # creating a datetime object for birthday this year
    birthday_this_year = datetime.datetime(dt_today.year, birthday.month, birthday.day)
    # creating a datetime object for birthday next year
    birthday_next_year = birthday.replace(year=dt_today.year + 1)

    # if birthday in future
    if birthday_this_year >= dt_today:
        days_to_birthday = birthday_this_year - dt_today
        user_age = dt_today.year - birthday.year
        day_of_week = birthday_this_year.strftime("%A")
    # if birthday in past
    else:
        days_to_birthday = birthday_next_year - dt_today
        user_age = (dt_today.year + 1) - birthday.year
        day_of_week = birthday_next_year.strftime("%A")

    return (days_to_birthday.days, day_of_week, user_age)

def birthday_on_day_of_week(birthday, year):
    """
    Returns the day of the week a birthday will fall in the given year

    Args:
        birthday: A datetime object for the birthday
        year (int): A year for which day of the week needs to be determined for the birthday
    
    Returns:
        birthday_given_year.strftime("%A") (str): A day of the week

    Examples:
        >>> birthday_on_day_of_week(datetime.datetime(1978, 7, 21), 2020)
        'Tuesday'

        >>> birthday_on_day_of_week(datetime.datetime(1978, 5, 17), 2019)
        'Friday'
    """
    birthday_given_year = datetime.datetime(year, birthday.month, birthday.day)

    return birthday_given_year.strftime("%A")

if __name__ == "__main__":
    while True:
        birthday = ask_birthday()
        (days, weekday, age) = days_to_birthday(birthday)
        if days == 0:
            print ""
            print "The given birthday is today ({})! The person is {} years old today.".format(weekday, age)
            print ""
        else:
            print ""
            print "The given birthday is {} days away and will fall on a {}.".format(days, weekday)
            print "The person will be {} years old.".format(age)
            print "BONUS: The birthday in 2020 will fall on a {}.".format(birthday_on_day_of_week(birthday, 2020))
            print ""
        
        if not ask_to_continue():
            break

    