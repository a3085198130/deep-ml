import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    # 转为numpy数组
    arr = np.array(a)
    # 检查元素总数是否匹配，不匹配返回空列表
    if arr.size != new_shape[0] * new_shape[1]:
        return []
    # 重塑矩阵，再转回python list
    reshaped_arr = arr.reshape(new_shape)
    reshaped_matrix = reshaped_arr.tolist()
    return reshaped_matrix
