"""関数"""

# デフォルト引数
def print_name(name = 'Hiroto'):
    print(name)

print_name()        # Hiroto
print_name('Taro')  # Taro

# 関数オブジェクト
func = print_name
func() # Hiroto

# return がない場合は戻り値はNoneになる
def not_return():
    pass

print(not_return()) # None

# キーワード引数
def add(a, b):
    print(f"{a=}, {b=}")
    return a + b

add(b = 20, a = 30) # a=30, b=20
