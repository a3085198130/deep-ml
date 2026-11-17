import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations

    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape                # m样本数量，n参数数量（含截距）
    y = y.reshape(-1, 1)         # 转为(m,1)列向量，方便矩阵运算
    theta = np.zeros((n, 1))     # 初始化权重为0，形状(n,1)

    for _ in range(iterations):
        y_hat = X @ theta         # 预测值 h_θ(x) = Xθ
        grad = (X.T @ (y_hat - y)) / m   # 计算梯度 ∇L
        theta = theta - alpha * grad     # 梯度下降更新

    return theta.flatten()        # 转为一维数组返回
