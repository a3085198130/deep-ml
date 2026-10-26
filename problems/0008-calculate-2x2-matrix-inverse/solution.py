import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    T=np.array(matrix,dtype=np.float64)
    if T.shape[0] != T.shape[1]:
        return None
    try:
        T_inv = np.linalg.inv(T)
    except np.linalg.LinAlgError:
        # T奇异，不可逆
        return None
    return T_inv