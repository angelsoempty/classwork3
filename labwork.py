#4
def fun(*args):
    result_dict = {}
    for arg in args:
        result_dict.update(arg)
    return result_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

result_dict = fun(dict1, dict2, dict3)
print(result_dict)
''