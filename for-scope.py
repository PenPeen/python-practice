"""
for文内の変数スコープの確認
"""

items = ["apple", "orange"]
for m in items:
    print(m) # apple, orange

# 変数`m`はブロック終了後も参照可能
print(m)    # orange
