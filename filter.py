"""
filter
条件に合致する要素を含むイテレータオブジェクトを作成する

基本構文
filter(関数, イテラブル)
"""

values = [v for v in range(11)]
print(values)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter()はイテレータを返すため、リスト化するにはlist()が必要
evens = list(filter(lambda x: x % 2 == 0, values))
print(evens)    # [0, 2, 4, 6, 8, 10]
