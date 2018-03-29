import csv
from datetime import datetime

# print dir(csv)

with open("google_stock_data.csv") as stock_file:
    read = csv.reader(stock_file)
    skip_header = next(read)
    # dataset = [row for row in read]
    # print dataset[0]
    # print dataset[1]
    
    dataset = []
    for row in read:
        date = datetime.strptime(row[0], '%m/%d/%Y')
        open_price = float(row[1])
        high = float(row[2])
        low = float(row[3])
        close_price = float(row[4])
        volume = int(row[5])
        adjusted_close = float(row[6])
        dataset.append([date, open_price, high, low, close_price, volume, adjusted_close])

    # print dataset[0]
    # print dataset[1]

    """calculate daily stock returns and
       write them to a separate file
       
        daily_return = todays_price - yesterdays_price / yesterdays_price   
    """
with open("google_returns.csv", "w") as returns:
    write = csv.writer(returns)

    # write the header
    write.writerow(["Date", "Return"])

    # loop through the dataset using the index
    for i in range(len(dataset) - 1):
        todays_row = dataset[i]
        todays_date = todays_row[0]
        todays_price = todays_row[-1]
        yesterdays_row = dataset[i+1]
        yesterdays_price = yesterdays_row[-1]

        daily_return = (todays_price - yesterdays_price) / yesterdays_price

        # format the date
        formatted_date = todays_date.strftime('%m/%d/%Y')

        # write to the google_returns.csv file
        write.writerow([formatted_date, daily_return])


    