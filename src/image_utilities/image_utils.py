#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module desciption: 
Description of what image_utils.py does.
"""
# image_utils.py created at 10-02-2023
__author__ = "Abhay Kumar"
__date__ = "10-02-2023"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = ""
__email__ = ""

from PIL import Image


def check_image_with_pil(path):
    try:
        Image.open(path)
    except IOError:
        print(f"[ERROR] there is a problem opening the image : {path}")
        return -1
    return 1


if __name__ == '__main__':
    pass
