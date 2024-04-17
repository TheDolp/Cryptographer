from client import Client
from alphabet import RussianAlphabet, EnglishAlphabet
from caesar import CaesarCode
from vigenere import VigenereCode
from vernam import VernamCode
from client import Client

class Communicator: 

	@staticmethod
	def start_code():
		print("What language do you use in files?")
		alphabet = [EnglishAlphabet(), RussianAlphabet()][Client.get_num(1, 2, ["English", "Russian"]) - 1]
		print("What code we are working with?")
		code = [CaesarCode, VigenereCode, VernamCode][Client.get_num(1, 3, ["Caesar", "Vigenere", "Vernam"]) - 1]
		code = code(alphabet)
		print("Do you want to code or to decode?")
		[Communicator.new_code, Communicator.new_decode][Client.get_num(1, 2, ["Code", "Decode"]) - 1](code)

	@staticmethod
	def new_code(code):
		print("Give me path to the input file.")
		file_in = Client.get_path()
		print("Give me path to the output file.")
		file_out = Client.get_path()
		print("Do you want me to generate code?")
		generate_code = [False, True][Client.get_num(0, 1, ["No, I have it", "Yes"])]
		print("Give me path to the code file.")
		file_code = Client.get_path()
		code.code(file_in, file_out, file_code, generate_code)

	@staticmethod
	def simple_decode(code):
		print("Give me path to the input file.")
		file_in = Client.get_path()
		print("Give me path to the output file.")
		file_out = Client.get_path()
		print("Give me path to the code file.")
		file_code = Client.get_path()
		code.decode(file_in, file_out, file_code)

	@staticmethod
	def auto_decode(code):
		print("Give me path to the input file.")
		file_in = Client.get_path()
		print("Give me path to the output file.")
		file_out = Client.get_path()
		code.auto_decode(file_in, file_out)

	@staticmethod
	def new_decode(code):
		if code.only_simple_decode:
			simple_decode(code)
			return
		print("Basic decode or auto-decode?")
		[Communicator.simple_decode, Communicator.auto_decode][Client.get_num(1, 2, ["Basic", "Auto"]) - 1](code)


