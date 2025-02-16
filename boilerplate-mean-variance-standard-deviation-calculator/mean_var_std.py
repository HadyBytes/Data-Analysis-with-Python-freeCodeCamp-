import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    input_arr = np.array(list, dtype='float64')
    arr = np.reshape(input_arr, (3, 3))
    calculations = dict()
    calculations['mean'] = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean().tolist()]
    calculations['variance'] = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var().tolist()]
    calculations['standard deviation'] = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std().tolist()]
    calculations['max'] = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max().tolist()]
    calculations['min'] = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min().tolist()]
    calculations['sum'] = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum().tolist()]
    return calculations