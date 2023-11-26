import input as ip
import dominant_strategy as ds
import optimal_point as op
import optimal_strategy as os
import numpy as np

matrix = ip.unmarshal_matrix()

print("matrix: ", matrix)

matrix = ds.dominant_strategy(matrix)

print("optimal point: ", op.findOptimalPoint(matrix))

flag, point = op.findOptimalPoint(matrix)

if not flag:
    os.Find_optimal_strategies(matrix)