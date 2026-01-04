"""スタティックメソッド"""

class Klass:
    @staticmethod  # スタティックメソッドには @staticmethod デコレータ
    def hello():   # 引数なし（selfもclsもなし）
        print("Hello")


Klass.hello()   # Hello

# インスタンスからもコールできる
klass = Klass()
klass.hello()   # Hello
