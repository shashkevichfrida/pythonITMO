import simplex.equation as eq
import numpy as np

def Find_optimal_strategies(matrix: np.ndarray):
    xA = solveA(matrix)
    print("\n\n================================================\n\n")
    yB, summ = solveB(matrix)

    print("\n\n\n\nxA: ", xA)
    print("yB: ", yB)

    print(f'game summ: {(1/summ):.4f}')
    print("S_b:")

    for key in yB.keys():
        print('%.4f' % (yB[key]/summ))







def solveA(matrix: np.ndarray):
    functionA = np.full(matrix.shape[0], fill_value=1) # len = m

    winA = eq.Equation(matrix.T, functionA, goal="min", type="gte", b=1)

    _, xA = winA.Solve()

    return xA

def solveB(matrix: np.ndarray):
    functionB = np.full(matrix.shape[1], fill_value=1) # len = n

    loseB = eq.Equation(matrix, functionB, goal="max", type="lte", b=1)

    matrix, yB = loseB.Solve()


    return yB, matrix[-1,-1]



