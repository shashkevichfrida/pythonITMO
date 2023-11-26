import dominant_strategy as ds
import numpy as np
import json

#matrix = np.array([[8,9,9,4], [6,5,8,7],[3,4,8,6], [8,9,9,4]])
json_str= open('input.json', 'r', encoding='utf-8').read()
data = json.loads(json_str)
matrix = data['matrix']

ds.dominant_strategy(matrix)


