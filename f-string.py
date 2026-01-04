"""フォーマット済み文字列リテラル"""

"""
f-string（Python3.6以降）
"""
name = "ikechi"
print(f"Hello {name}") # Hello ikechi

# Python3.8以降で利用できる省略記法
name = "ikechi"
print(f"{name=}") # name='ikechi'

"""
format（{}を引数に置換する）
"""
text = "Hello {}. My name is {}".format('Taro', 'Ikechi')
print(text) # Hello Taro. My name is Ikechi

# 引数の順番を指定する
text = "Hello {1}. My name is {0}".format('Taro', 'Ikechi')
print(text) # Hello Ikechi. My name is Taro

# キーワードを指定する
text = "Hello {t}. My name is {i}".format(t = 'Taro', i = 'Ikechi')
print(text) # Hello Taro. My name is Ikechi

# ハッシュをキーワード引数に指定
hash = {'a': 10, 'b': 20, 'c': 30}
print('{a}, {b}, {c}'.format(**hash)) # 10, 20, 30
