#2
def fun(*args):
    print(sorted(args, key=len))

fun('asd', 'asdd', 'asd', 'asdssd')