# Training

The following steps needs to be taken to train "faster_rcnn_inception_resnet_v2_atrous_oid" model on a new dataset. The new dataset here is the "test" dataset downloaded from the Open Image Dataset (OID).

## Downloading Data Files

Open Image Dataset stores image annotation and box data in csv files. First, download  test-annotations-bbox.csv from this link and place it in the OID_Dataset folder https://www.figure-eight.com/dataset/open-images-annotated-with-bounding-boxes/

The downloaded file is a CSV file that contains all ground truth and classified bounding boxes for each image in the test set.
Then, download test-images.csv from the same link and place it in the OID_Dataset folder. The downloaded file contains URL address of all test images.


## Data preparation

Two sets of data are needed to train the model. One set is TRAIN and one set is TEST. Each of these sets needs to be fed into the model during training. Hence, the downloaded file from the OID website needs to be split into Test and Train sets.

### csv file preparation and Image download (data_util folder)
Make sure all of the created files are placed in the right folders. Destination folders are defined in the py script files.

#### 1- Run this file "OID_annotation_and_imageURL_csv_creator.py"
Before running the file, pay attention to the section that requires user to make changes. This file searches through the test-annotations-bbox.csv and filter images that contain a certain class boxes and the create two csv files as follows:
1- A csv file that contains images with the filetered class box in them and the box information
2- A csv file that contains all URL links of images with the fileterd class box 

In this case, OID_annotation_and_imageURL_csv_creator.py searches for boxes with label "tree". The label, however, has an identification code which is '/m/07j7r'. For identification code of each class see: class-descriptions-boxable.csv in here https://storage.googleapis.com/openimages/web/download.html

#### 2- Run this file "OID_image_with_certain_label_download_python2.py"
Before running the file, pay attention to the section that requires user to make changes. This script downloads all images from URLs listed in the csv file that was created in 1.

#### 3- Run this file "OID_annotation_test_data_csv_split(train_test_only).py"
Before running the file, pay attention to the section that requires user to make changes. This script creates two csv files of image box annotations. One for Train and one for Test dataset.

#### 4- Run this file "file_categorizer.py"
Before running the file, pay attention to the section that requires user to make changes. This script move images that belong to each Train and Test sets to its corresponding folder. Note that the folders must be created before running the file


### TFR file creation for training (TFR_Creator folder)

#### Run the file "TFRecord_creator_for_OID_python2.py"
Before running the file, pay attention to the section that requires user to make changes. The model uses tensorflow record files (TFR) to train models. These record files store image raw files along with box and annotation information in TFRecord or TFR formats.

### Label map modification

#### Downloading and modifying the OID label map
Download the OID label map file named "oid_bbox_trainable_label_map.pbtxt" in the Tensorflow Object Detection Model repository in here https://github.com/tensorflow/models/tree/master/research/object_detection/data
The label map must be in the correct format. Class codes and numbers must be correctly defined. "label_map_tree.pbtxt" is the modified version of the OID label map to only include the tree class. Ths label map will be used later for training

## Training a pretrained model
Follow the steps in "Quick Start: Training a pet detector" (if running on cloud) or "Running locally" (if running locally) in here: https://github.com/tensorflow/models/tree/master/research/object_detection

Use the "code_shortcut" file for modified codes. Consider the followings when modifying the pet detector steps:

### Downloading the pretrained "faster_rcnn_inception_resnet_v2_atrous_oid" model

This model is a pretrained faster rcnn model which is pretrained on OID. Download the latest version of "faster_rcnn_inception_resnet_v2_atrous_oid" from here and extract it in the Saved_Models/"Model_Name_Here" folder: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

### Updating version of the downloaded mode to match the installed tensorflow version
As mentioned in here: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md the model may not be compatible with other versions of TF. Hence, it needs to update by steps described in here: 
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/exporting_models.md

Shortcut
~~~
# From tensorflow/models/research/
INPUT_TYPE=image_tensor \
PIPELINE_CONFIG_PATH=/home/arman/Desktop/Trial/Saved_Models/faster_rcnn_inception_resnet_v2_atrous_oid_2018_01_28/pipeline.config \
TRAINED_CKPT_PREFIX=/home/arman/Desktop/Trial/Saved_Models/faster_rcnn_inception_resnet_v2_atrous_oid_2018_01_28/model.ckpt \
EXPORT_DIR=/home/arman/Desktop/Trial/Saved_Models/faster_rcnn_inception_resnet_v2_atrous_oid_2018_01_28/up_to_date_version

python object_detection/export_inference_graph.py \
    --input_type=${INPUT_TYPE} \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --trained_checkpoint_prefix=${TRAINED_CKPT_PREFIX} \
    --output_directory=${EXPORT_DIR}
~~~

### Modifying the config file

The config file for the model must be modified in order for the model to run and train. Sample configs are provided by google in here: https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs

Make sure the config file is correctly modified for either running on cloud or your local machine. Once modified the config file, place the file in the "Configs" or "Configs/Cloud" folder depending on your training machine (cloud or local)








