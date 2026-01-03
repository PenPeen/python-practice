"""
### 数値同士の演算

- 複素数型を含む演算は結果も複素数型になる
- 複素数型を含まず浮動小数点型を含む演算は、結果も浮動小数点型となる
- 複素数型も浮動小数点型も含まない演算は結果は整数型になる

→ 演算結果は、含まれる数値の中で最も「上位」の型になる

>>> 1 + 2
3
>>> 1 - 2.0
-1.0
>>> 1 * 2j
2j
>>> 1 / 2
0.5
>>> 1 / 0
Traceback (most recent call last):
  File "<python-input-31>", line 1, in <module>
    1 / 0
    ~~^~~
ZeroDivisionError: division by zero
"""
