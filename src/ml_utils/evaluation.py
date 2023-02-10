#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module description:
Description of what evaluation.py does.
"""
# evaluation.py created at 10-02-2023
__author__ = "Abhay Kumar"
__date__ = "10-02-2023"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = ""
__email__ = ""

from abc import ABC, abstractmethod
from typing import List

import numpy as np


class ClassificationTestTemplate(ABC):

    def __init__(self, class_names: List, true_labels: np.array, predicted_probabilities: np.array):
        """

        :param class_names:
        :param true_labels:
        :param predicted_probabilities:
        """
        self.class_names = class_names
        self.true_labels = true_labels
        self.predicted_probabilities = predicted_probabilities
        self.predicted_labels = np.argmax(predicted_probabilities,axis=1)

    @abstractmethod
    def produce_classification_report(self):
        pass

    @abstractmethod
    def produce_pr_plot(self):
        pass

    @abstractmethod
    def produce_roc_auc_plot(self):
        pass

    @abstractmethod
    def produce_confusion_matrix_plot(self):
        pass

    @abstractmethod
    def find_best_threshold_for_each_class(self):
        pass

    @abstractmethod
    def get_overall_accuracy(self):
        pass

    @abstractmethod
    def get_overall_precision(self):
        pass

    @abstractmethod
    def get_overall_recall(self):
        pass

    @abstractmethod
    def get_overall_f1_score(self):
        pass

    @abstractmethod
    def get_class_wise_accuracy(self):
        pass

    @abstractmethod
    def get_class_wise_precision(self):
        pass

    @abstractmethod
    def get_class_wise_recall(self):
        pass

    @abstractmethod
    def get_class_wise_f1_score(self):
        pass




if __name__ == '__main__':
    pass
