# Challenge1
# with open(b"C:\Users\Saeed\Desktop\my_file.txt", mode='a') as file:
#     file.write('\n new line')
# Challenge2 Absolute file path
# with open(b"C:\Users\Saeed\Desktop\my_file.txt") as file:
#     content = file.read()
#     print(content)
# Challenge3 Relative file path
with open("../../../my_file.txt") as file:
    content = file.read()
    print(content)
