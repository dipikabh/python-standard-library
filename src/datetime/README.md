# Solving Problems Related to the `datetime` Module

### A sample run of the program to show its behaviour

```console
$ python src/datetime/birthday_arithmetic.py
Enter a date of birth (yyyy/mm/dd): 1980/10/10

The given birthday is 186 days away and will fall on a Wednesday.
The person will be 38 years old.
BONUS: The birthday in 2020 will fall on a Saturday.

Find days remaining to another birthday? (Y/N): j

Sorry, invalid input

Find days remaining to another birthday? (Y/N): y
Enter a date of birth (yyyy/mm/dd): 2020/10/10

This birthday is in the future! Enter a valid date of birth.

Enter a date of birth (yyyy/mm/dd): 2017/2/2

The given birthday is 301 days away and will fall on a Saturday.
The person will be 2 years old.
BONUS: The birthday in 2020 will fall on a Sunday.

Find days remaining to another birthday? (Y/N): n
$
```

## Changelog

- 2018-04-05 21:43: Used datetime.replace() to create a datetime object instead of using timedelta.
- 2018-04-05 21:38: Moved the user prompts to their own functions. Added readme and changelog.