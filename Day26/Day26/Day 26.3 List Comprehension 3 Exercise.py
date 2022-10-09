with open('./file1.txt') as f1:
    file_1 = f1.readlines()
with open('./file2.txt') as f2:
    file_2 = f2.readlines()

result = [int(number) for number in file_1 if number in file_2]
print(result)
