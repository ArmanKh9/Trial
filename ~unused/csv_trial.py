#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 00:05:03 2018

@author: arman
"""

import pandas as pd
import numpy as np

'''a = [1,2,3,4,5]
b= [10,20,30,40,50]

data = {'a': a,
        'b' : b}
df = pd.DataFrame(data=data)

print(df.shape)'''

'''df_1=pd.read_csv('/home/arman/Desktop/Trial/OID_Dataset/test-annotations-bbox.csv')
print(df_1.iloc[1])
df_2 = df_1.groupby('ImageID')
print(df_2)'''


'''row_0 = pd.read_csv('/home/arman/Desktop/Trial/annotation_trial.csv',
                    skiprows = lambda x: x not in [0])
row_1 = pd.read_csv('/home/arman/Desktop/Trial/annotation_trial.csv',
                    skiprows = lambda x: x not in [1])


print(df)'''

data1 = {
        'ImageID': ['i1', 'i1', 'i1', 'i1', 'i1', 'i2', 'i2'],
        'LabelName': ['abcv', 'a', 'b', 'b', 'c', 'b', 'c'],
        'YMin': [0.3, 0.6, 0.8, 0.1, None, 0.0, 0.0],
        'XMin': [0.1, 0.3, 0.7, 0.0, None, 0.1, 0.1],
        'XMax': [0.2, 0.3, 0.8, 0.5, None, 0.9, 0.9],
        'YMax': [0.3, 0.6, 1, 0.8, None, 0.8, 0.8],
        'IsOccluded': [0, 1, 1, 0, None, 0, 0],
        'IsTruncated': [0, 0, 0, 1, None, 0, 0],
        'IsGroupOf': [0, 0, 0, 0, None, 0, 1],
        'IsDepiction': [1, 0, 0, 0, None, 0, 0],
        'ConfidenceImageLabel': [None, None, None, None, 0, None, None],
        }
data2 = {
        'ImageID':['i1', 'i2']
        }
df1 = pd.DataFrame(data=data1)
df2 = pd.DataFrame(data=data2)


df_concat = pd.concat([df1,df2], sort=False)

df_grouped = df_concat.groupby('ImageID')

for counter, image_data in enumerate(df_grouped):
    print(image_data[0])
    
print(int('000132c20b84269b',16))
print(int('000132c20b84269b',16)%100)
#label_map = {'a': 0, 'b': 1, 'c': 2}

#df1 = df1.groupby('ImageID')



#for counter, image_data in enumerate(df1):
#    print(image_data[0])

'''
b"abcde"

b"abcde".decode("utf-8") '''