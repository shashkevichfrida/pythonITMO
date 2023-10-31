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

        #self.removeZeroRows()

        while(not self.isOptimal()):
            # if not self.isReferencePlan():
            #     continue
            foundSolving, x, y = self.solvingElement()

            if not foundSolving:
                print("no solvation")
                return

            self.jordanStep(x, y)

            print("\n\n\n")
            print(self.matrix)

        return self.matrix
    
    def isOptimal(self) -> bool:
        flag = True

        for i in range(1, self.width-1):
            if self.matrix[self.height-1, i] < 0:
                flag = False
                break
            
        return flag
    
    def jordanStep(self, solving_x: int, solving_y: int):

        print("\tjordanStep at ", solving_x, " ", solving_y)

        new_matrix = np.zeros(self.matrix.shape)

        for i in range(self.width):
            new_matrix[solving_y, i] = self.matrix[solving_y, i] / self.matrix[solving_y, solving_x]

        for i in range(self.height):
            if i == solving_y:
                continue

            for j in range(self.width):
                new_matrix[i, j] = self.matrix[i,j] - self.matrix[i, solving_x] * new_matrix[solving_y, j]

        self.matrix = new_matrix
        
        # for i in range(self.height):
        #     if i == solving_y:
        #         continue

        #     value = self.matrix[i, solving_x]
        #     self.matrix[i, solving_x] = -value/solving_value

        # for j in range(self.width):
        #     if j == solving_x:
        #         continue

        #     value = self.matrix[solving_y, j]
        #     self.matrix[solving_y, j] = value/solving_value

        # for i in range(self.height):
        #     if i == solving_y:
        #         continue

        #     for j in range(self.width):
        #         if j == solving_x:
        #             continue
                
        #         fraction = (self.matrix[solving_y, j] * self.matrix[i, solving_y]) / solving_value
        #         self.matrix[i, j] = self.matrix[i, j] - fraction

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
                print("govno")
                return
            
            self.jordanStep(l, i)

            self.matrix = np.delete(self.matrix, (i), axis=0)

    def findZeroRow(self) -> (bool, int):
        for i in range(self.height-1):
            if self.matrix[i, 0] == 0:
                return True, i
            
        return False, 0
    
    def zeroSolvingElement(self, row: int) -> (bool, int):
        b_row = self.matrix[row, self.width-1]

        for i in range(self.width-1):
            if self.matrix[row, i] >= 0:
                continue

            return True, i

        return False, 0


    # def solvingElement(self) -> (bool, int, int):
    #     finded = False

    #     coeff_width = self.width - 1
    #     coeff_height = self.height - 1

    #     min_solving_value = 10**10
    #     min_solving_x = 0
    #     min_solving_y = 0

    #     for l in range(1, coeff_width):
    #         if self.matrix[self.height-1, l] <= 0:
    #             continue

    #         for j in range(1, coeff_height):
    #             if self.matrix[j, l] <= 0:
    #                 continue

    #             b_j = self.matrix[j, self.width-1]

    #             if b_j / self.matrix[j, l] < min_solving_value:
    #                 min_solving_value = self.matrix[j, l]
    #                 min_solving_x = l
    #                 min_solving_y = j
    #                 finded = True

    #     return finded, min_solving_x, min_solving_y

    # def solvingElement(self) -> (bool, int, int):
    #     finded = False

    #     coeff_width = self.width - 1
    #     coeff_height = self.height - 1

    #     negative_b_row = 0

    #     for i in range(coeff_height):
    #         if self.matrix[i, self.width-1] < 0:
    #             negative_b_row = i
    #             break

    #     flag = False
    #     solving_column = 0
    #     for i in range(1, coeff_width):
    #         if self.matrix[negative_b_row, i] < 0:
    #             flag = True
    #             solving_column = i

    #     if not flag:
    #         return False, 0, 0
        
    #     min_fraction = 10**10
    #     min_solving_row = 0

    #     founded = False
        
    #     for i in range(coeff_height):
    #         b_row = self.matrix[i, solving_column]

    #         fraction = b_row/self.matrix[i, solving_column]
    #         if fraction < 0:
    #             continue

    #         if fraction < min_fraction:
    #             founded = True
    #             min_fraction = fraction
    #             min_solving_row = i

    #     return founded, solving_column, min_solving_row

    def solvingColumn(self) -> int:
        mainCol = 1;
 
        for j in range(1, self.width-1):
            if self.matrix[self.height-1, j] < self.matrix[self.height-1, mainCol]:
                mainCol = j
        print("main col = ", mainCol)
        return mainCol

    def solvingElement(self) -> (bool, int, int):
        solving_column = self.solvingColumn()
        solving_row = 0

        for i in range(self.height-1):
            if self.matrix[i, solving_column] > 0:
                solving_row = i
                break


        for i in range(solving_row, self.height):
            if self.matrix[i, solving_column] > 0 and ((self.matrix[i, self.width-1] / self.matrix[i, solving_column]) < (self.matrix[solving_row, self.width-1] / self.matrix[solving_row, solving_column])):
                solving_row = i

        print("main row = ", solving_row)
        return True, solving_row, solving_column







