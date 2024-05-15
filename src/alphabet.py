import string

class Alphabet: 
	def __init__(self):
		self.lowercase = []
		self.uppercase = []
		self.size = 0

	def is_in_alph(self, char):
		return char in self.lowercase or char in self.uppercase

	def get_number(self, char):
		return self.lowercase.index(char) if char in self.lowercase else self.uppercase.index(char)

	def get_lower_char(self, num):
		return self.lowercase[num]

	def get_upper_char(self, num):
		return self.uppercase[num]

	def move_symb(self, char, num):
		num = (self.get_number(char) + num) % self.size
		if char in self.lowercase:
			return self.lowercase[num]
		return self.uppercase[num]


class EnglishAlphabet(Alphabet):
	def __init__(self):
		self.lowercase = list(string.ascii_lowercase)
		self.uppercase = list(string.ascii_uppercase)
		self.size = len(self.lowercase)
		self.most_popular = 'e'

class RussianAlphabet(Alphabet):
	def __init__(self):
		self.lowercase = [chr(num) for num in range(ord('а'), ord('я')+1)]
		self.uppercase = [chr(num) for num in range(ord('A'), ord('Я')+1)]
		self.size = len(self.lowercase)
		self.most_popular = 'о'

