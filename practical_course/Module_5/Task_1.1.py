class StringVar:
	def __init__(self, string): # создание строки объект
		self.string = string
	
	def set(self, changeString): # изменение строки
		self.string = changeString
	
	def get(self): # вывод строки
		return self.string


a = StringVar(input('String: '))
print(a.get()) # вывод настроящей строки

a.set(input('What to change? ')) # изменение строки
print(a.get())
