#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module desciption: 
Description of what InferenceTemplate.py does.
"""
# InferenceTemplate.py created at 10-02-2023
__author__ = "Abhay Kumar"
__date__ = "10-02-2023"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = ""
__email__ = ""

from abc import ABC, abstractmethod

import numpy as np


class ClassificationInference(ABC):
    """
    A common set of properties and behavior for all Inference needs
    """

    def __init__(self, model_location: str):
        self.model_obj = None
        self.model_location = model_location
        self.class_names = []

    @staticmethod
    @abstractmethod
    def download_model(self):
        pass

    @abstractmethod
    def load_model(self):
        pass

    def load_classes(self, labels: list):
        pass

    def invalidate_model(self):
        if self.model_obj:
            self.model_obj = None

    def invalidate_class_names(self):
        if self.class_names:
            self.class_names = []

    @abstractmethod
    def preprocess(self):
        pass

    @abstractmethod
    def post_process(self):
        pass

    @abstractmethod
    def predict_probability(self, image_array) -> np.array():
        """
        :return:
        """
        pass

    @abstractmethod
    def predict(self, image_array: np.array, threshold: float = 0.5) -> np.array():
        """
        :param image_array: image array of shape [nXHxWxChannel]
        :param threshold: floar
        :return: image array of shape [nXClasses]
        """
        pass


if __name__ == '__main__':
    pass
