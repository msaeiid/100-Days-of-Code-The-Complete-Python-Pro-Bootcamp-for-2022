students_height = input("Input a list of student height \n").split()
sum = 0
count=0
for student in students_height:
    sum += int(student)
    count+=1
average = int(sum/count)
print(sum)
print(count)
print(average)
