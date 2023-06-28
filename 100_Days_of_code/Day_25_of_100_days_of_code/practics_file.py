# with open ('weather_data.csv') as data:
#     content = data.readlines()
#     print(content)

import csv

with open("weather_data.csv") as data:
    content = csv.reader(data)
    temperatures = []
    for row in content:
        if row[1] != 'temp':
            temperatures.append(float(row[1]))
    print(temperatures)

    # for row in content:
    #     print(row)

import pandas
data = pandas.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])

# data_conversion = data.to_dict()
# print(data_conversion)

# average = data['temp'].mean()

average = data['temp'].max()
day = [data.day == max('temp')]
print(day)
print(average)