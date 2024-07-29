import os

import pickle
from time import sleep

### FUNCTIONS ###
def display_title_bar():
	os.system('clear')

	print('\t*************************')
	print('\t ******  Crow v1  ****** ')
	print('\t*************************')
	print('_________________________________________')

def get_user_mode():

	print('\n[1] Uppercase')
	print('[2] Title Case')
	print('[3] Lowercase')
	print('[4] Recent Output')
	print('[q] Quit')

	return input('\nEnter mode: ')

def clean_up(inp):
	splitInput = inp.split('-')
	joinedInput = '/'.join(splitInput).replace(' / ','/').replace('/ ','/').replace(' /','/')
	return joinedInput

def upperCase():
	inputString = input('String you want to be uppercase: ')
	return inputString.upper()

def titleCase():
	inputString = input('String you want to be title-case: ')
	return inputString.title()

def lowerCase():
	inputString = input('String you want to be lowercase: ')
	return inputString.lower()

def load_recents():
	# load recents from file, puts them in a list 'recents'
	# if file doesn't exist, creates an empty list
	try:
		file_object = open('recent-output.pydata', 'rb')
		recents = pickle.load(file_object)
		file_object.close()
		return recents

	except Exception as e:
		print(e)
		return []

def get_recent_output():
	# dumps the output into a file, and prints
	try:
		file_object = open('recent-output.pydata', 'wb')
		pickle.dump(recents, file_object)
		file_object.close()

		print('\nRecent output: ')
		for recent in recents:
			print(recent)

	except Exception as e:
		print(e)
		print('\nRecent output could not be saved')

### SETUP ###
recents = load_recents()

choice = ''
outputString = ''
display_title_bar()

while choice != 'q':	
	choice = get_user_mode()
	display_title_bar()

	if choice == '1':
		outputString = clean_up(upperCase())
		recents.append(outputString)
		print(outputString)

	elif choice == '2':
		outputString = clean_up(titleCase())
		recents.append(outputString)
		print(outputString)

	elif choice == '3':
		outputString = clean_up(lowerCase())
		recents.append(outputString)
		print(outputString)

	elif choice == '4':
		get_recent_output()

	elif choice == 'q':
		get_recent_output()
		print('\nBye.')

	else:
		print('Please enter a valid choice.\n')
		sleep(2)