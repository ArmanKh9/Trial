'''
This creates the following csv files from the original annotation csv data file:
    If test data is 0.2 of the origianl data set and training and validation are 0.7/0.3 then:
    1- Training = 0.8*(number of rows in the original annotation file)
    2- Test = 0.2*(number of rows in the original annotation file)
'''

import pandas as pd

fraction_of_data_train = 0.8
train_annotation_output_name = 'OID_annotation_tree_train.csv'
test_annotation_output_name = 'OID_annotation_tree_test.csv'
output_csv_path = '/home/arman/Desktop/Trial/Annotation/label_tree_data/'
annotation_data_file = '/home/arman/Desktop/Trial/Annotation/OID_annotation_label_tree_test.csv'

#read the original annotation data csv file into dataframe
annotation_df = pd.read_csv(annotation_data_file)
annotation_df = annotation_df.set_index('ImageID')

#create a sub-dataframe for train dataset which includes both training and validation data
# and ensuring that no image is in both train and test data sets
count_1 = 0
while (annotation_df.index[int(fraction_of_data_train*annotation_df.shape[0]) + count_1] == annotation_df.index[int(fraction_of_data_train*annotation_df.shape[0]) + count_1 - 1]):
    count_1 = count_1 + 1

df = annotation_df.iloc[0:int(fraction_of_data_train*annotation_df.shape[0]) + count_1]

#create a csv file to include rows from 0 to fraction_of_data_train_train*(total number of rows) in the
# fraction of the original data that was extracted for training and validation together
# also ensuring that no image is in both train and valid data sets
df.to_csv(path_or_buf = output_csv_path + train_annotation_output_name)

df = None
#create a sub-dataframe for test data set that is (1-fraction_of_data_train) of the original annotation dataset
df = annotation_df.iloc[int(fraction_of_data_train*annotation_df.shape[0]) + count_1 : annotation_df.shape[0]]

#create a csv file to include rows from fraction_of_data_train*(total number of rows)+1 to total number of rows
#in the original annotation data file
df.to_csv(path_or_buf = output_csv_path + test_annotation_output_name)

