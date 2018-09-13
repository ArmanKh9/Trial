import tensorflow as tf
import os
import numpy as np
import sys
import cv2
sys.path.append('/home/arman/treecoin/models/research')
from object_detection.utils import dataset_util
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#user to populate the following parameters
num_of_images = 2
image_input_path = '/home/arman/Desktop/Trial/'
output_path = '/home/arman/Desktop/Trial/TFR/'
output_name = 'new.record'


def create_tf_example(image, image_name):
    
      # TODO(user): Populate the following variables from your example.
      height = image.shape[0] # Image height
      width = image.shape[1] # Image width
      filename = image_name # Filename of the image. Empty if image is not from file
      encoded_image_data = image.tostring() # Encoded image bytes. tostring converts the image array into string
      image_format = b'jpeg' # b'jpeg' or b'png'
    
      xmins = [20/width] # List of normalized left x coordinates in bounding box (1 per box)
      xmaxs = [40/width] # List of normalized right x coordinates in bounding box
                 # (1 per box)
      ymins = [135/height] # List of normalized top y coordinates in bounding box (1 per box)
      ymaxs = [180/height] # List of normalized bottom y coordinates in bounding box
                 # (1 per box)
      classes_text = ['cat'] # List of string class name of bounding box (1 per box)
      classes = [1] # List of integer class id of bounding box (1 per box)
    
      tf_example = tf.train.Example(features=tf.train.Features(feature={
          'image/height': dataset_util.int64_feature(height),
          'image/width': dataset_util.int64_feature(width),
          'image/filename': dataset_util.bytes_feature(filename.encode('utf8')), #utf8 encodes th filename 
          #'image/source_id': dataset_util.bytes_feature(filename), #utf8 to be used to encode the filename
          'image/encoded': dataset_util.bytes_feature(encoded_image_data),
          'image/format': dataset_util.bytes_feature(image_format),
          'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
          'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
          'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
          'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
          'image/object/class/text': dataset_util.bytes_list_feature(
                  x.encode('utf8') for x in classes_text),
          'image/object/class/label': dataset_util.int64_list_feature(classes),
      }))
          
      return tf_example



writer = tf.python_io.TFRecordWriter(output_path + output_name)
    
# TODO(user): Write code to read in your dataset to examples variable
#image = mpimg.imread('/home/arman/Desktop/Trial/image_1.jpg')
examples = []
examples_name = []
for i in range(1, num_of_images+1):
    image = cv2.imread(image_input_path + 'image_' + str(i) + '.jpg')
    image_name = 'image_'+ str(i) + '.jpg'
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.astype(np.float32)
    examples_name.append(image_name)
    examples.append(image)

for j in range(len(examples)):
    tf_example = create_tf_example(examples[j], examples_name[j])
    writer.write(tf_example.SerializeToString())

writer.close()
