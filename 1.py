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
