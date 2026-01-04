"""
zip

複数のイテラブル(リスト、タプルなど)を並行して処理する組み込み関数
"""

# 基本
names = ['Alice', 'Bob', 'Carol']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}歳")
"""
Alice: 25歳
Bob: 30歳
Carol: 35歳
"""

# Distの作成
keys = ['name', 'age', 'city']
values = ['田中', 28, '東京']
pair = dict(zip(keys, values))
print(pair)
"""
{'name': '田中', 'age': 28, 'city': '東京'}
"""
