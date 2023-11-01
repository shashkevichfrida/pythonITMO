import numpy as np

class Simplex_table:

    matrix: np.ndarray

    height: int
    width: int

    def __init__(self, shape: np.shape):
        self.matrix = np.zeros(shape)
        self.height = shape[0]
        self.width = shape[1]

    def Print(self):
        print(self.matrix)


    def SetRow(self, row: np.ndarray, rowIndex: int):
        self.matrix[rowIndex] = row
    
    def Solve(self) -> np.ndarray:
        basis = {}

        self.removeZeroRows()

        while(not self.isReferencePlan()):
            print("\n\nreferencing:\n")
            foundSolving, x, y = self.solvingElementForReference()

            if not foundSolving:
                print("no solvation")
                return

            self.jordanStep(x, y)

            print(self.matrix)
            print()

        while(not self.isOptimal()):
            print("\n\noptimizing:\n")
            foundSolving, x, y = self.solvingElementForOptimal()

            if not foundSolving:
                print("no solvation")
                return
            
            self.jordanStep(x, y)

            basis[y] = x

            print(self.matrix)
            print()


        for key in basis.keys():
            basis[key] = self.matrix[key, self.width-1]

        print("basis: ", basis)

        return self.matrix
    
    def jordanStep(self, solving_x: int, solving_y: int):

        print("step at x = ", solving_x, " y = ", solving_y)

        solving_value = self.matrix[solving_y, solving_x]

        new_matrix = np.zeros(self.matrix.shape)

        for i in range(self.width):
            new_matrix[solving_y, i] = self.matrix[solving_y, i]/solving_value

        for i in range(self.height):
            new_matrix[i, solving_x] = -self.matrix[i, solving_x]/solving_value

        for i in range(self.height):
            if i == solving_y:
                continue

            for j in range(self.width):
                if j == solving_x or (j == 0 and i == self.height-1):
                    continue

                new_matrix[i, j] = self.matrix[i, j] - (self.matrix[solving_y, j] * self.matrix[i, solving_x])/solving_value

        new_matrix[solving_y, solving_x] = 1/solving_value

        self.matrix = new_matrix

    def isOptimal(self) -> bool:
        flag = True

        for i in range(1, self.width-1):
            if self.matrix[self.height-1, i] < 0:
                flag = False
                break
            
        return flag
            

    def isReferencePlan(self) -> bool:
        for i in range(self.height):
            if self.matrix[i, self.width - 1] < 0:
                return False
            
        return True
            

    def removeZeroRows(self):
        while(True):
            found, i = self.findZeroRow()
            if not found:
                break

            found, l = self.zeroSolvingElement(i)
            if not found:
                print("Противоречащие ограничения")
                return
            
            self.jordanStep(l, i)

            self.matrix = np.delete(self.matrix, (i), axis=0)
            self.height = self.height-1

        print("after deleting zero rows:\n", self.matrix)

    def findZeroRow(self) -> (bool, int):
        for i in range(self.height-1):
            if self.matrix[i, 0] == 0:
                return True, i
            
        return False, 0
    
    def zeroSolvingElement(self, row: int) -> (bool, int):
        b_row = self.matrix[row, self.width-1]

        flag = False
        solving_column = 1

        for i in range(1, self.width-1):
            if self.matrix[row, i] == 0:
                continue

            fraction = b_row / self.matrix[row, i]

            if fraction <= b_row / self.matrix[row, solving_column] and fraction > 0:
                solving_column = i
                flag = True

        return flag, solving_column


    def solvingElementForOptimal(self) -> (bool, int, int):
        finded = False

        coeff_width = self.width - 1
        coeff_height = self.height - 1

        min_solving_value = 10**10
        min_solving_x = 0
        min_solving_y = 0

        for l in range(1, coeff_width):
            if self.matrix[self.height-1, l] >= 0:
                continue

            for j in range(coeff_height):
                if self.matrix[j, l] <= 0:
                    continue

                b_j = self.matrix[j, self.width-1]

                if b_j / self.matrix[j, l] < min_solving_value:
                    min_solving_value = self.matrix[j, l]
                    min_solving_x = l
                    min_solving_y = j
                    finded = True

        return finded, min_solving_x, min_solving_y
    
    def solvingElementForReference(self) -> (bool, int, int):
        negative_b_row: int

        for i in range(self.height-1):
            if self.matrix[i, self.width-1] < 0:
                negative_b_row = i
                break

        solving_column: int
        finded = False

        for i in range(1, self.width-1):
            if self.matrix[negative_b_row, i] < 0:
                finded = True
                solving_column = i
                break

        if not finded:
            print("controversy in constraint")
            return False, 0, 0
        
        solving_row = 0

        for j in range(self.height-1):
            fraction = self.matrix[j, self.width-1] / self.matrix[j , solving_column]

            if fraction < self.matrix[solving_row, self.width-1] / self.matrix[solving_row , solving_column]:
                solving_row = j

        return True, solving_column, solving_row

