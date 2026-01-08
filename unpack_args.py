""" *args """

def add(a, b, c):
    print(f'{a=} {b=} {c=}')
    return a + b + c

args = [10, 20, 30]
result = add(*args)                 # a=10 b=20 c=30
print(result)                       # 60

""" **args """

def add_key_word_only(*, a, b, c):
    print(f'{a=} {b=} {c=}')
    return a + b + c

args = {'a': 10, 'b': 20, 'c': 30}
result = add_key_word_only(**args)  # a=10 b=20 c=30
print(result)                       # 60

""" *args & **args """

def add_key_word_mix(*a, **b):
    print(f'{a=} {b=}')

# a=(10, 20, 30) b={'a': 10, 'b': 20, 'c': 30}
args = [10, 20, 30]
args2 = {'a': 10, 'b': 20, 'c': 30}
add_key_word_mix(*args, **args2)

# a=(10, 20, 30) b={'d': 40, 'e': 50}
add_key_word_mix(10, 20, 30, d = 40, e = 50)
