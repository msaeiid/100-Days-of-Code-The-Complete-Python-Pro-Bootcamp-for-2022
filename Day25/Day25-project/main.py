# Challenge 1
# with open('./weather_data.csv', mode='r') as file:
#     data = []
#     for line in file.readlines():
#         data.append(line.strip().split(','))
#     print(data)

# open with CSV
# import csv
#
# with open('./weather_data.csv', mode='r') as file:
#     file = list(csv.reader(file))
#     temperatures = [int(row[1]) for row in file[1:]]
#     print(temperatures)


import pandas

data = pandas.read_csv('./weather_data.csv')
# challenge 2
# print(data)
# print(data['temp'].to_list())
# challenge 3 average
# print(sum(data['temp']) / len(data))
# print(data['temp'].mean())
# print(data.temp.max())
# print(data.condition)

# how print row
# print(data[data.day == 'Monday'])
# maximum temperature
# maximum_temperature = data.temp.max()
# print(data[data.temp == data.temp.max()])
# جالبه
# print(data.temp  == data.temp.max())
# particular row
# print(data[data.temp == data.temp.max()].condition)

# Monday temp not in C in F
# temp = int(data[data.day == 'Monday'].temp)
# print(temp * 9 / 5 + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
