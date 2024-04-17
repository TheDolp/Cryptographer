from alphabet import RussianAlphabet, EnglishAlphabet
from caesar import CaesarCode
from vigenere import VigenereCode
from communicator import Communicator
from client import Client

def print_information():
	print("i will write information")

print("Hello, world!\nI'm here to code your files.")
while True:
	print("What do you want?")
	var = ["help", "new", "exit"][Client.get_num(1, 3, ["I want to know more this program", "I want to start work with new code", "Exit"]) - 1]
	match var:
		case "help": 
			print_information()
		case "new": 
			Communicator.start_code()
		case "exit": 
			break

print("Bye!")	