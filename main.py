from src.client import Client
from src.communicator import Communicator

def print_information():
	print("\nI can use three types of code: Caesar, Vernam and Vigenere.")
	print("For every code type I can code and decode files.")
	print("Special for Caesar I can decode text without code-letter! But it does not work for small files.\n") 

print("Hello, world!\nI'm here to code your files.")
while True:
	print("\nWhat do you want?")
	var = ["help", "new", "exit"][Client.get_num(1, 3, ["I want to know more about this program", "I want to start work with new code", "Exit"]) - 1]
	match var:
		case "help": 
			print_information()
		case "new": 
			Communicator.start_code()
		case "exit": 
			break

print("Bye!")	
