import numpy as np


def binary_classification_log_likelihood(yhat, y):
    """
    対数尤度
    :param x <numpy array>:
    :param y <numpy array>:
    :return:
    """
    if len(yhat) != len(y):
        raise ValueError('yhatとyの長さが異なります')
    if not len(yhat):
        raise ValueError('yhatとyの長さは1以上である必要があります')
    if ((y != 0) & (y != 1)).any():
        raise ValueError('yは0,1の2値である必要があります')

    # 0*log0は0として計算。つまり、nanとなるデータは除いて足し合わせ
    tmp = y * np.log(yhat) + (1 - y) * np.log(1 - yhat)
    return -(tmp[~np.isnan(tmp)]).sum()

