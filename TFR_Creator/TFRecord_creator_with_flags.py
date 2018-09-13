import tensorflow as tf
import os
import numpy as np
import sys
import cv2
#os.chdir("/home/arman/treecoin/models/research")
sys.path.append('/home/arman/treecoin/models/research')

from object_detection.utils import dataset_util

import matplotlib.pyplot as plt
import matplotlib.image as mpimg



flags = tf.app.flags
flags.DEFINE_string('input_path', '/home/arman/Desktop/Trial/', 'Path to input images')#user must define input image path using flag on command line when running the script
flags.DEFINE_string('output_path', '', 'Path to output TFRecord') #user must define output path using flag on command line when running the script
FLAGS = flags.FLAGS


def create_tf_example(image):

    
      # TODO(user): Populate the following variables from your example.
      height = image.shape[0] # Image height
      width = image.shape[1] # Image width
      filename = 'image_1.jpg' # Filename of the image. Empty if image is not from file
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


def main(_):
      writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    
      # TODO(user): Write code to read in your dataset to examples variable
      #image = mpimg.imread('/home/arman/Desktop/Trial/image_1.jpg')
      examples=[]
      for i in range(1, 3):
          image = cv2.imread(FLAGS.input_path + 'image_' + str(i) + '.jpg')
          image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
          image = image.astype(np.float32)
          examples.append(image)

      for example in examples:
        tf_example = create_tf_example(example)
        writer.write(tf_example.SerializeToString())
    
      writer.close()
    

if __name__ == '__main__':
    tf.app.run()
