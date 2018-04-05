Learning how to use the modules from the Python standard library

1. csv<br>
Problem: Analyze the first ten years of stock data for Google (https://www.youtube.com/watch?v=Xi52tx6phRU)
    - Two .csv files, one with input data (google_stock_data.csv) and the other with output (google_returns.csv)
    - google_stock_date_without_csv.py:
        - with and try/except statements
        - open(), read() and close() functions
    - google_stock_date_with_csv.py:
        - csv.reader, csv.writer, writerow(), next()
        - datetime.strptime, strftime

2. datetime<br>
Problem: Find days remaining to the birthday and age of the person
    - Documented function behavior using Sphinx's Napoleon extension (https://sphinxcontrib-napoleon.readthedocs.io/en/latest/) based on the Google Style
    - Restructured code under the main body of the file
    - try/except/raise statements
    - datetime.datetime.today(), datetime.datetime.strptime
