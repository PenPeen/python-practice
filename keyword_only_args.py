def keyword_only_args(a, *, b, c):
    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')

keyword_only_args(3, b = 4, c = 5)
# a=3
# b=4
# c=5

# keyword_only_args(3, 4, 5)
# 例外となる。
# TypeError: keyword_only_args() takes 1 positional argument but 3 were given
