student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}
# student_grades["Harry"] = "Exceeds Expectation"
# student_grades["Ron"] = "Acceptable"
# student_grades["Hermione"] = "Outstanding"
# student_grades["Draco"] = "Acceptable"
# student_grades["Neville"] = "Fail"
# print(student_grades)

#TODO-2: Write your code below to add the grades to student_grades.👇

for grade in student_scores:
    if student_scores[grade] in range (91, 100):
        student_grades[grade] = "Outstanding" 
        # print(grade)
    if student_scores[grade] in range (81, 90):
        student_grades[grade] = "Exceeds Expectations" 
    if student_scores[grade] in range (71, 80):
        student_grades[grade] = "Acceptable" 
    if student_scores[grade] in range (0, 70):
        student_grades[grade] = "Fail" 
print(student_grades)

# 🚨 Don't change the code below 👇
# print(student_grades)
