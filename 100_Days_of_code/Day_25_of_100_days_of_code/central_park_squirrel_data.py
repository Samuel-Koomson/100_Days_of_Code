import pandas
squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(squirrel_data)
# color = squirrel_data['Primary Fur Color']
color = squirrel_data['Primary Fur Color'].count()
print(squirrel_data['Primary Fur Color'] != 'cinnamon')
# print(color)