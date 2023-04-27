print('asdgfas', 1234, 9.0)

def black_hole(*args):
    print(type(args))
    for argument in args:
        print(argument)

black_hole(234, 'Earth', 'rusnya', 'time', 1243)

print()

def black_hole_named(**kwargs):
        print(type(kwargs))
        for key, value in kwargs.items():
            print(key, value)
black_hole_named(name='Gleb', planet='Earth', number = 5)

print()

def black_hole_full(*args, **kwargs):
    if not args: #для перевірки наявності не іменнованих аргументів
        return 0
    for argument in args:
        print(argument)
    for key, value in kwargs.items():
        print(key, value)
black_hole_full(234, 'Earth', 'rusnya', 'time', 1243,
                name='Gleb', planet='Earth', number = 5)

lst = [1,2,3]
dict_1 = {'n':1, 'b':2, 'a':3}

def fun(var_1, var_2, var_3):
    print(var_1, var_2, var_3)
fun(*lst)

def fun_dict(n, b, a):
    print(1, 2, 3)
fun_dict(**dict_1)