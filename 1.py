print('asdgfas', 1234, 9.0)

def black_hole(*args):
    print(type(args))
    for argument in args:
        print(argument)

black_hole(234, 'Earth', 'rusnya', 'time', 1243)

def black_hole_named(**kwargs):
        print(type(kwargs))
        for key, value in kwargs.items():
            print(key, value)
black_hole_named(name='Gleb', planet='Earth', number = 5)