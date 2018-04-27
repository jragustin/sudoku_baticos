'''
Creator: Andric Quinn S. Baticos
Section: CMSC 11 G-1L
Student Number: 2015-13764
Description: This file contains the functions for the board of the game - Sudoku
'''

#		START --- LIST OF IMPORTS
import os, random, time, pythondesign, checkfunctions
clear = lambda: os.system('clear')

#		START --- LIST OF FUNCTIONS

def board(difficulty):

	#	Initialization
	allCoordinates = loadBoard(difficulty)														#	--- loads a random board()
	tempCoordinates = allCoordinates.copy()														#	---	makes copy that can be edited
	changeableCoordinates = {}																	#	---	will hold all blanks (0)
	constantCoordinates = {}																	#	---	will hold all the fixed numbers

	#	Globalization - used to make the following initializations available to all functions
	global allCoordinates, tempCoordinates, changeableCoordinates, constantCoordinates

	#	Initialization For Printing Sudoku Menu
	if difficulty == 1:
		difficultyPrint = '\tEASY BOARD'
	elif difficulty == 2:
		difficultyPrint = '     AVERAGE BOARD'
	elif difficulty == 3:
		difficultyPrint = '    DIFFICULT BOARD'
	elif difficulty == 4:
		difficultyPrint = '     INSANE BOARD'

	for i in allCoordinates:
		if allCoordinates[i] != 0:
			constantCoordinates[i] = allCoordinates[i]
		else:
			changeableCoordinates[i] = allCoordinates[i]

	#	MINOR INITIALIZATIONS
	blankCoordinates = changeableCoordinates.copy()
	changedCoordinates = {}
	global blankCoordinates, changedCoordinates
	#	--------------------

	boardGame = True
	while boardGame:

		for i in blankCoordinates:
			if i in changedCoordinates:
				continue
			else:
				tempCoordinates[i] = ' '

		theGrid()
		print ("\t\t\t", difficultyPrint)
		print()
		print('\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

		#	--- PROGRAM EXECUTES THIS CODE IF THE BOARD IS COMPLETE
		done = checkfunctions.boardCheck(blankCoordinates, changedCoordinates)
		if done:
			clear()
			for i in range (0,20):
				print()
			print ("\t\t        CONGRATULATIONS!\n\t\t\t\tBOARD COMPLETE!")
			print ()
			input ("\t\t\t Press <ENTER> to EXIT")
			return 5
		#	--- END PROGRAM/GAME

		choice4 = pythondesign.boardMenu()
		if choice4 == '1':
			coordinate = coordinateInput_AddReplace()
			if coordinate == False:
				continue
			number = getNum()
			if number == 0:
				number = '_'
			elif number != False:
				row = coordinate[0].upper()
				column = coordinate[1]

				#	Assigns KEYS for checking of coordinate per box
				key = str(row) + str (column)
				if key == 'A1' or key == 'A2' or key == 'A3' or key == 'B1' or key == 'B2' or key == 'B3' or key == 'C1' or key == 'C2' or key == 'C3':
					key = 'X1'
				if key == 'A4' or key == 'A5' or key == 'A6' or key == 'B4' or key == 'B5' or key == 'B6' or key == 'C4' or key == 'C5' or key == 'C6':
					key = 'X2'
				if key == 'A7' or key == 'A8' or key == 'A9' or key == 'B7' or key == 'B8' or key == 'B9' or key == 'C7' or key == 'C8' or key == 'C9':
					key = 'X3'
				if key == 'D1' or key == 'D2' or key == 'D3' or key == 'E1' or key == 'E2' or key == 'E3' or key == 'F1' or key == 'F2' or key == 'F3':
					key = 'X4'
				if key == 'D4' or key == 'D5' or key == 'D6' or key == 'E4' or key == 'E5' or key == 'E6' or key == 'F4' or key == 'F5' or key == 'F6':
					key = 'X5'
				if key == 'D7' or key == 'D8' or key == 'D9' or key == 'E7' or key == 'E8' or key == 'E9' or key == 'F7' or key == 'F8' or key == 'F9':
					key = 'X6'
				if key == 'G1' or key == 'G2' or key == 'G3' or key == 'H1' or key == 'H2' or key == 'H3' or key == 'I1' or key == 'I2' or key == 'I3':
					key = 'X7'
				if key == 'G4' or key == 'G5' or key == 'G6' or key == 'H4' or key == 'H5' or key == 'H6' or key == 'I4' or key == 'I5' or key == 'I6':
					key = 'X8'
				if key == 'G7' or key == 'G8' or key == 'G9' or key == 'H7' or key == 'H8' or key == 'H9' or key == 'I7' or key == 'I8' or key == 'I9':
					key = 'X9'

				#	CHECKS THE NUMBER vertically, horizontally, and per-box
				rowchecking = checkfunctions.rowcheck(allCoordinates, tempCoordinates, str(column), str(row), number)
				columnchecking = checkfunctions.columncheck(allCoordinates, tempCoordinates, str(row), str(column), number)
				boxchecking = checkfunctions.boxcheck(allCoordinates, tempCoordinates, key, number, row, column)

				if rowchecking and columnchecking and boxchecking:
					for i in tempCoordinates:
						if coordinate == i:
							tempCoordinates[coordinate] = number
							changedCoordinates[coordinate] = number
				else:
					print ("\tUser Input Invalid.\n\tPlease wait...")
					time.sleep(2)
				
		if choice4 == '2':
			if changedCoordinates == {}:
				print()
				print("\tNo Removable Coordinates. Please wait...")
				time.sleep(2)
			else:
				coordinate = coordinateInput_Delete()
				if coordinate == False:
					continue
				else:
					for i in tempCoordinates:
						if coordinate == i:
							tempCoordinates[coordinate] = '_'
							del changedCoordinates[coordinate]

		elif choice4 == '3':
			resetBoard = True
			while resetBoard:
				theGrid()
				print ("\tAre you sure you want to reset the board? Y or N")
				print()
				choice8 = input ("\t>> ")
				if choice8 == "Y" or choice8 == "y":
					tempCoordinates = allCoordinates.copy()
					blankCoordinates = changeableCoordinates.copy()
					changedCoordinates = {}
					break
				elif choice8 == "N" or choice8 == "n":
					break
				else:
					continue

		elif choice4 == '5':
			return 5

		else:
			continue

def theGrid():

		# INITIALIZATIONS	
		ALPHA_COUNT = 0
		ALPHABET = "ABCDEFGHI"
		NUMBERS = "123456789"

		clear()
		print()
		print("\t", end ="   ")
		for i in NUMBERS:
			for j in range (0, 35):
				print (i, end = "     ")
				break
		print()
		print()

		#	The Grid (3X3 BOARD)

		print ("\t#", end = "")

		for i in range (0,53):						#	HEAD GRID
			print ("#", end = "")
		print ("#")

		for i in range (0,35):						#	GRID DOWNWARDS

			if i == 11:								#	FIRST INNER HORIZONTAL LINE - MAIN GRID
				print ("\t#", end = "")
				for j in range (0,53):
					print ("#", end = "")
				print ("#")

			elif i == 23:							#	SECOND INNER HORIZONTAL LINE - MAIN GRID
				print ("\t#", end = "")
				for j in range (0,53):
					print ("#", end = "")
				print ("#")

			else:									#	INSIDE-BOX (BLANK PRINTING)

				if i == 3 or i == 7 or i == 15 or i == 19 or i == 27 or i == 31:	#	FIRST INNER HORIZONTAL LINE - MINOR GRID (BASE)

					print ("\t#", end = "")

					for j in range (0,53):			
						if j == 17:					#	FIRST INNER HORIZONTAL LINE - MINOR GRID (INTERSECTING => FIRST INNER VERTICAL LINE - MAIN GRID)
							print ("#", end ="")	
						elif j == 35:				#	SECOND INNER HORIZONTAL LINE - MINOR GRID (INTERSECTING => FIRST INNER VERTICAL LINE - MAIN GRID)
							print ("#", end ="")
						elif j == 5 or j == 11 or j == 23 or j == 29 or j == 41 or j == 47:		#	FIRST INNER HORIZONTAL LINE - MINOR GRID (INTERSECTING => FIRST INNER VERTICAL LINE - MINOR GRID)
							print ("|", end ="")
						else:
							print ("-",end ="")		#	FIRST INNER HORIZONTAL LINE - MINOR GRID
					print("#")
			
				else:								#	ROWS-PER-COLUMN (BLANK SPACE BABY)
					print ("\t#", end = "")			

					for j in range (0,53):
						if j == 17:
							print ("#", end ="")	#	FIRST INNER VERTICAL LINE INTERSECTION - MAIN GRID
						elif j == 35:
							print ("#", end ="")	#	SECOND INNER VERTICAL LINE INTERSECTION - MAIN GRID

						# GRID VALUES - ROW A
						elif i == 1 and j == 2:
							print (tempCoordinates['A1'], end ="")
						elif i == 1 and j == 8:
							print (tempCoordinates['A2'], end ="")
						elif i == 1 and j == 14:
							print (tempCoordinates['A3'], end ="")
						elif i == 1 and j == 20:
							print (tempCoordinates['A4'], end ="")
						elif i == 1 and j == 26:
							print (tempCoordinates['A5'], end ="")
						elif i == 1 and j == 32:
							print (tempCoordinates['A6'], end ="")
						elif i == 1 and j == 38:
							print (tempCoordinates['A7'], end ="")
						elif i == 1 and j == 44:
							print (tempCoordinates['A8'], end ="")
						elif i == 1 and j == 50:
							print (tempCoordinates['A9'], end ="")

						# GRID VALUES - ROW B
						elif i == 5 and j == 2:
							print (tempCoordinates['B1'], end ="")
						elif i == 5 and j == 8:
							print (tempCoordinates['B2'], end ="")
						elif i == 5 and j == 14:
							print (tempCoordinates['B3'], end ="")
						elif i == 5 and j == 20:
							print (tempCoordinates['B4'], end ="")
						elif i == 5 and j == 26:
							print (tempCoordinates['B5'], end ="")
						elif i == 5 and j == 32:
							print (tempCoordinates['B6'], end ="")
						elif i == 5 and j == 38:
							print (tempCoordinates['B7'], end ="")
						elif i == 5 and j == 44:
							print (tempCoordinates['B8'], end ="")
						elif i == 5 and j == 50:
							print (tempCoordinates['B9'], end ="")

						# GRID VALUES - ROW C
						elif i == 9 and j == 2:
							print (tempCoordinates['C1'], end ="")
						elif i == 9 and j == 8:
							print (tempCoordinates['C2'], end ="")
						elif i == 9 and j == 14:
							print (tempCoordinates['C3'], end ="")
						elif i == 9 and j == 20:
							print (tempCoordinates['C4'], end ="")
						elif i == 9 and j == 26:
							print (tempCoordinates['C5'], end ="")
						elif i == 9 and j == 32:
							print (tempCoordinates['C6'], end ="")
						elif i == 9 and j == 38:
							print (tempCoordinates['C7'], end ="")
						elif i == 9 and j == 44:
							print (tempCoordinates['C8'], end ="")
						elif i == 9 and j == 50:
							print (tempCoordinates['C9'], end ="")

						# GRID VALUES - ROW D
						elif i == 13 and j == 2:
							print (tempCoordinates['D1'], end ="")
						elif i == 13 and j == 8:
							print (tempCoordinates['D2'], end ="")
						elif i == 13 and j == 14:
							print (tempCoordinates['D3'], end ="")
						elif i == 13 and j == 20:
							print (tempCoordinates['D4'], end ="")
						elif i == 13 and j == 26:
							print (tempCoordinates['D5'], end ="")
						elif i == 13 and j == 32:
							print (tempCoordinates['D6'], end ="")
						elif i == 13 and j == 38:
							print (tempCoordinates['D7'], end ="")
						elif i == 13 and j == 44:
							print (tempCoordinates['D8'], end ="")
						elif i == 13 and j == 50:
							print (tempCoordinates['D9'], end ="")

						# GRID VALUES - ROW E
						elif i == 17 and j == 2:
							print (tempCoordinates['E1'], end ="")
						elif i == 17 and j == 8:
							print (tempCoordinates['E2'], end ="")
						elif i == 17 and j == 14:
							print (tempCoordinates['E3'], end ="")
						elif i == 17 and j == 20:
							print (tempCoordinates['E4'], end ="")
						elif i == 17 and j == 26:
							print (tempCoordinates['E5'], end ="")
						elif i == 17 and j == 32:
							print (tempCoordinates['E6'], end ="")
						elif i == 17 and j == 38:
							print (tempCoordinates['E7'], end ="")
						elif i == 17 and j == 44:
							print (tempCoordinates['E8'], end ="")
						elif i == 17 and j == 50:
							print (tempCoordinates['E9'], end ="")

						# GRID VALUES - ROW F
						elif i == 21 and j == 2:
							print (tempCoordinates['F1'], end ="")
						elif i == 21 and j == 8:
							print (tempCoordinates['F2'], end ="")
						elif i == 21 and j == 14:
							print (tempCoordinates['F3'], end ="")
						elif i == 21 and j == 20:
							print (tempCoordinates['F4'], end ="")
						elif i == 21 and j == 26:
							print (tempCoordinates['F5'], end ="")
						elif i == 21 and j == 32:
							print (tempCoordinates['F6'], end ="")
						elif i == 21 and j == 38:
							print (tempCoordinates['F7'], end ="")
						elif i == 21 and j == 44:
							print (tempCoordinates['F8'], end ="")
						elif i == 21 and j == 50:
							print (tempCoordinates['F9'], end ="")

						# GRID VALUES - ROW G
						elif i == 25 and j == 2:
							print (tempCoordinates['G1'], end ="")
						elif i == 25 and j == 8:
							print (tempCoordinates['G2'], end ="")
						elif i == 25 and j == 14:
							print (tempCoordinates['G3'], end ="")
						elif i == 25 and j == 20:
							print (tempCoordinates['G4'], end ="")
						elif i == 25 and j == 26:
							print (tempCoordinates['G5'], end ="")
						elif i == 25 and j == 32:
							print (tempCoordinates['G6'], end ="")
						elif i == 25 and j == 38:
							print (tempCoordinates['G7'], end ="")
						elif i == 25 and j == 44:
							print (tempCoordinates['G8'], end ="")
						elif i == 25 and j == 50:
							print (tempCoordinates['G9'], end ="")

						# GRID VALUES - ROW H
						elif i == 29 and j == 2:
							print (tempCoordinates['H1'], end ="")
						elif i == 29 and j == 8:
							print (tempCoordinates['H2'], end ="")
						elif i == 29 and j == 14:
							print (tempCoordinates['H3'], end ="")
						elif i == 29 and j == 20:
							print (tempCoordinates['H4'], end ="")
						elif i == 29 and j == 26:
							print (tempCoordinates['H5'], end ="")
						elif i == 29 and j == 32:
							print (tempCoordinates['H6'], end ="")
						elif i == 29 and j == 38:
							print (tempCoordinates['H7'], end ="")
						elif i == 29 and j == 44:
							print (tempCoordinates['H8'], end ="")
						elif i == 29 and j == 50:
							print (tempCoordinates['H9'], end ="")

						# GRID VALUES - ROW I
						elif i == 33 and j == 2:
							print (tempCoordinates['I1'], end ="")
						elif i == 33 and j == 8:
							print (tempCoordinates['I2'], end ="")
						elif i == 33 and j == 14:
							print (tempCoordinates['I3'], end ="")
						elif i == 33 and j == 20:
							print (tempCoordinates['I4'], end ="")
						elif i == 33 and j == 26:
							print (tempCoordinates['I5'], end ="")
						elif i == 33 and j == 32:
							print (tempCoordinates['I6'], end ="")
						elif i == 33 and j == 38:
							print (tempCoordinates['I7'], end ="")
						elif i == 33 and j == 44:
							print (tempCoordinates['I8'], end ="")
						elif i == 33 and j == 50:
							print (tempCoordinates['I9'], end ="")

						elif j == 5 or j == 11 or j == 23 or j == 29 or j == 41 or j == 47:		#	INTERSECTION: VERTICAL MINOR GRID
							print ("|", end ="")
						else:																	#	BLANK SPACE BABY
							print (" ",end ="")

					if i == 1 or i == 5 or i == 9 or i == 13 or i == 17 or i == 21 or i == 25 or i == 29 or i == 33:
						print("#   ", end = ALPHABET[ALPHA_COUNT])								#	VERTICAL COORDINATE PRINTING
						print()
						ALPHA_COUNT = ALPHA_COUNT + 1
						if ALPHA_COUNT == 9:
							ALPHA_COUNT = 0
					else:
						print("#")

		print ("\t#", end = "")
		for i in range (0,53):
			print ("#", end = "")
		print ("#")
		print()

		#	END PRINTING OF THE GRID

#	---------------------------------------------------------------------------------------------------------------		LOADING function

def loadBoard(difficulty):

	#	Initialization
	ALPHANUM_COUNT = 0
	NUMBER_COUNT = 0
	ALPHABET = "ABCDEFGHI"
	NUMBERS = "123456789"
	allCoordinates = {}
	defaultCoordinates = []
	fixedXYCoordinates = []

	for i in ALPHABET:
		for j in NUMBERS:
			keyname = i + j
			defaultCoordinates.append(keyname)
			fixedXYCoordinates.append(keyname)

	#	DIFFICULTY IDENTIFIER w/ INITIALIZATIONS

	if difficulty == 1:
		randomizer = random.randint(1,6)
		difficultyString = 'easyBoard/' + str(randomizer) + '.csv'
		fileReader = open (difficultyString, 'r')
	elif difficulty == 2:
		randomizer = random.randint(1,6)
		difficultyString = 'mediumBoard/' + str(randomizer) + '.csv'
		fileReader = open (difficultyString, 'r')
	elif difficulty == 3:
		randomizer = random.randint(1,6)
		difficultyString = 'difficultBoard/' + str(randomizer) + '.csv'
		fileReader = open (difficultyString, 'r')
	elif difficulty == 4:
		randomizer = random.randint(1,3)
		difficultyString = 'insaneBoard/' + str(randomizer) + '.csv'
		fileReader = open (difficultyString, 'r')

	for line in fileReader:
		line = line [:-1]
		A1,A2,A3,A4,A5,A6,A7,A8,A9,B1,B2,B3,B4,B5,B6,B7,B8,B9,C1,C2,C3,C4,C5,C6,C7,C8,C9,D1,D2,D3,D4,D5,D6,D7,D8,D9,E1,E2,E3,E4,E5,E6,E7,E8,E9,F1,F2,F3,F4,F5,F6,F7,F8,F9,G1,G2,G3,G4,G5,G6,G7,G8,G9,H1,H2,H3,H4,H5,H6,H7,H8,H9,I1,I2,I3,I4,I5,I6,I7,I8,I9 = line.split(",")
		allCoordinates = {'A1':int(A1),'A2':int(A2),'A3':int(A3),'A4':int(A4),'A5':int(A5),'A6':int(A6),'A7':int(A7),'A8':int(A8),'A9':int(A9),'B1':int(B1),'B2':int(B2),'B3':int(B3),'B4':int(B4),'B5':int(B5),'B6':int(B6),'B7':int(B7),'B8':int(B8),'B9':int(B9),'C1':int(C1),'C2':int(C2),'C3':int(C3),'C4':int(C4),'C5':int(C5),'C6':int(C6),'C7':int(C7),'C8':int(C8),'C9':int(C9),'D1':int(D1),'D2':int(D2),'D3':int(D3),'D4':int(D4),'D5':int(D5),'D6':int(D6),'D7':int(D7),'D8':int(D8),'D9':int(D9),'E1':int(E1),'E2':int(E2),'E3':int(E3),'E4':int(E4),'E5':int(E5),'E6':int(E6),'E7':int(E7),'E8':int(E8),'E9':int(E9),'F1':int(F1),'F2':int(F2),'F3':int(F3),'F4':int(F4),'F5':int(F5),'F6':int(F6),'F7':int(F7),'F8':int(F8),'F9':int(F9),'G1':int(G1),'G2':int(G2),'G3':int(G3),'G4':int(G4),'G5':int(G5),'G6':int(G6),'G7':int(G7),'G8':int(G8),'G9':int(G9),'H1':int(H1),'H2':int(H2),'H3':int(H3),'H4':int(H4),'H5':int(H5),'H6':int(H6),'H7':int(H7),'H8':int(H8),'H9':int(H9),'I1':int(I1),'I2':int(I2),'I3':int(I3),'I4':int(I4),'I5':int(I5),'I6':int(I6),'I7':int(I7),'I8':int(I8),'I9':int(I9)} 
	fileReader.close()
	return allCoordinates

#	-------------------------------------------------------------------------------------------------------------MINOR LIST (COORDINATE FUNCTIONS)

def coordinateInput_Delete():
	inputCoordinate = True
	while inputCoordinate:
		clear()
		print()
		theGrid()
		print('\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
		print()
		print("\tREMOVABLE COORDINATES:")
		print()
		print("\t", end ="")
		count = 0
		for i in changedCoordinates:
			count = count + 1
			print(i, end = "| ")
			if count % 14 == 0:
				print ("\n\t", end = "")
		print()
		print()
		print('\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
		choice5 = input ("\tEnter Coordinate To Be Deleted\n\t(Format:A1): ")
		if choice5.upper() in changedCoordinates:
			choice5 = choice5.upper()
			return choice5
		else:
			print ("\tUser Input Invalid!")
			for i in constantCoordinates:
				if str(choice5.upper()) == str(i):
					print ("\tNumber Cannot Be Changed.")
			choice6 = cancel_Deleting()
			if choice6:
				continue
			else:
				return False

def coordinateInput_AddReplace():
	inputCoordinate = True
	while inputCoordinate:
		clear()
		print()
		theGrid()
		addPrint()
		choice7 = input ("\tEnter Coordinate To Be Replaced\n\t(Format:A1): ")
		if choice7.upper() in changeableCoordinates:
			choice7 = choice7.upper()
			return choice7
		else:
			print ("\tUser Input Invalid!")
			choice7 = cancel_AddingReplacing()
			if choice7:
				continue
			else:
				return 0

def cancel_Deleting():
	out = True
	while out:
		choice6 = input ("\tDo you want to continue deleting? Y or N\n\t")
		if choice6 == 'y' or choice6 == 'Y':
			return True
		elif choice6 == 'n' or choice6 == 'N':
			return False
		else:
			clear()
			theGrid()
			print('\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
			print()
			print("\tNOMINATED COORDINATES FOR DELETION:")
			print()
			print("\t", end ="")
			count = 0
			for i in changedCoordinates:
				count = count + 1
				print(i, end = "| ")
				if count % 14 == 0:
					print ("\n\t", end = "")
			print()
			print()
			print('\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
			decision = cancel_Deleting()
			return decision

def cancel_AddingReplacing():
	out = True
	while out:
		choice6 = input ("\tDo you want to continue adding/replacing? Y or N\n\t")
		if choice6 == 'y' or choice6 == 'Y':
			return True
		elif choice6 == 'n' or choice6 == 'N':
			return False
		else:
			clear()
			theGrid()
			addPrint()
			decision = cancel_AddingReplacing()
			return decision

def addPrint():
	print('\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
	print()
	print("\tBLANK COORDINATES:")
	print()
	print("\t", end ="")
	count = 0
	for i in blankCoordinates:
		if i in changedCoordinates:
			continue
		count = count + 1
		print(i, end = "| ")
		if count % 14 == 0:
			print ("\n\t", end = "")
	print()
	print()
	print('\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
	print()
	print("\tCHANGED COORDINATES:")
	print()
	print("\t", end ="")
	count = 0
	for i in changedCoordinates:
		count = count + 1
		print(i, end = "| ")
		if count % 14 == 0:
			print ("\n\t", end = "")
	print()
	print()
	print('\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

def getNum():
	number = input ("\tEnter Number: ")
	if number.isdigit():
		if int(number) == 0:
			return 0
		if int(number) > 0 and int(number) <= 9:
			return int(number)
	elif number.isdigit() == False:
		return False
	else:
		return 0

		#----------------------------------------------------------------------------------------------END OF MINOR LIST (COORDINATE FUNCTIONS)

#		END --- END OF FUNCTIONS

#========================================================TEST CANVAS FOR CODES================================================================#
'''
#	TESTING FOR LOAD GAME
def loadGame():
	fileReader = open ("savedGame.csv", "r")
	for line in fileReader:
		line = line [:-1]
		A1,A2,A3,A4,A5,A6,A7,A8,A9,B1,B2,B3,B4,B5,B6,B7,B8,B9,C1,C2,C3,C4,C5,C6,C7,C8,C9,D1,D2,D3,D4,D5,D6,D7,D8,D9,E1,E2,E3,E4,E5,E6,E7,E8,E9,F1,F2,F3,F4,F5,F6,F7,F8,F9,G1,G2,G3,G4,G5,G6,G7,G8,G9,H1,H2,H3,H4,H5,H6,H7,H8,H9,I1,I2,I3,I4,I5,I6,I7,I8,I9 = line.split(",")
'''