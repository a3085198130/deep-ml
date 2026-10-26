import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    A=np.array(a,dtype=np.float64)
    B=np.array(b,dtype=np.float64)
    if A.shape[1] != B.shape[0]:
        return -1
    m=A.shape[0]
    n=B.shape[1]
    t=A.shape[1]
    # 方式1 推荐（不会浅拷贝bug）
    c = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(t):
                c[i][j]+=A[i][k]*B[k][j]
    return c