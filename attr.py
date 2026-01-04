"""
- `hasattr`: オブジェクトの属性有無を判定する
- `getattr`: オブジェクトの属性を取得
- `setattr`: オブジェクトの属性を設定
- `delattr`: オブジェクトの属性を削除
"""

class Klass:
    def __init__(self, name):
        self.name = name

# hasattr
klass = Klass('Taro')
print(hasattr(klass, 'name'))   # True
print(hasattr(klass, 'age'))    # False

# getattr
print(getattr(klass, 'name'))   # Taro
try:
    # AttributeError: 'Klass' object has no attribute 'age'
    print(getattr(klass, 'age'))
except AttributeError:
    print('ageは存在しません。')

# setattr
setattr(klass, 'name', 'Takuya')
print(getattr(klass, 'name'))   # Takuya
setattr(klass, 'age', 18)
print(getattr(klass, 'age'))    # 18

# delattr
delattr(klass, 'age')
try:
    # AttributeError: 'Klass' object has no attribute 'age'
    print(getattr(klass, 'age'))
except AttributeError:
    print('ageは存在しません。')
