def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float] | int:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    
    # Empty matrix case
    if len(a) == 0:
        return []
    
    col_count = len(a[0])
    vec_len = len(b)
    
    if col_count != vec_len:
        return -1
    
    result = []
    for row in a:
        dot = 0
        for ai, bi in zip(row, b):
            dot += ai * bi
        result.append(dot)
    return result
