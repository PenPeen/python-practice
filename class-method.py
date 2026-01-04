"""クラスメソッド"""

class Klass:
    @classmethod  # クラスメソッドには @classmethod デコレータをつける
    def hello(cls):
      print("Hello")


Klass.hello()   # Hello

# インスタンスからもコールできる。
klass = Klass()
klass.hello()
