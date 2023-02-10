# image_io created at 04/02/22
__author__ = "Abhay Kumar"
__date__ = "04/02/22"
__copyright__ = "Copyright 2022"
__license__ = ""

"""
This module contains common utilities related to image
"""
import cv2
import numpy as np
from urllib.request import urlopen

def serialize_image_array(image_array):
    success,encoded_image = cv2.encode(".jpg",image_array)
    image_byte_array = encoded_image.tobytes()
    return image_byte_array

def serialise_image_file(image_path):
    image_byte_array = open(image_path,"rb").read()
    return image_byte_array

def serialise_image_from_url(image_url):
    image_byte_array = bytes(urlopen(image_url).read())
    return image_byte_array

def encode_image(image_path):
    if image_path.startswith("http"):
        image_byte_array = serialise_image_from_url(image_path)
    else:
        image_byte_array = serialise_image_file(image_path)
    return image_byte_array

def deserialize_to_image_array(image_byte_array ):
    image_np_array = np.frombuffer(image_byte_array,np.uint8)
    image_array = cv2.imdecode(image_np_array,cv2.IMREAD_COLOR)
    return image_array


