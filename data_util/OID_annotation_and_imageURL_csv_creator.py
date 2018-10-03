import pandas as pd
import urllib.request

# user needs to define the followings
annotation_output_name = 'OID_annotation_label_tree_test.csv'
url_output_name = 'OID_url_label_tree_test.csv'
desired_label = '/m/07j7r'
output_csv_path = '/home/arman/Desktop/Trial/Annotation/'
annotation_data_file = '/home/arman/Desktop/Trial/OID_Dataset/test-annotations-bbox.csv'
URL_data_file = '/home/arman/Desktop/Trial/OID_Dataset/test-images.csv'

annotation_df = pd.read_csv(annotation_data_file)
annotation_df = annotation_df[annotation_df.LabelName == desired_label]
annotation_df = annotation_df.set_index('ImageID')
annotation_df.to_csv(path_or_buf = output_csv_path + annotation_output_name)

image_name_list = []
for i in range(annotation_df.shape[0]):
    image_name = annotation_df.index[i]+'.jpg'
    if image_name not in image_name_list:
        image_name_list.append(image_name)


#reading the csv file that contains image URLs for download
URL_data_file_df = pd.read_csv(URL_data_file, index_col = 'image_name')

#creating a list of image URLs
URL_list = []
for i in range(len(image_name_list)):
    URL_list.append(URL_data_file_df.loc[image_name_list[i]].image_url)

# creating a dataframe fro the url list
url_df = pd.DataFrame({'image_name': image_name_list,
           'image_url' : URL_list})

# creating csv file from the url dataframe that contain images with a certain box label
url_df = url_df.set_index('image_name')
url_df.to_csv(path_or_buf = output_csv_path + url_output_name)
