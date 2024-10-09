# Code to run OpenPose and extract keypoints

import cv2
import numpy as np
from openpose import pyopenpose as op

params= {
    "model_folder" : "models/pose_estimation_model/", 
    "hand": False,
    "face": False
}

opWrapper = op.WrapperPython()
opWrapper/configure(params)
opWrapper.start()

def extract_keypoints(image):
    datum = op.Datum()
    datum.cvInputData = image
    opWrapper.emplaceAndPop([datum])
    return datum.poseKeypoints