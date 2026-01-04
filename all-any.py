"""
all, any
イテラブルの要素を真偽値で評価

基本構文
all(イテラブル)  # すべてが True なら True
any(イテラブル)  # 1つでも True なら True
"""

# all()
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False

# any()
print(any([False, False, True]))  # True
print(any([False, False, False])) # False
