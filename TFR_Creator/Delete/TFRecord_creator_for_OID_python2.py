import tensorflow as tf
import sys
import pandas as pd
import os

import contextlib2

sys.path.append('/home/arman/treecoin/models/research')
from object_detection.core import standard_fields
from object_detection.utils import dataset_util
from object_detection.utils import label_map_util
from object_detection.dataset_tools import tf_record_creation_util

#user to populate the following parameters
image_input_path = '/home/arman/Desktop/Trial/Images/Train/'
output_path = '/home/arman/Desktop/Trial/TFR/train.tfrecord'
label_map_path = '/home/arman/Desktop/Trial/Label_map/label_map_tree.pbtxt'
annotation_data_file = '/home/arman/Desktop/Trial/Annotation/label_tree_data/OID_annotation_tree_train.csv'
num_shards = 30


def tf_example_from_annotations_data_frame(annotations_data_frame, label_map,
                                           encoded_image):
    
  """Populates a TF Example message with image annotations from a data frame.

  Args:
    annotations_data_frame: Data frame containing the annotations for a single
      image.
    label_map: String to integer label map.
    encoded_image: encoded image

  Returns:
    The populated TF Example, if the label of at least one object is present in
    label_map. Otherwise, returns None.
  """
  filtered_data_frame = annotations_data_frame[
      annotations_data_frame.LabelName.isin(label_map)]
  filtered_data_frame_boxes = filtered_data_frame[
      ~filtered_data_frame.YMin.isnull()]
  filtered_data_frame_labels = filtered_data_frame[
      filtered_data_frame.YMin.isnull()]
  image_id = annotations_data_frame.ImageID.iloc[0]

  feature_map = {
      standard_fields.TfExampleFields.object_bbox_ymin:
          dataset_util.float_list_feature(
              filtered_data_frame_boxes.YMin.as_matrix()),
      standard_fields.TfExampleFields.object_bbox_xmin:
          dataset_util.float_list_feature(
              filtered_data_frame_boxes.XMin.as_matrix()),
      standard_fields.TfExampleFields.object_bbox_ymax:
          dataset_util.float_list_feature(
              filtered_data_frame_boxes.YMax.as_matrix()),
      standard_fields.TfExampleFields.object_bbox_xmax:
          dataset_util.float_list_feature(
              filtered_data_frame_boxes.XMax.as_matrix()),
      standard_fields.TfExampleFields.object_class_text:
          dataset_util.bytes_list_feature(
              filtered_data_frame_boxes.LabelName.as_matrix()),
      standard_fields.TfExampleFields.object_class_label:
          dataset_util.int64_list_feature(
              filtered_data_frame_boxes.LabelName.map(lambda x: label_map[x])
              .as_matrix()),
      standard_fields.TfExampleFields.filename:
          dataset_util.bytes_feature('{}.jpg'.format(image_id)),
      standard_fields.TfExampleFields.source_id:
          dataset_util.bytes_feature(image_id),
      standard_fields.TfExampleFields.image_encoded:
          dataset_util.bytes_feature(encoded_image),
  }

  if 'IsGroupOf' in filtered_data_frame.columns:
    feature_map[standard_fields.TfExampleFields.
                object_group_of] = dataset_util.int64_list_feature(
                    filtered_data_frame_boxes.IsGroupOf.as_matrix().astype(int))
  if 'IsOccluded' in filtered_data_frame.columns:
    feature_map[standard_fields.TfExampleFields.
                object_occluded] = dataset_util.int64_list_feature(
                    filtered_data_frame_boxes.IsOccluded.as_matrix().astype(
                        int))
  if 'IsTruncated' in filtered_data_frame.columns:
    feature_map[standard_fields.TfExampleFields.
                object_truncated] = dataset_util.int64_list_feature(
                    filtered_data_frame_boxes.IsTruncated.as_matrix().astype(
                        int))
  if 'IsDepiction' in filtered_data_frame.columns:
    feature_map[standard_fields.TfExampleFields.
                object_depiction] = dataset_util.int64_list_feature(
                    filtered_data_frame_boxes.IsDepiction.as_matrix().astype(
                        int))

  if 'ConfidenceImageLabel' in filtered_data_frame_labels.columns:
    feature_map[standard_fields.TfExampleFields.
                image_class_label] = dataset_util.int64_list_feature(
                    filtered_data_frame_labels.LabelName.map(
                        lambda x: label_map[x]).as_matrix())
    feature_map[standard_fields.TfExampleFields.
                image_class_text] = dataset_util.bytes_list_feature(
                    filtered_data_frame_labels.LabelName.as_matrix()),
  return tf.train.Example(features=tf.train.Features(feature=feature_map))

#below is what converted from python 3.5. Not sure if works. Some lines need to change to match python 2.7
'''
  filtered_data_frame = annotations_data_frame[
      annotations_data_frame.LabelName.isin(label_map)]
  filtered_data_frame_labelname_bytes = filtered_data_frame.LabelName.str.encode('utf8') #data need to be in bytes. str.encode('utf8') is used to change the data type from string to bytes
  filtered_data_frame_boxes = filtered_data_frame[
      ~filtered_data_frame.YMin.isnull()]
  filtered_data_frame_labels = filtered_data_frame[
      filtered_data_frame.YMin.isnull()]
  image_id = annotations_data_frame.ImageID.iloc[0]

  feature_map = {
      standard_fields.TfExampleFields.object_bbox_ymin:
          dataset_util.float_list_feature(
              filtered_data_frame_boxes.YMin.values),
      standard_fields.TfExampleFields.object_bbox_xmin:
          dataset_util.float_list_feature(
              filtered_data_frame_boxes.XMin.values),
      standard_fields.TfExampleFields.object_bbox_ymax:
          dataset_util.float_list_feature(
              filtered_data_frame_boxes.YMax.values),
      standard_fields.TfExampleFields.object_bbox_xmax:
          dataset_util.float_list_feature(
              filtered_data_frame_boxes.XMax.values),
      standard_fields.TfExampleFields.object_class_text:
          dataset_util.bytes_list_feature(
              filtered_data_fr  filtered_data_frame_labelname_bytes = filtered_data_frame.LabelName.str.encode('utf8')ame_labelname_bytes),
      standard_fields.TfExampleFields.object_class_label:
          dataset_util.int64_list_feature(
              filtered_data_frame_boxes.LabelName.map(lambda x: label_map[x])
              .values),
      standard_fields.TfExampleFields.filename:
          dataset_util.bytes_feature('{}.jpg'.format(image_id)),
      standard_fields.TfExampleFields.source_id:
          dataset_util.bytes_feature(image_id),
      standard_fields.TfExampleFields.image_encoded:
          dataset_util.bytes_feature(encoded_image),
  }

  if 'IsGroupOf' in filtered_data_frame.columns:
    feature_map[standard_fields.TfExampleFields.
                object_group_of] = dataset_util.int64_list_feature(
                    filtered_data_frame_boxes.IsGroupOf.values.astype(int))
      
  if 'IsOccluded' in filtered_data_frame.columns:
    feature_map[standard_fields.TfExampleFields.
                object_occluded] = dataset_util.int64_list_feature(
                    filtered_data_frame_boxes.IsOccluded.values.astype(int))
      
  if 'IsTruncated' in filtered_data_frame.columns:
    feature_map[standard_fields.TfExampleFields.
                object_truncated] = dataset_util.int64_list_feature(
                    filtered_data_frame_boxes.IsTruncated.values.astype(int))
      
  if 'IsDepiction' in filtered_data_frame.columns:
    feature_map[standard_fields.TfExampleFields.
                object_depiction] = dataset_util.int64_list_feature(
                    filtered_data_frame_boxes.IsDepiction.values.astype(int))

  if 'ConfidenceImageLabel' in filtered_data_frame_labels.columns:
    feature_map[standard_fields.TfExampleFields.
                image_class_label] = dataset_util.int64_list_feature(
                    filtered_data_frame_labels.LabelName.map(
                        lambda x: label_map[x]).values)
    feature_map[standard_fields.TfExampleFields.
                image_class_text] = dataset_util.bytes_list_feature(
                    filtered_data_frame_labels.LabelName.values),
  return tf.train.Example(features=tf.train.Features(feature=feature_map))'''


label_map = label_map_util.get_label_map_dict(label_map_path)
all_box_annotations = pd.read_csv(annotation_data_file)
all_images = tf.gfile.Glob(os.path.join(image_input_path, '*.jpg'))
all_image_ids = [os.path.splitext(os.path.basename(v))[0] for v in all_images]
all_image_ids = pd.DataFrame({'ImageID': all_image_ids})
all_annotations = pd.concat([all_box_annotations, all_image_ids], sort=False)

with contextlib2.ExitStack() as tf_record_close_stack:
    output_tfrecords = tf_record_creation_util.open_sharded_output_tfrecords(
        tf_record_close_stack, output_path, num_shards)
    
    for counter, image_data in enumerate(all_annotations.groupby('ImageID')):
        image_id, image_annotations = image_data
        
        image_path = os.path.join(image_input_path, image_id + '.jpg')
        with tf.gfile.Open(image_path) as image_file:    
            encoded_image = image_file.read()
            
        tf_example = tf_example_from_annotations_data_frame(
          image_annotations, label_map, encoded_image)
        
        if tf_example:
            shard_idx = int(image_id, 16) % num_shards
            output_tfrecords[shard_idx].write(tf_example.SerializeToString())
