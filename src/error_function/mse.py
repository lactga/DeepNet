def mse(yhat, y):
    """
    平均二乗誤差
    :param yhat <numpy array>:
    :param y <numpy array>:
    :return:
    """
    if len(yhat) != len(y):
        raise ValueError('yhatとyの長さが異なります')
    if not len(yhat):
        raise ValueError('yhatとyの長さは1以上である必要があります')

    return 1/2 * ((yhat - y) ** 2).mean()
