import numpy as np
import simplex.constraint as ct
import simplex.simplex_table_try2 as stb
import json

class Equation:
    function: np.ndarray
    start_function: np.ndarray

    goal: str

    constraints: np.ndarray

    number_of_start_variables: int

    number_of_added_variables: int

    simplex_table: stb.Simplex_table

    def __init__(self, matrix: np.ndarray, function: np.ndarray, goal: str, type: str, b:float):
        self.function = function
        self.start_function = function
        self.number_of_start_variables = len(function)
        self.goal = goal

        constraintsLength = matrix.shape[0]

        self.constraints = np.ndarray(shape=(constraintsLength), dtype=ct.Constraint)
        for i in range(constraintsLength):
            self.constraints[i] = ct.Constraint(matrix[i], type, b)



    def Map(self, raw_equation: json):
        self.function = np.array(raw_equation['f'])
        self.start_function = self.function

        self.goal = raw_equation['goal']

        constraintsLength = len(raw_equation['constraints'])

        self.number_of_start_variables = len(raw_equation['constraints'][0]["coefs"])

        self.constraints = np.full(constraintsLength, fill_value=ct.Constraint())
        for i in range(constraintsLength):

            self.constraints[i] = ct.Constraint()

            self.constraints[i].Map(raw_equation['constraints'][i])

    def Validate(self) -> bool:

        self.Print()
        validLength = self.number_of_start_variables

        flag = True

        if len(self.function) != validLength:
            flag = False
        
        for constraint in self.constraints:
            if not constraint.Validate(validLength):
                flag = False
        return flag

    def toCanonical(self):

        if self.goal == "max":
            self.goal = "min"
            self.function = -self.function

        self.number_of_added_variables = 0

        for constraint in self.constraints:
            self.number_of_added_variables = constraint.ToCanonical(self.number_of_added_variables)

    def createSimplexTable(self):
        width = self.number_of_start_variables + self.number_of_added_variables + 2
        height = len(self.constraints) + 1
        self.simplex_Table = stb.Simplex_table((height, width))

        self.pushRowsToTable()


    def pushRowsToTable(self):
        for i in range(len(self.constraints)):

            constraint = self.constraints[i]

            rowSize = self.number_of_start_variables + self.number_of_added_variables + 2
            row = np.zeros(rowSize)
            row[rowSize -1] = constraint.B

            row[1:len(constraint.Coefficients)+1] = constraint.Coefficients

            if len(constraint.Coefficients) > self.number_of_start_variables:
                row[0] = constraint.Coefficients[-1]

            self.simplex_Table.SetRow(row, i)

        rowSize = self.number_of_start_variables + self.number_of_added_variables + 2
        funcRow = np.zeros(rowSize)
        funcRow[1:self.number_of_start_variables+1] = self.function
        self.simplex_Table.SetRow(funcRow, len(self.constraints))

    def Solve(self) -> np.ndarray:
        if not self.Validate():
            print("invalid equation")
            return
        self.toCanonical()

        print("canonical:")
        self.Print()

        self.createSimplexTable()

        self.simplex_Table.Print()

        solution = self.simplex_Table.Solve()

        print("solution:\n", solution)

        return solution

    def Print(self):
        print("func: ", self.function, " -> ", self.goal)
        print("number_of_start_variables = ", self.number_of_start_variables)
        print("constraints:")

        for constraint in self.constraints:
            constraint.Print()




