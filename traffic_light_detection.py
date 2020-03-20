
# This code was written on google colab so use the same for running it 
# name your test image as test_image.png
# After cloning the repository place your test image on ../content/Mask_RCNN/images 

# clone the github repo of the model
!git clone https://github.com/matterport/Mask_RCNN

# change the directory 
import os 
os.chdir('Mask_RCNN/samples')

# import the required directories
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt

# Root directory of the project
ROOT_DIR = os.path.abspath("../")

# Import Mask RCNN
sys.path.append(ROOT_DIR)  
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize

# Import COCO config
sys.path.append(os.path.join(ROOT_DIR, "samples/coco/"))  # To find local version
import coco

%matplotlib inline 

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

# Directory of images to run detection on
IMAGE_DIR = os.path.join(ROOT_DIR, "images")

class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()

# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on MS-COCO
model.load_weights(COCO_MODEL_PATH, by_name=True)

# COCO Class names
# Index of the class in the list is its ID
class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']

# move the new test image to (../content/Mask_RCNN/images) directory then only the model will detect it 
# path of the test image
path = '../images/test_image.png'
image = skimage.io.imread(path)

# Run the model on the test image for detection
results = model.detect([image], verbose=0)

# RCNN trained on COCO dataset detects many other classes including traffic signals 
# so we should seperate the id's and ROI of the traffic lights from the rest 
r = results[0]
array_class = r.get('class_ids')
res = np.where(array_class == 10)

# draw the bounding box from the obtained ROI data 
import cv2 as cv
qwe= [None]*len(res[0])
i = 0
while i < len(res[0]):
  j = res[0][i];
  qwe[i] = r['rois'][j]
  y1,x1,y2,x2 = qwe[i]
  final_image = cv.rectangle(image,(x1,y1),(x2,y2),(0,0,255),1)
  i +=1

# display the final image with bounding boxes
from google.colab.patches import cv2_imshow
cv2_imshow(final_image)
