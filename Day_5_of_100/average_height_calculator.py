# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
student = 0
for height in student_heights:
    student += height
    #print(student)

counter = 0
for height in student_heights:
    counter += 1
    #print(counter)
print({round(student / counter)})





