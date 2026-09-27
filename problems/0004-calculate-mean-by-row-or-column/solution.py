def mat_mult(A, B):
    # 矩阵乘法 A * B
    n = len(A)
    m = len(B[0])
    k = len(B)
    res = [[0.0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0.0
            for t in range(k):
                s += A[i][t] * B[t][j]
            res[i][j] = s
    return res

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    if mode == 'row':
        # 每行均值：matrix @ ones(col,1) / n_cols
        ones_col = [[1.0] for _ in range(n_cols)]
        sum_rows = mat_mult(matrix, ones_col)
        means = [x[0] / n_cols for x in sum_rows]

    elif mode == 'column':
        # 每列均值：ones(1,row) @ matrix / n_rows
        ones_row = [[1.0 for _ in range(n_rows)]]
        sum_cols = mat_mult(ones_row, matrix)
        means = sum_cols[0]
        means = [v / n_rows for v in means]

    return means
