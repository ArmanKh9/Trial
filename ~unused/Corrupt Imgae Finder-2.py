import tensorflow as tf
import sys
import os
import urllib2
from os import listdir
from PIL import Image
import matplotlib.image as mpimg



def tensorflow_pred(imagepath):

    #suppress TF log-info messages - remove to display TF logs 
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    #response = Image.open(imagepath)

    #image_data = response.read()
    image_data = mpimg.imread(imagepath)

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
                    in tf.gfile.GFile("/home/arman/Desktop/Trial/Label_map/label_map_tree.pbtxt")]
    try:
        graph = tf.Graph()
        with graph.as_default(): 
              # Unpersists graph from file
            with tf.gfile.FastGFile("/home/arman/Desktop/Trial/Saved_Models/graph.pbtxt", 'rb') as f:
                
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                _ = tf.import_graph_def(graph_def, name='')

        with tf.Session() as sess:
            
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
        
            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        
        for node_id in top_k:
            classification = label_lines[node_id]
            score = predictions[0][node_id]
            if (score >=0.5):
                return ('%s (score = %.5f)' % (classification, score))
            
    except tf.errors.InvalidArgumentError:
            print ('Poor image quality, unable to predict')
            
            
for filename in listdir('/home/arman/Desktop/Trial/Images/Train/'):
  if filename.endswith('.jpg'):
      imagepath = '/home/arman/Desktop/Trial/Images/Train/'+filename
      tensorflow_pred(imagepath)