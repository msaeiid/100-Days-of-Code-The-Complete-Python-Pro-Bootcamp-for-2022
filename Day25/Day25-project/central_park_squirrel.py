import pandas

data = pandas.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
red = data[data['Primary Fur Color'] == 'Cinnamon']['Primary Fur Color'].count()
grey = data[data['Primary Fur Color'] == 'Gray']['Primary Fur Color'].count()
black = data[data['Primary Fur Color'] == 'Black']['Primary Fur Color'].count()
new_data = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [grey, red, black]
}
new_data_frame = pandas.DataFrame(new_data)
new_data_frame.to_csv('squirrel_count.csv')
