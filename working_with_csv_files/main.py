# import csv
# import pandas

# with open("/home/nirav/OneDrive/CS/Python/100DaysOfPython/working_with_csv_files/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperature.append(temp)
#     print(temperature)

import pandas as pd

data = pd.read_csv('working_with_csv_files/Sep_Expense_Summary.csv')
# print(data['AMOUNT'].mean())
# print(data.DATE)
# print(data[data.DATE == '23/Sep'])
print(data[data.AMOUNT == data.AMOUNT.min()])

# data_dict = data.to_dict()
# print(data_dict)
#data_series = data['temp'].to_list()
#average = sum(data_series)/len(data_series)
#print(average)

#Alternatively average can also be found using mean method from pandas library
# average = data['temp'].mean()
# print(average)

#maximum = data['temp'].max()
#print(maximum)

#Creating a dataframe from scratch
data_dict = {
    'Students': ['Nirav', 'Vatsal', 'Nikunj', 'Mansi'],
    'Scores': [86, 88, 92, 95],
    'Gender': ["Male", "Male", "Male", "Female"]

}

data1 = pd.DataFrame(data_dict)
print(data1)
data1.to_csv('new_data.csv')