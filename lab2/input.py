import dominant_strategy as ds
import optimal_point as op
import json
import numpy as np

# fileName = 'without_optimal_point.json'
# fileName = 'with_optimal_point.json'
fileName = 'example.json'

def unmarshal_matrix() -> np.ndarray:
    json_str= open(fileName, 'r', encoding='utf-8').read()
    data = json.loads(json_str)
    matrix = data['matrix']

    return matrix