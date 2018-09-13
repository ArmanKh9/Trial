
image_input_path = '/home/arman/Desktop/Trial/Images/Train/'
import tensorflow as tf
import os
import pandas as pd



all_images = tf.gfile.Glob(os.path.join(image_input_path, '*.jpg'))
all_image_ids = [os.path.splitext(os.path.basename(v))[0] for v in all_images]
all_image_ids = pd.DataFrame({'ImageID': all_image_ids})



for i in range(len(all_images)):
    
    
    