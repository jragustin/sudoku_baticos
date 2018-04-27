'''
Creator: Andric Quinn S. Baticos
Section: CMSC 11 G-1L
Student Number: 2015-13764
Description: This file contains the mother file for the game - Sudoku.
'''

import boardfunctions, pythondesign, time, os
clear = lambda: os.system('clear')

#		Initializations

game = True
mainMenuCount = 0
difficultyCount =0

#	START

while game:

	if mainMenuCount == 0:

		mainMenuCount = mainMenuCount + 1
		choice1 = pythondesign.menu1()	

		if choice1 == '1':

			decision = True
			while decision:

				choice2 = pythondesign.continueGame()

				if choice2 == '1':

					difficulty = True
					while difficulty:

						#	--- LOADS DIFFICULTY WITH SLEEP ("else statement" - removed sleep because of the same reason: irritating.)
						if difficultyCount == 0:
							difficultyCount = difficultyCount + 1
							choice3 = pythondesign.difficulty1()
						else:
							choice3 = pythondesign.difficulty2()
						#	---	end loading

						if choice3.isdigit():

							choice3 = int(choice3)

							if choice3 > 0 and choice3 <= 4:
								board = True
								choice3 = boardfunctions.board(choice3)

							if choice3 == 5:
								break

							else:
								continue

						else:
							continue

				elif choice2 == '3':
					break

		elif choice1 == '2':
			pythondesign.howToPlay()

		elif choice1 == '3':
			pythondesign.aboutTheGame()
			
		elif choice1 == '4':
			clear()
			exit()

	#	Used the same code from the "if" statement
	#	Difference: The printing on the first loop uses the time.sleep on each menu. Some beta testers
	#	found it very irritating that the program uses the "sleep" effect every time they go back to the menu.

	else:
		choice1 = pythondesign.menu2()
		if choice1 == '1':
			decision = True
			while decision:
				choice2 = pythondesign.continueGame()
				if choice2 == '1':
					difficulty = True
					while difficulty:
						if difficultyCount == 0:
							difficultyCount = difficultyCount + 1
							choice3 = pythondesign.difficulty1()
						else:
							choice3 = pythondesign.difficulty2()
						if choice3.isdigit():
							choice3 = int(choice3)
							if choice3 > 0 and choice3 <= 4:
								choice3 = boardfunctions.board(choice3)
							if choice3 == 5:
								break
							else:
								continue
						else:
							continue
				elif choice2 == '3':
					break
		elif choice1 == '2':
			pythondesign.howToPlay()
		elif choice1 == '3':
			pythondesign.aboutTheGame()
		elif choice1 == '4':
			clear()
			exit()

#	END