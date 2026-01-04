"""ゲッターとセッター"""

class Book:
    def __init__(self, raw_price):
        self.raw_price = raw_price
        self._discounts = 0   # プライベート変数

    @property                 # ゲッター
    def discounts(self):
        return self.discounts
    @discounts.setter         # セッター
    def discounts(self, value):
        if value < 0 or value > 100:
            raise ValueError('discounts must be between 0 and 100')
        self._discounts = value
    @property
    def price(self):
        multi = 100 - self._discounts
        return int(self.raw_price * multi / 100)

# Book1
book1 = Book(2000)
print(book1.price)  # 2000

# Book2
book2 = Book(3000)
book2.discounts = 10
print(book2.price)  # 2700

# Book3
book3 = Book(1000)
book3.discounts = 105   # ValueError: discounts must be between 0 and 100
