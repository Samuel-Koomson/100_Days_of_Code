"""Using a non existent file in the file path"""

# file1 = open('a_new_file.txt'):
#the above code throws an error because the txt file does not exist

# try:
#     file1 = open('a_new_file.txt')
#     dict_a ={'key': 'error'}
#     print(dict_a['keying'])
# except FileNotFoundError:
#     print('file did not exist a new file has been created')
#     file1 = open('a_new_file.txt', 'w')
# except KeyError:
#     print('No such key in dictionary')
# else:
#     content = file1.read()
#     print(content)
# finally:
#     file1.close()
#     print("File closed we are good to go")

"""Generating custom made exceptions"""

height = float(input("Height: "))
weight = int(input("Weight"))

bmi = weight / (height * height)
print(bmi)

if height > 3:
    raise ValueError
    print("height cannot be more than 3")
