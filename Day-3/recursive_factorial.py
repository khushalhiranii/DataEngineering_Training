def factorial(number):
    if number==1:
        return 1
    else:
        return number * factorial(number-1)
    
number = input()

try:
    number = int(number)
    print(factorial(number))
except ValueError:
    print("Invalid input")