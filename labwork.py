#4
humans = [('Sasha', 16), ('Sanya', 17), ('Oleksandr', 18)]

def fun(*args):
    name_age = {}
    if args:
        for tup in args[0]:
            name, age = tup
            name_age[name] = age
    return name_age
print(fun(humans))