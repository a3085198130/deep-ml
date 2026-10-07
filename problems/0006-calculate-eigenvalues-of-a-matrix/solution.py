import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    
    trace = a + d
    det = a * d - b * c
    
    # 特征方程 λ² − trace·λ + det = 0
    discriminant = trace ** 2 - 4 * det
    
    sqrt_d = math.sqrt(discriminant)
    lambda1 = (trace + sqrt_d) / 2
    lambda2 = (trace - sqrt_d) / 2
    
    # 从大到小排序
    eigenvalues = sorted([lambda1, lambda2], reverse=True)
    return eigenvalues
