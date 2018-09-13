import os
import pandas as pd

train_annotation_input_name = 'OID_annotation_tree_train.csv'
valid_annotation_input_name = 'OID_annotation_tree_valid.csv'
test_annotation_input_name = 'OID_annotation_tree_test.csv'
input_csv_path = '/home/arman/Desktop/Trial/Annotation/label_tree_data/'
image_path = '/home/arman/Desktop/Trial/Images/'


train_df = pd.read_csv(input_csv_path + train_annotation_input_name)
valid_df = pd.read_csv(input_csv_path + valid_annotation_input_name)
test_df = pd.read_csv(input_csv_path + test_annotation_input_name)


for file_name in os.listdir('/home/arman/Desktop/Trial/Images'):
    file_name = file_name[0:-4]
    if os.path.isfile(image_path + file_name + '.jpg'):
        if file_name in train_df.ImageID.values:
            os.rename(image_path + file_name + '.jpg', 
                      image_path + 'Train/' + file_name + '.jpg')
        
        if file_name in valid_df.ImageID.values:
            os.rename(image_path + file_name + '.jpg', 
                      image_path + 'Valid/' + file_name + '.jpg')
            
        if file_name in test_df.ImageID.values:
            os.rename(image_path + file_name + '.jpg', 
                      image_path + 'Test/' + file_name + '.jpg')