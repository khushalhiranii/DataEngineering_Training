def swap(a, b):
    a = a+b
    b = a-b
    a = a-b
    print('First element:', a)
    print('Second element:', b)

a=int(input('Enter first element to swap: '))
b=int(input('Enter second element to swap: '))
swap(a, b)
# print(a, b)