import logging
import os
from datetime import datetime
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
#from tensorflow.keras.models import load_model

def write_image(out, frame):
    """
    writes frame from the webcam as png file to disk. datetime is used as filename.
    """
    if not os.path.exists(out):
        os.makedirs(out)
    now = datetime.now() 
    dt_string = now.strftime("%H-%M-%S-%f") 
    filename = f'{out}/{dt_string}.png'
    logging.info(f'write image {filename}')
    cv2.imwrite(filename, frame)


def key_action():
    # https://www.ascii-code.com/
    k = cv2.waitKey(1)
    if k == 113: # q button
        return 'q'
    if k == 32: # space bar
        return 'space'
    if k == 112: # p key
        return 'p'
    return None


def init_cam(width, height):
    """
    setups and creates a connection to the webcam
    """

    logging.info('start web cam')
    cap = cv2.VideoCapture(0)

    # Check success
    if not cap.isOpened():
        raise ConnectionError("Could not open video device")
    
    # Set properties. Each returns === True on success (i.e. correct resolution)
    assert cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    assert cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    return cap


def add_text(text, frame):
    # Put some rectangular box on the image
    # cv2.putText()
    return NotImplementedError


def run_model(image):
    #classes=os.listdir('../data/')
    image=np.array(image)
    image=np.expand_dims(image,axis=0)
    s_model = load_model("../models/modelfix.h5")
    prediction=s_model.predict(image)
    print(prediction)
    return prediction

def run_model2(image):
    #classes=os.listdir('../data/')
    img=load_img('../data/vader/14-07-54-274602.png',target_size=(224,224))
    image=np.array(image)
    image=np.expand_dims(image,axis=0)
    s_model = load_model("../models/modelfix.h5")
    prediction=s_model.predict(image)
    print(prediction)
    return prediction
    