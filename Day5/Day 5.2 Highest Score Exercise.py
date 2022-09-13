students_height = input("Input a list of student height \n").split()
max_height = int(students_height[0])
min_height = int(students_height[0])
for height in students_height:
    if int(height) > max_height:
        max_height = int(height)
    if int(height) < min_height:
        min_height = int(height)
print(
    f"The highest score in the class is: {max_height}\nThe lowest score in the class is: {min_height}")
