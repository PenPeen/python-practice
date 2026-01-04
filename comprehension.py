"""内包表記"""

# 基本構文
# [リストの要素 for 変数 in イテラブルオブジェクト]
strs = [str(v) for v in range(10)]
print(strs) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 内包表記を活用して偶数のListを作成する
evens = [v for v in range(10) if v % 2 == 0]
print(evens) # [0, 2, 4, 6, 8]

# 内包表記でDictを作成する
dict = {str(v): v for v in range(10)}
print(dict) # {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
