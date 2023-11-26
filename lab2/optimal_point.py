import numpy as np

def findOptimalPoint(matrix: np.ndarray) -> (bool, float):
    a = np.min(matrix, axis=1)
    b = np.max(matrix, axis=0)

    maxMinA = np.max(a)
    minMaxB = np.min(b)

    # если найдена седловая точка 
    if maxMinA == minMaxB:
        return True, maxMinA
    
    return False, 0