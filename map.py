"""
map
イテラブルに対して、組み込み関数を繰り返し適用する

基本構文
filter(関数, イテラブル)
"""

values = [v for v in range(11)]
print(values)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map()はイテレータを返すため、リスト化するにはlist()が必要
mapped = list(map(lambda x: x * 10, values))
print(mapped)   # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 複数の引数
names = ['Tom', 'Bob', 'Mike']
ages = [18, 20, 22]

print(list(map(lambda name, age: f"{name}:{age}", names, ages)))  # ['Tom:18', 'Bob:20', 'Mike:22']
