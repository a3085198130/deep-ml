import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Standardization: (x - μ) / σ, ddof=0 总体标准差
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0, ddof=0)
    standardized_data = (data - mean) / std
    
    # Min-Max Normalization: (x - min) / (max - min)
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    normalized_data = (data - min_val) / (max_val - min_val)
    
    # 四舍五入保留4位小数
    standardized_data = np.round(standardized_data, 4)
    normalized_data = np.round(normalized_data, 4)
    
    return standardized_data, normalized_data
