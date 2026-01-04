"""クラスの継承"""

class Parent:
    def hello(self):
        print("hello")

class Children(Parent):
    def greet(self):
        print("good morning")

children = Children()
children.hello()
children.greet()
