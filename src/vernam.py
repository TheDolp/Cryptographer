import random
from math import ceil

class VernamCode:
	only_simple_decode = True

	def __init__(self, alphabet_):
		self.alphabet = alphabet_

	def code_str(self, str_in, code):
		return ''.join([self.alphabet.move_symb(char, (self.alphabet.get_number(char) ^ self.alphabet.get_number(code_char)) 
				- self.alphabet.get_number(char)) if self.alphabet.is_in_alph(char) else char for char, code_char in zip(str_in, code)])

	def decode_str(self, str_in, code):
		return code_str(str_in, code)

	def code(self, path_in, path_out, path_code, generate_code = False):
		if generate_code:
			with open(path_code, 'w') as file_code:
				for _ in range(random.choice([i for i in range(1, 100)])):
					file_code.write(random.choice(self.alphabet.lowercase))
		with open(path_in, 'r') as file_in:
			with open(path_out, 'w') as file_out:
				with open(path_code, 'r') as file_code:
					code = file_code.read().rstrip()
					text = file_in.read()
					code = code * ceil(len(text) / len(code))
					file_out.write(self.code_str(text, code))

	def decode(self, path_in, path_out, path_code):
		code(path_in, path_out, path_code)

