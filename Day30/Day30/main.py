# ## Sample error
# try:
#     file = open('./file.text')
#     print('FileFoundError')
#
#     # a_dictionary = {"key": "value"}
#     # print(a_dictionary['test'])
# except FileNotFoundError:
#     file = open('./file.text', 'w')
#     file.write('File data...[]')
#     print('FileNotFoundError')
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     print(file.read())
# finally:
#     file.close()
#     print("File was closed.")
#     raise KeyError('This is an error that I made up.')

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
print(f"your bmi : {weight / height ** 2}")
