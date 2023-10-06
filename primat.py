import json

def change_coefs(coefs, type_operation):
    for i in range(len(coefs)):
        if coefs[i] == 0 and type_operation == 'eq':
            coefs[i] = 1
            break
        elif coefs[i] == 0 and type_operation == 'gte':
            coefs[i] = -1
            break



def canonical_form(equation):
    for i in equation:
        if i.get('type') == 'eq':
            coefs = i.get('coefs')
            change_coefs(coefs, 'eq')
            i['type'] = 'lte'

        if i.get('type') == 'gte':
            coefs = i.get('coefs')
            change_coefs(coefs, 'gte')
            i['type'] = 'lte'
    return equation




json_str = '''{
    "f": [1, 2, 3],
    "goal": "max",
    "constraints": [
        {
            "coefs": [1, 0, 0],
            "type": "eq",
            "b": 1
        },
        {
            "coefs": [1, 1, 0],
            "type": "gte",
            "b": 2
        },
        {
            "coefs": [1, 1, 1],
            "type": "lte",
            "b": 3
        }
    ]
}'''

equation = json.loads(json_str)
constraints = equation.get('constraints')

canonical_form(constraints)
print(equation)