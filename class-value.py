"""クラス変数"""

class Klass:
    title = "Hello World"

# クラス変数の参照
print(Klass.title)    # Hello World

# インスタンス変数からも参照可能
klass = Klass()
print(klass.title)    # Hello World

# [注意点] クラス変数の更新はクラス経由で行う必要がある。
klass.title = "New Title"
print(klass.title)    # New Title
print(Klass.title)    # Hello World

Klass.title = "New Title"
print(klass.title)    # New Title
print(Klass.title)    # New Title
