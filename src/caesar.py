import random

class CaesarCode:
	only_simple_decode = False

	def __init__(self, alphabet_):
		self.alphabet = alphabet_

	def code_str(self, str_in, code):
		return ''.join([self.alphabet.move_symb(char, self.alphabet.get_number(code[0])) 
						if self.alphabet.is_in_alph(char) else char for char in str_in])

	def decode_str(self, str_in, code):
		return ''.join([self.alphabet.move_symb(char, -self.alphabet.get_number(code[0])) 
						if self.alphabet.is_in_alph(char) else char for char in str_in])

	def code(self, path_in, path_out, path_code, generate_code = False):
		if generate_code:
			with open(path_code, 'w') as file_code:
				file_code.write(random.choice(self.alphabet.lowercase))
		with open(path_in, 'r') as file_in:
			with open(path_out, 'w') as file_out:
				with open(path_code, 'r') as file_code:
					file_out.write(self.code_str(file_in.read(), file_code.read()))

	def decode(self, path_in, path_out, path_code):
		with open(path_in, 'r') as file_in:
			with open(path_out, 'w') as file_out:
				with open(path_code, 'r') as file_code:
					file_out.write(self.decode_str(file_in.read(), file_code.read()))

	def auto_decode(self, path_in, path_out):
		with open(path_in, 'r') as file_in:
			cnt = [0 for _ in range(self.alphabet.size)]
			text = file_in.read()
			for char in text:
				if self.alphabet.is_in_alph(char):
					cnt[self.alphabet.get_number(char)] += 1
			most_popular = 0
			for i in range(1, len(cnt)):
				if cnt[i] > cnt[most_popular]:
					most_popular = i
			code = self.alphabet.get_lower_char((most_popular - self.alphabet.get_number(self.alphabet.most_popular)) % self.alphabet.size)
			with open(path_out, 'w') as file_out:
					file_out.write(self.decode_str(text, code))
