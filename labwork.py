#5
def func(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'b': 5, 'e': 6}

result = func(dict1, dict2, dict3)
print(result)
