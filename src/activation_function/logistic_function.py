# coding: utf-8
import math


def logistic_function(x):
    """
    ロジスティック関数
    :param x:
    :return:
    """
    return 1 / (1 + math.exp(-x))
