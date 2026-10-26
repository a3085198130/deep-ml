import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    # 转numpy数组
    A_mat = np.array(A, dtype=np.float64)
    T_mat = np.array(T, dtype=np.float64)
    S_mat = np.array(S, dtype=np.float64)
    
    # 检查方阵
    if T_mat.shape[0] != T_mat.shape[1] or S_mat.shape[0] != S_mat.shape[1]:
        return -1
    # 检查维度匹配：T⁻¹ A S，T的列 = A行，A的列 = S行
    if T_mat.shape[1] != A_mat.shape[0] or A_mat.shape[1] != S_mat.shape[0]:
        return -1
    
    try:
        T_inv = np.linalg.inv(T_mat)
    except np.linalg.LinAlgError:
        # T奇异，不可逆
        return -1
    try:
        S_inv = np.linalg.inv(S_mat)
    except np.linalg.LinAlgError:
        return -1
    
    # 计算 T⁻¹ A S
    res_mat = T_inv @ A_mat @ S_mat
    # 转回list
    transformed_matrix = res_mat.tolist()
    return transformed_matrix
