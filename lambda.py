"""
基本構文
lambda 引数: 戻り値
"""

# 通常の関数
def add(x, y):
    return x + y

# Lambda
add_lambda = lambda x, y: x + y

print(add(3, 5))        # 8
print(add_lambda(3, 5)) # 8
