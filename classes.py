class About_me:
	def __init__(self, name, book, movie, height, food):
		self.name = name
		self.book = book
		self.movie = movie
		self.height = height
		self.food = food
	def get_name(self):
		return self.name 
	def get_book(self):
		return self.book
	def get_movie(self):
		return self.movie
	def get_height(self):
		return self.height
	def get_food(self):
		return self.food

Me = About_me('Debbie', 'Americanah', 'Same kind of different', 168, 'Spaghetti')
print(Me.get_food())
