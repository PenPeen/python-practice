"""dict"""

# 宣言
dict = {'a': 10, 'b': 20}
print(type(dict)) # <class 'dict'>

# 要素の追加
dict['c'] = 30
print(dict) # {'a': 10, 'b': 20, 'c': 30}

# 要素の削除(pop or del)
dict.pop('c')
print(dict) # {'a': 10, 'b': 20}

del dict['b']
print(dict) # {'a': 10}

# for文での繰り返し
dict = {'a': 10, 'b': 20, 'c': 30}
for d in dict:
    print(d) # a, b, c（キーが順次取り出される）

# for + values
for d in dict.values():
    print(d) # 10, 20, 30（値が順次取り出される）

# for + items
for key, value in dict.items():
    print(key) # a, b, c（キーが順次取り出される）
    print(value) # 10, 20, 30（値が順次取り出される）

# キーの存在検証
print('a' in dict) # True
print('d' in dict) # False

# 値の存在検証
print(10 in dict.values()) # True
print(40 in dict.values()) # False
