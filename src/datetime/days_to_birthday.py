
import datetime

class DateInFutureException(Exception):
    pass

def parse_and_validate(user_input):
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
        >>> parse_and_validate('2012/07/23')
        datetime.datetime(2012, 7, 23, 0, 0)

        Invalid input string - letters instead of a date
        >>> parse_and_validate('abcd')
        Traceback (most recent call last):
        ...
        ValueError: time data 'abcd' does not match format '%Y/%m/%d'

        A valid input string but date in future
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
    Returns number of days to a given birthday and the age of the person.
    
    Args:
        birthday: A datetime object for the birthday
    
    Returns:
        A tuple of (days, age)
        days_to_birthday.days: Returns number of days remaining for the next birthday
        user_age: Returns the age of the person with the given birthday

    Note:
        The doctests in the Examples section will fail in future because answers correspond to today's date.

    Examples:
        A birthday in future
        >>> days_to_birthday(datetime.datetime(1978, 7, 21))
        (106, 40)

        A birthday in the past, same month
        >>> days_to_birthday(datetime.datetime(1975, 4, 1))
        (360, 44)

        A birthday in future, same month
        >>> days_to_birthday(datetime.datetime(1975, 4, 21))
        (15, 43)

        A birthday in future, another month
        >>> days_to_birthday(datetime.datetime(1978, 1, 21))
        (290, 41)
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
        user_answer = raw_input("Find days remaining to birthday and age? (Y/N): ")
        if user_answer.lower() == "y":
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
                print "The given birthday is today! The person is {} years old today.".format(age)
            else:
                print "The given birthday is {} days away. The person will be {} years old on his/her next birthday.".format(days, age)
        elif user_answer == "n":
            break
        else:
            print "Sorry, invalid input"

    