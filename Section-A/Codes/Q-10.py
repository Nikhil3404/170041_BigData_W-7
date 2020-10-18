
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
weekmap = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
print('')

# count of the five most popular items
popular_items, popular_items_count = map_indexes_and_values(Bakery_data_set, 'Item')
plt.bar(popular_items[:10], popular_items_count[:10])

def coffee_ext(group):
    match = group['Item'].str.contains('Coffee')
    return Bakery_data_set.loc[match]

coffee_item = Bakery_data_set[ Bakery_data_set['Item'].str.contains('Coffee')]['Transaction'].unique()


#
coffee_item = pd.DataFrame(coffee_item,columns=['Transaction'])
coffee_m=coffee_item.merge(Bakery_data_set, left_on='Transaction',right_on='Transaction',how='right')

coffee_m = coffee_m[~coffee_m.Item.str.contains('Coffee')]['Item'].value_counts()


print("Question 10")
second_item = Bakery_data_set[Bakery_data_set['Item'] == popular_items[1]]
weekday, weekday_count = map_indexes_and_values(second_item, 'Weekday')
x2 = [weekmap[x] for x in weekday]
wkmp = {}
for j,x in enumerate(x2):
    wkmp[x] = weekday_count[j]
ordervals = [wkmp[val] for val in order]
plt.bar(order, ordervals, color='gold')
plt.xlabel('Weekday')
plt.ylabel('Number of Transactions')
plt.title('Popularity of '+popular_items[1]+' by weekday')
plt.show()

yearsetup=Bakery_data_set.loc[Bakery_data_set['year']==2017]

coffee=yearsetup.set_index(['Item'])
onlycoffee=coffee.loc['Coffee']
onlycoffee.reset_index(inplace=True)

popular=onlycoffee['Date'].value_counts()
print(popular.head())
popular.head().plot(kind='line', color='red', marker='*')
plt.xlabel('Day/Date')
plt.ylabel('Number of Transactions')
plt.title('Top 5 Coffee Sales day in 2017')
plt.show()