
#170041_Nikhil


import pandas as pd
import matplotlib.pyplot as plt



Bakery_data_set = pd.read_csv("E:/BreadBasket_DMS.csv")
Bakery_data_set.dropna()
Bakery_data_set = Bakery_data_set[Bakery_data_set['Item'] != 'NONE']

Bakery_data_set['Date'] = pd.to_datetime(Bakery_data_set['Date'])
Bakery_data_set['Time'] = pd.to_datetime(Bakery_data_set['Time'])
Bakery_data_set['Year'] = Bakery_data_set['Date'].dt.year
Bakery_data_set['Month'] = Bakery_data_set['Date'].dt.month
Bakery_data_set['Day'] = Bakery_data_set['Date'].dt.day
Bakery_data_set['Weekday'] = Bakery_data_set['Date'].dt.weekday
Bakery_data_set['Hour'] = Bakery_data_set['Time'].dt.hour

def map_indexes_and_values(df, col):
    df_col = df[col].value_counts()
    x = df_col.index.tolist()
    y = df_col.values.tolist()
    return x, y



print("Question 6")
Bakery_data_set.groupby('Weekday')['Transaction'].nunique().plot(kind='bar', title='Number of items sold per weekday.')
plt.xlabel('Days')
plt.ylabel('Number of Transactions')
plt.show()