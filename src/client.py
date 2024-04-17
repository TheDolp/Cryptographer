from pathlib import PurePath
import os

class Client: 
	@staticmethod
	def get_num(first, last, lst):
		print("Choose from the list below")
		for i in range(first, last + 1):
			print(i, ') ' + lst[i - first], sep='')
		print(f'Enter a number from {first} to {last}')
		while True:
			num = input()
			if not num.isdigit():
				print("It is not a number")
				continue
			num = int(num)
			if num < first or last < num:
				print("Number should be different")
				continue
			return num

	@staticmethod
	def get_path():
		while True:
			file = input()
			file.rstrip()
			if not os.path.exists(file):
				print("Incorrect path")
				continue
			return file	
