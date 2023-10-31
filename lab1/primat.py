import json
import equation as eq

def change_coefs(coefs, type_operation):
    for i in range(len(coefs)):
        if coefs[i] == 0 and type_operation == 'eq':
            coefs[i] = 1
            break
        elif coefs[i] == 0 and type_operation == 'gte':
            coefs[i] = -1
            break



def canonical_form(constrants):
    for constrant in constrants:
        if constrant.get('type') == 'eq':
            coefs = constrant.get('coefs')
            change_coefs(coefs, 'eq')
            constrant['type'] = 'lte'

        if constrant.get('type') == 'gte':
            coefs = constrant.get('coefs')
            change_coefs(coefs, 'gte')
            constrant['type'] = 'lte'
    return constrants

json_str= open('input.json', 'r', encoding='utf-8').read()

def unmarshal_Equation(json_data) -> eq.Equaton:
    raw_data = json.loads(json_data)

    equation = eq.Equaton()

    equation.Map(raw_data)

    return equation

equation = unmarshal_Equation(json_str)

print("equation:")

equation.Print()
print("solvation: ")
equation.Solve()



