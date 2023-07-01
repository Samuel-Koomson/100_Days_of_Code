#opening and reading data files in python

with open ('weather_data.csv') as data:
    content = data.readlines()
    # print(content)

#opening and reading data files using the csv library in python
import csv

with open("weather_data.csv") as data:
    content = csv.reader(data)
    temperatures = []
    for row in content:
        print(row)
        if row[1] != 'temp':
            temperatures.append(float(row[1]))
    print(temperatures)


    # for row in content:
    #     print(row)
#opening and reading data files using the pandas library in python

import pandas

# #pandas picks the first row of a data as the headings
# data = pandas.read_csv('weather_data.csv')
# # print(data)
# # print(type(data))
# # print(type(data['temp']))
# #
# # #pandas can convert data to different forms
# # data_conversion = data.to_dict()
# # print(data_conversion)
# #
# # average_list = data['temp'].to_list()
# # print(average_list)
# #
# # #pandas also has inbuilt statistical methods which makes it easy to work with stats
# #
# # average = data['temp'].mean()
# #
# # average = data['temp'].max()
# # print(average)
#
# #How to get data from rows
# day = [data.temp == data.temp.max()]
# print(day)
#
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# fahr = monday_temp * 9/5 + 32
# print(fahr)

p_dict ={
    'employee': ['Wisdom', 'Jude', 'Lemuel', 'Barbara', 'Sybil', 'Rosa'],
    'salary': [5000, 6000, 4500, 5000, 4590, 5500],
    'Jobrole': ['sales', 'brands', 'sales', 'claims', 'underwriting', 'PR']
}
pydata = pandas.DataFrame(p_dict)
print(pydata)
