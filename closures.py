'''
Nested functions:
    Function inside a function called nested function
    This function can access variables of enclosing scope
'''


def outer_func(msg):
    print("This is outer func")

    def inner_func():  # Nested function
        print("This is inner function",msg)
    inner_func()


outer_func("for understand")


'''
Non-local variables:
    use nonlocal keyword in order to modify the value of nonlocal variable
'''


def outer_func():
    a = 10     # local variable it is not a global variable

    def inner_func():
        nonlocal a
        a = 20
        print("inner func", a)
    return inner_func()


outer_func()

# closures function


def in_func(info):
    def out_func():
        print(info)
    return out_func


result = in_func("Welcome")
result()