# `datetime` related problems

## A sample run

```console
$ python src/datetime/birthday_arithmetic.py
Enter a date of birth (yyyy/mm/dd): 1978/7/21

The given birthday is 106 days away and will fall on Saturday.
The person will be 40 years old.
BONUS: The birthday in 2020 will fall on a Tuesday.

Find days remaining to a birthday? (Y/N): l
Sorry, invalid input
Find days remaining to a birthday? (Y/N): y
Enter a date of birth (yyyy/mm/dd): 2190/2/3
This birthday is in the future! Enter a valid date of birth.
Enter a date of birth (yyyy/mm/dd): 2017/2/3

The given birthday is 303 days away and will fall on Sunday.
The person will be 2 years old.
BONUS: The birthday in 2020 will fall on a Monday.

Find days remaining to a birthday? (Y/N): n
$
```

## Changelog

- 2018-04-05 21:43: Used datetime.replace() to create similar datetime objects
- 2018-04-05 21:38: Moved the user prompts to their own functions. Added readme and changelog.