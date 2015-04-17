import pandas as pd
import numpy as np
import time as time
from pandas.tseries.offsets import Day,Hour
from pandas import DataFrame,Series

date_begin = pd.to_datetime('2014-12-19 00')
item_path = '../ali/tianchi_mobile_recommend_train_item.csv'
user_path    = '../ali/tianchi_mobile_recommend_train_user.csv'


# devide total data into files with each behaviors
def writeBehaviorToFile(behavior_filename, behavior_type, befor_days = 7):
	#read data from train_user
	user_data = pd.read_csv(user_path,sep=',')
	
	#transform date time to standard type
	user_data.time = pd.to_datetime(user_data.time);
	behavior_data = user_data[user_data.time > date_begin - befor_days*Day()]

	#exact the data with behavior type
	behavior_data = user_data[user_data.behavior_type == behavior_type]
	print behavior_data.head(3)

	#write the data into csv
	behavior_data.to_csv(behavior_filename)

if __name__ == '__main__':
	writeBehaviorToFile('car.csv', 3)
	writeBehaviorToFile('buy.csv', 4)

