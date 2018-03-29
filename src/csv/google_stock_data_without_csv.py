"""using the open(), read() and close() functions"""
# file1 = open("google_stock_data.csv")
# text1 = file1.read()
# file1.close()
# print text1

"""using the try/except and with statements"""
# try:
#     with open("google_stock_data.csv") as file2:
#         text2 = file2.read()
# except IOError:
#         text2 = None
# print text2

"""reading lines without using the csv module"""
with open("google_stock_data.csv") as file3:
    # text3 = [line for line in file3]
    # print text3[0]
    # print text3[1]
    # print text3[0].rstrip().split(",")
    # print text3[1].rstrip().split(",")
    dataset = [line.rstrip().split(",") for line in file3]
    print dataset[1]