"""First option for opening a file is the manual option where you are
required to close your file after use. below is the syntax and methods for executing this task"""
file = open('my_textfile.txt')
file_content = file.read()
print(file_content)
file.close()

""""The second method is the auto open and close method where the file gets closed automatically after use"""
with open('my_textfile.txt') as file1:
    file_content = file1.read()
    # print(file_content)

#writing to a file
"""We can also write into our file using different methods"""

with open('my_textfile.txt', 'w') as file1:
    file1.write('This is an update using the write option')
    print(file1)
#using the write parameter replaces the content of your file with the new text

# with open('my_textfile.txt', 'a') as file1:
#     file1.write('This is option allows for the addition of new text in the document to be appended')
#     # print(file_content)