def do_something(a, b, c, *args, **kwargs):
    print("funkcija")
    print(a, b, c)
    print(args, type(args))
    for i in args:
        print(i)

    print(kwargs, type(kwargs))
    if "word" in kwargs:
        print("word exists")
    print("ciklas veikia")


do_something(1, 2, 3, 8, words=9, z=99)


def another_function(a, **kwargs):
    print(a)
    print(kwargs)


another_function(a=9, nesamone=10)
