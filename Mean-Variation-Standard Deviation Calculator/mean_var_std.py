import numpy as np

def calculate(digits):
    if len(digits) < 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {'mean': list(), 'variance': list(), 'standard deviation': list(), 'max': list(), 'min': list(), 'sum': list()}

    array = np.array(digits).reshape(3,3)
    flatten_array = np.array(digits)
  
    for ax in range(2):
        calculations['mean'].append([x for x in array.mean(axis=ax)])
        calculations['variance'].append([x for x in array.var(axis=ax)])
        calculations['standard deviation'].append([x for x in array.std(axis=ax)])
        calculations['max'].append([x for x in array.max(axis=ax)])
        calculations['min'].append([x for x in array.min(axis=ax)])
        calculations['sum'].append([x for x in array.sum(axis=ax)])


    calculations['mean'].append(flatten_array.mean())
    calculations['standard deviation'].append(flatten_array.std())
    calculations['variance'].append(flatten_array.var())
    calculations['max'].append(flatten_array.max())
    calculations['min'].append(flatten_array.min())
    calculations['sum'].append(flatten_array.sum())
  
    return calculations