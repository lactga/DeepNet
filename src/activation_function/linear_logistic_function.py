# coding: utf-8
import math


def linear_logistic_function(x):
    """
    ロジスティック関数を線形で近似した関数
    :param x:
    :return:
    """
    if x < -1:
        return -1
    elif x >= 1:
        return 1
    else:
        return x
