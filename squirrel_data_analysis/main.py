import pandas as pd

data = pd.read_csv('squirrel_data_analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_count = data['Primary Fur Color'].value_counts()['Gray']
black_count = data['Primary Fur Color'].value_counts()['Black']
cinnamon_count = data['Primary Fur Color'].value_counts()['Cinnamon']

count_data = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [gray_count, cinnamon_count, black_count]
}

count_data_df = pd.DataFrame(count_data)
count_data_df.to_csv('squirrel_data_analysis/Squirrel_furcolor.csv')
print(count_data_df)