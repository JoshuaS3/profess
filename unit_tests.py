#!/usr/bin/env python3

import sys
import os

def error(message):
	print("ERROR: " + message)
	exit(1)

def main(directory):
	files = os.listdir(directory)
	for file in files:
		if file.endswith(".py"):
			print(file)
			print("="*len(file))
			try:
				exec(open(os.path.join(directory, file)).read())
			except Exception as e:
				print(e)
			print()
			print()

if __name__ == "__main__":
	args = sys.argv
	if len(args) == 1:
		error("At least one argument required")
	directory = args[-1]
	main(directory)
