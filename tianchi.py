# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:21:55 2015

@author: MaogengXia
"""

import pandas as pd
import numpy as np
item_data = pd.read_csv('tianchi_mobile_recommend_train_item.csv')[1:]
print item_data
# user_data = pd.read_csv('tianchi_mobile_recommend_train_user.csv')[1:]
# itemMat = np.mat(item_data)
# userMat = np.mat(user_data)