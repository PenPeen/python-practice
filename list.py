"""List"""

# 宣言
items = ['a', 'b', 'c']
print(type(items)) # <class 'list'>

# スライスによる要素取得（RubyでいうRange）
print(items[0:2]) # ['a', 'b']（先頭からitems[2]の一つ前まで取得）
print(items[:2]) # ['a', 'b']（:の前を省略すると先頭から）
print(items[1:]) # ['b', 'c']（:の後を省略すると最後まで）

# 要素の追加
items.append('d')
print(items) # ['a', 'b', 'c', 'd']

# 要素の削除
del items[1]
print(items) # ['a', 'c', 'd']
