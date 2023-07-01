import pandas
squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(squirrel_data)
#
# color = squirrel_data['Primary Fur Color']
# # color = squirrel_data['Primary Fur Color'].count()
# print(squirrel_data['Primary Fur Color'] != 'cinnamon')
# print(color)

gray_squirrel = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])
print(gray_squirrel)
print(cinnamon_squirrel)
print(black_squirrel)

squirrel_dict = {
    'color': ['Gray', 'Cinnamon', 'Black'],
    'count': [gray_squirrel, cinnamon_squirrel, black_squirrel]
}
print(squirrel_dict)
color_data = pandas.DataFrame(squirrel_dict)
print(color_data)

color_data.to_csv("color_data.csv")

