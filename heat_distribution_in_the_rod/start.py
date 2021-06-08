import numpy as num
from config import Config


def get():
    result = [Config.U_0]
    n = int(Config.LENGTH / Config.DELTA_X)
    for i in range(1, n):
        current_x = i * Config.DELTA_X
        result.append(num.sin(2 * current_x))

    result.append(Config.U_LENGTH)
    return result
