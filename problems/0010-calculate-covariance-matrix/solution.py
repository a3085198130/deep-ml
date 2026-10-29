import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    X = np.array(vectors, dtype=float)
    means = np.mean(X, axis=1, keepdims=True)
    centered = X - means
    cov = centered @ centered.T / (X.shape[1] - 1)
    return cov.tolist()
