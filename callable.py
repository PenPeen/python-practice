"""
callble()
オブジェクトが「呼び出せる」かどうかをチェックする関数。
"""

x = 10
print(callable(x))            # False

def my_function():
    pass

print(callable(my_function))  # True
