def calculation(x):
    return (x+10)**2

numbers = [1, 2, 3, 4]

ans = []

func = lambda x: (x+10)**2

# ans = map(func, numbers)
ans = map(calculation, numbers)
ans = list(ans)
print(ans)