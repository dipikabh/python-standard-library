
import datetime
import sys

class DateInFutureException(Exception):
    pass

def parse_and_validate(user_input):
    """
    Parse given string for a date, validate that the date is not in future,
    and return a datetime object

    :param user_input string: The string to parse
    :returns: datetime object for the given date
    :raises: ValueError If the format is invalid
    :raises: DateInFutureException If date is in the future

    >>> parse_and_validate('2012/07/23')
    datetime.datetime(2012, 7, 23, 0, 0)

    >>> parse_and_validate('abcd')
    Traceback (most recent call last):
    ...
    ValueError: time data 'abcd' does not match format '%Y/%m/%d'

    >>> parse_and_validate('2018/12/23')
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
    >>> days_to_birthday(datetime.datetime(1978, 7, 21))
    (106, 40)

    # earlier than current month
    >>> days_to_birthday(datetime.datetime(1978, 1, 21))
    (290, 41)

    # current month, earlier date
    >>> days_to_birthday(datetime.datetime(1975, 4, 1))
    (360, 44)

    # current month, later date
    >>> days_to_birthday(datetime.datetime(1975, 4, 21))
    (15, 43)
    """

    dt_today = datetime.datetime.today()
    birthday_this_year = datetime.datetime(dt_today.year, birthday.month, birthday.day)
    birthday_next_year = datetime.datetime((dt_today.year + 1), birthday.month, birthday.day)

    # birthday this year, yet to come
    if birthday_this_year >= dt_today:
        days_to_birthday = birthday_this_year - dt_today
        user_age = dt_today.year - birthday.year
    # birthday this year, already passed
    else:
        days_to_birthday = birthday_next_year - dt_today
        user_age = (dt_today.year + 1) - birthday.year

    return (days_to_birthday.days, user_age)


if __name__ == "__main__":

    while True:
        user_input = raw_input("What is your date of birth (yyyy/mm/dd): ")
        try:
            birthday = parse_and_validate(user_input)
            break
        except ValueError as e:
            print e
        except DateInFutureException as e:
            print e
            
    
    (days, age) = days_to_birthday(birthday)
    if days == 0:
        print "Your birthday is today! You are {} years old today.".format(age)
    else:
        print "Your birthday is {} days away. You will be {} years old on your next birthday.".format(days, age)

    