import random

## List Comprehension
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     new_list.append(n + 1)
# print(new_list)

## Challenge1
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

# name = "Angela"
# new_list = [letter for letter in name]

## Challenge2
# numbers = [number * 2 for number in range(1, 5)]

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) < 5]

## Challenge3
# long_names = [name.upper() for name in names if len(name) > 5]

## Dictionary comprehension
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
## Challenge4
# passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

## Looping through dictionaries:
# for (key, value) in dictionary.items():
#     print(value)

##Iterate over a pandas Dataframe
import pandas

student_dict = {"student": ["angela", "James", "Lily"],
                "score": [56, 76, 98]}
data = pandas.DataFrame(student_dict)
# print(data)
## Loop through a data frame
# for (key, value) in data.items():
#     print(value)

##Loop through rows of a data frame
for (index, row) in data.iterrows():
    if row.student == 'angela':
        print(row.score)
