'''This script scans through Open Image Dataset related CSV files to find and download
images with a certain bounding box label (like tree, cat, dog, car, etc)
'''

import pandas as pd
import urllib
import tensorflow as tf
import os

# user needs to define the followings
desired_label = '/m/07j7r'
image_download_path = '/home/arman/Desktop/Trial/Images/'
annotation_data_file = '/home/arman/Desktop/Trial/Annotation/label_tree_data/OID_annotation_tree_test.csv'
URL_data_file = '/home/arman/Desktop/Trial/OID_Dataset/test-images.csv'

# reading data in the csv file that has '/m/07j7r' label which is "tree" label
# per label_map file
df = pd.read_csv(annotation_data_file, index_col='LabelName').loc[desired_label]

# create a list with image names to be used later for finding corresponding URL for download
image_name_list = []
for i in range(df.shape[0]):
    image_name = str(df.iloc[i].ImageID)
    if image_name not in image_name_list:
        image_name_list.append(image_name)

#reading the csv file that contains image URLs for download
df2 = pd.read_csv(URL_data_file, index_col = 'image_name')

#checking what images are in the destination folder
exist_images = tf.gfile.Glob(os.path.join(image_download_path, '*.jpg'))
exist_images_name = [os.path.splitext(os.path.basename(v))[0] for v in exist_images]

#creating a list of image URLs
URL_list = []
for i in range(len(image_name_list)):
    if image_name_list[i] not in exist_images_name:
        URL_list.append([df2.loc[image_name_list[i]+'.jpg'].image_url,
                         image_name_list[i]+'.jpg'])

#download images
for i in range(len(URL_list)):
    urllib.urlretrieve(URL_list[i][0], image_download_path + URL_list[i][1])

print(len(URL_list), 'images with box label ', desired_label,' were downloaded')
