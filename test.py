import pandas as pd
import numpy as np
import time as time
from pandas.tseries.offsets import Day,Hour
from pandas import DataFrame,Series

def list2csv(li,filename):
    li1=[]
    li2=[]
    for item in li:
        li1.append(item[0])
        li2.append(item[1])
    df=pd.DataFrame({'user_id':li1, 'item_id':li2})
    df.to_csv(filename,index=False)

date_begin = pd.to_datetime('2014-12-19 00')
item_path = 'tianchi_mobile_recommend_train_item.csv'
user_path    = 'tianchi_mobile_recommend_train_user.csv'

# item_after = 'item.csv
user_after = 'user.csv'
car_data_path = 'car.csv'
buy_data_path = 'buy.csv'
#read data
# item_data = pd.read_csv(item_path)
user_data = pd.read_csv(user_path,sep=',')
user_data.time = pd.to_datetime(user_data.time);
user_data = user_data[user_data.time > date_begin - 7*Day()]

car_data = user_data[user_data.behavior_type == 3]
buy_data = user_data[user_data.behavior_type == 4]

# car_data = car_data.set_index(['user_id','item_id'])
# buy_data = buy_data.set_index(['user_id','item_id'])

# car_data = car_data.drop_duplicates(cols=['item_id','user_id'])
# buy_data = buy_data.drop_duplicates(cols=['item_id','user_id'])


# get the 
temp = pd.merge(car_data, buy_data, how='inner')
print np.shape(buy_data)
print np.shape(car_data)

# print after_date
# print np.shape(car_data-temp)

# list2csv(car_data, car_data_path)
# list2csv(buy_data, buy_data_path)
car_data.to_csv(car_data_path)
buy_data.to_csv(buy_data_path)

print 'success'

# item_data.to_csv(item_after)