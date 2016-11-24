# coding: utf-8
import math


def rectified_linear_function(x):
    """
    正規化線形関数
    :param x:
    :return:
    """
    return max([x, 0])
