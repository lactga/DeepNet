import numpy as np


def mse(x, y):
    """
    平均二乗誤差
    :param x <numpy array>:
    :param y <numpy array>:
    :return:
    """
    if len(x) != len(y):
        raise ValueError('引数xとyの長さが異なります')
    if not len(x):
        raise ValueError('xとyの長さは1以上である必要があります')

    return ((x - y) ** 2).mean()