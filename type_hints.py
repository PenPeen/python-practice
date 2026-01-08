"""
型ヒント

- 関数や変数はアノテーションを用いて型ヒント（引数と戻り値に対して型情報）を付けられる
- ただし静的型付け言語とは異なり実行時に型チェックがされる訳ではない。
    - 理解の補助
    - 静的解析ツール（mypy…）による型チェックの利用
    - IDEの精度向上

VSCodeでは、 `$ brew install mypy` + 拡張機能の Mypy Type Checker をインストールすることでエラー表示してくれるので便利
"""

def greet(name: str):
    print(f'Hello {name}')

# Hello Hiroto
greet('Hiroto')

# Hello 1（実行時に型チェックがされる訳ではないので実行は可能）
greet(1)
