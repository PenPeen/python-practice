"""クラス"""

# 定義
class Klass:
	# initialize
	def __init__(self, num, content):
		self.num = num
		self.content = content

	# instance method
	def output(self):
		print(f'{self.content}')

print(Klass)	# <class '__main__.Klass'>

# インスタンス化
klass = Klass(1, 'My Content')
print(isinstance(klass, Klass)) 	# True

# インスタンスメソッド
klass.output()				# My Content
print(klass.num)			# 1
print(klass.content)	# My Content

klass.num = 5
print(klass.num)			# 5
