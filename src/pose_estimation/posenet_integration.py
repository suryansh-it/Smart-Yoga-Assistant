# Code to run PoseNet and extract keypoints
# posenet(15 keypoints)
import cv2
import tensorflow as tf
import numpy as np


#load posenet model
model = tf.keras.models.load_model('models/pose_estimation_model/posenet_model.h5')

def extract_keypoints(image):
    image= cv2.resize(image,(236,236))
    image= np.expand_dims(image,axis=0)/255.0
    keypoints= model.predict(image)
    return keypoints