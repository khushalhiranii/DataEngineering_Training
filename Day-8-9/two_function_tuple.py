def main_function(func1, func2, var):
    return (func1(var), func2(var))

def square(n):
    return n**2

def cube(n):
    return n**3

print(main_function(square, cube, 4))