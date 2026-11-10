import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    m = len(b)
    x = [0.0 for _ in range(m)]  # 初始全0
    for _ in range(n):
        x_new = [0.0] * m
        for i in range(m):
            s = 0.0
            for j in range(m):
                if j != i:
                    s += A[i][j] * x[j]
            x_new[i] = (b[i] - s) / A[i][i]
        x = x_new
    # 最终保留4位小数
    return [round(v, 4) for v in x]