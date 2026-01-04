"""タプル"""

# ()で定義
data = (1, 2, 3)
print(type(data)) # <class 'tuple'>

# , で定義
data = 1, 2, 3
print(type(data))

# ListからTupleの作成
lists = [1, 2, 3]
print(type(tuple(lists)))
