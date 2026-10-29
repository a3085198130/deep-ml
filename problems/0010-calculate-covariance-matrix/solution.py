def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_samples = len(vectors[0])
    # 计算每个特征的均值
    means = [sum(f) / n_samples for f in vectors]
    
    cov_matrix = [[0.0 for _ in range(n_features)] for _ in range(n_features)]
    
    for i in range(n_features):
        for j in range(n_features):
            total = 0.0
            for k in range(n_samples):
                total += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
            cov = total / (n_samples - 1)
            cov_matrix[i][j] = cov
    return cov_matrix
