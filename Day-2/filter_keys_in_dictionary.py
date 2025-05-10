keys = ['a', 'bb', 'aca', 'awe', 'csd', 'all']
values = [1, 2, 3, 4, 5, 6]

my_dict = {k:v for (k,v) in zip(keys, values) if k[0] == 'a'}
print(my_dict.items())