#2
def fun(*args):
    print(max(args, key=len))

fun('asd', 'asdd', 'asd', 'asdssd')