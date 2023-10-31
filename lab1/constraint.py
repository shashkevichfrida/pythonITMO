import numpy as np
import json

class Constraint:
    Coefficients: np.array

    Type: str

    B: float

    def Map(self, raw_data: json):
        self.Coefficients = np.array(raw_data['coefs'])

        self.Type = raw_data['type']

        self.B = raw_data['b']

    def ToCanonical(self, number_of_added_variables: int) -> int:
        if self.Type == "gte":
            self.Coefficients = np.append(self.Coefficients, np.zeros(number_of_added_variables))
            self.Coefficients = np.append(self.Coefficients, -1)
        elif self.Type == "lte":
            self.Coefficients = np.append(self.Coefficients, np.zeros(number_of_added_variables))
            self.Coefficients = np.append(self.Coefficients, 1)
        else:
            return number_of_added_variables
        
        self.Type = "eq"

        return number_of_added_variables + 1

    def Print(self):
        print(self.Coefficients, " ", self.Type, " ", self.B, "   len = ", len(self.Coefficients))

    def Validate(self, validsize: int) -> bool:
        return len(self.Coefficients) == validsize