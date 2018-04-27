'''
Creator: Andric Quinn S. Baticos
Section: CMSC 11 G-1L
Student Number: 2015-13764
Description: This file contains the functions for checking the coordinate inputs in the game - Sudoku
'''

#		START --- LIST OF IMPORTS
import os, time
clear = lambda: os.system('clear')

#		START --- LIST OF FUNCTIONS

def rowcheck(allCoordinates, tempCoordinates, column, row, number):

	rows = {}
	rowvalues = []

	#	GROUPING - ROW
	rows['A'] = {'1':tempCoordinates['A1'],'2':tempCoordinates['A2'],'3':tempCoordinates['A3'],'4':tempCoordinates['A4'],'5':tempCoordinates['A5'],'6':tempCoordinates['A6'],'7':tempCoordinates['A7'],'8':tempCoordinates['A8'],'9':tempCoordinates['A9']}
	rows['B'] = {'1':tempCoordinates['B1'],'2':tempCoordinates['B2'],'3':tempCoordinates['B3'],'4':tempCoordinates['B4'],'5':tempCoordinates['B5'],'6':tempCoordinates['B6'],'7':tempCoordinates['B7'],'8':tempCoordinates['B8'],'9':tempCoordinates['B9']}
	rows['C'] = {'1':tempCoordinates['C1'],'2':tempCoordinates['C2'],'3':tempCoordinates['C3'],'4':tempCoordinates['C4'],'5':tempCoordinates['C5'],'6':tempCoordinates['C6'],'7':tempCoordinates['C7'],'8':tempCoordinates['C8'],'9':tempCoordinates['C9']}
	rows['D'] = {'1':tempCoordinates['D1'],'2':tempCoordinates['D2'],'3':tempCoordinates['D3'],'4':tempCoordinates['D4'],'5':tempCoordinates['D5'],'6':tempCoordinates['D6'],'7':tempCoordinates['D7'],'8':tempCoordinates['D8'],'9':tempCoordinates['D9']}
	rows['E'] = {'1':tempCoordinates['E1'],'2':tempCoordinates['E2'],'3':tempCoordinates['E3'],'4':tempCoordinates['E4'],'5':tempCoordinates['E5'],'6':tempCoordinates['E6'],'7':tempCoordinates['E7'],'8':tempCoordinates['E8'],'9':tempCoordinates['E9']}
	rows['F'] = {'1':tempCoordinates['F1'],'2':tempCoordinates['F2'],'3':tempCoordinates['F3'],'4':tempCoordinates['F4'],'5':tempCoordinates['F5'],'6':tempCoordinates['F6'],'7':tempCoordinates['F7'],'8':tempCoordinates['F8'],'9':tempCoordinates['F9']}
	rows['G'] = {'1':tempCoordinates['G1'],'2':tempCoordinates['G2'],'3':tempCoordinates['G3'],'4':tempCoordinates['G4'],'5':tempCoordinates['G5'],'6':tempCoordinates['G6'],'7':tempCoordinates['G7'],'8':tempCoordinates['G8'],'9':tempCoordinates['G9']}
	rows['H'] = {'1':tempCoordinates['H1'],'2':tempCoordinates['H2'],'3':tempCoordinates['H3'],'4':tempCoordinates['H4'],'5':tempCoordinates['H5'],'6':tempCoordinates['H6'],'7':tempCoordinates['H7'],'8':tempCoordinates['H8'],'9':tempCoordinates['H9']}
	rows['I'] = {'1':tempCoordinates['I1'],'2':tempCoordinates['I2'],'3':tempCoordinates['I3'],'4':tempCoordinates['I4'],'5':tempCoordinates['I5'],'6':tempCoordinates['I6'],'7':tempCoordinates['I7'],'8':tempCoordinates['I8'],'9':tempCoordinates['I9']}

	for a in rows:
		if row == a:
			for b in rows[a]:
				if b == column:
					for c in rows[a].values():
						rowvalues.append(c)
					for d in range (0, len(rowvalues)):
						if rowvalues[d] == number:
							print ("\tThere exist that number in this row.")
							return False
					return True

def columncheck(allCoordinates, tempCoordinates, row, column, number):

	columns = {}
	columnvalues = []

	#	GROUPING - COLUMN
	columns['1'] = {'A':tempCoordinates['A1'],'B':tempCoordinates['B1'],'C':tempCoordinates['C1'],'D':tempCoordinates['D1'],'E':tempCoordinates['E1'],'F':tempCoordinates['F1'],'G':tempCoordinates['G1'],'H':tempCoordinates['H1'],'I':tempCoordinates['I1']}
	columns['2'] = {'A':tempCoordinates['A2'],'B':tempCoordinates['B2'],'C':tempCoordinates['C2'],'D':tempCoordinates['D2'],'E':tempCoordinates['E2'],'F':tempCoordinates['F2'],'G':tempCoordinates['G2'],'H':tempCoordinates['H2'],'I':tempCoordinates['I2']}
	columns['3'] = {'A':tempCoordinates['A3'],'B':tempCoordinates['B3'],'C':tempCoordinates['C3'],'D':tempCoordinates['D3'],'E':tempCoordinates['E3'],'F':tempCoordinates['F3'],'G':tempCoordinates['G3'],'H':tempCoordinates['H3'],'I':tempCoordinates['I3']}
	columns['4'] = {'A':tempCoordinates['A4'],'B':tempCoordinates['B4'],'C':tempCoordinates['C4'],'D':tempCoordinates['D4'],'E':tempCoordinates['E4'],'F':tempCoordinates['F4'],'G':tempCoordinates['G4'],'H':tempCoordinates['H4'],'I':tempCoordinates['I4']}
	columns['5'] = {'A':tempCoordinates['A5'],'B':tempCoordinates['B5'],'C':tempCoordinates['C5'],'D':tempCoordinates['D5'],'E':tempCoordinates['E5'],'F':tempCoordinates['F5'],'G':tempCoordinates['G5'],'H':tempCoordinates['H5'],'I':tempCoordinates['I5']}
	columns['6'] = {'A':tempCoordinates['A6'],'B':tempCoordinates['B6'],'C':tempCoordinates['C6'],'D':tempCoordinates['D6'],'E':tempCoordinates['E6'],'F':tempCoordinates['F6'],'G':tempCoordinates['G6'],'H':tempCoordinates['H6'],'I':tempCoordinates['I6']}
	columns['7'] = {'A':tempCoordinates['A7'],'B':tempCoordinates['B7'],'C':tempCoordinates['C7'],'D':tempCoordinates['D7'],'E':tempCoordinates['E7'],'F':tempCoordinates['F7'],'G':tempCoordinates['G7'],'H':tempCoordinates['H7'],'I':tempCoordinates['I7']}
	columns['8'] = {'A':tempCoordinates['A8'],'B':tempCoordinates['B8'],'C':tempCoordinates['C8'],'D':tempCoordinates['D8'],'E':tempCoordinates['E8'],'F':tempCoordinates['F8'],'G':tempCoordinates['G8'],'H':tempCoordinates['A8'],'I':tempCoordinates['I8']}
	columns['9'] = {'A':tempCoordinates['A9'],'B':tempCoordinates['B9'],'C':tempCoordinates['C9'],'D':tempCoordinates['D9'],'E':tempCoordinates['E9'],'F':tempCoordinates['F9'],'G':tempCoordinates['G9'],'H':tempCoordinates['H9'],'I':tempCoordinates['I9']}

	for x in columns:
		if column == x:
			for y in columns[x]:
				if y == row:
					for z in columns[x].values():
						columnvalues.append(z)
					for w in range (0, len(columnvalues)):
						if columnvalues[w] == number:
							print ("\tThere exist that number in this column.")
							return False
					return True

def boxcheck (allCoordinates, tempCoordinates, key, number, row, column):

	boxes = {}
	boxvalues = []
	coordinateValue = str(row) + str (column)

	# GROUPING - BOX
	boxes['X1'] = {'A1':tempCoordinates['A1'],'A2':tempCoordinates['A2'],'A3':tempCoordinates['A3'],'B1':tempCoordinates['B1'],'B2':tempCoordinates['B2'],'B3':tempCoordinates['B3'],'C1':tempCoordinates['C1'],'C2':tempCoordinates['C2'],'C3':tempCoordinates['C3']}
	boxes['X2'] = {'A4':tempCoordinates['A4'],'A5':tempCoordinates['A5'],'A6':tempCoordinates['A6'],'B4':tempCoordinates['B4'],'B5':tempCoordinates['B5'],'B6':tempCoordinates['B6'],'C4':tempCoordinates['C4'],'C5':tempCoordinates['C5'],'C6':tempCoordinates['C6']}
	boxes['X3'] = {'A7':tempCoordinates['A7'],'A8':tempCoordinates['A8'],'A9':tempCoordinates['A9'],'B7':tempCoordinates['B7'],'B8':tempCoordinates['B8'],'B9':tempCoordinates['B9'],'C7':tempCoordinates['C7'],'C8':tempCoordinates['C8'],'C9':tempCoordinates['C9']}
	boxes['X4'] = {'D1':tempCoordinates['D1'],'D2':tempCoordinates['D2'],'D3':tempCoordinates['D3'],'E1':tempCoordinates['E1'],'E2':tempCoordinates['E2'],'E3':tempCoordinates['E3'],'F1':tempCoordinates['F1'],'F2':tempCoordinates['F2'],'F3':tempCoordinates['F3']}
	boxes['X5'] = {'D4':tempCoordinates['D4'],'D5':tempCoordinates['D5'],'D6':tempCoordinates['D6'],'E4':tempCoordinates['E4'],'E5':tempCoordinates['E5'],'E6':tempCoordinates['E6'],'F4':tempCoordinates['F4'],'F5':tempCoordinates['F5'],'F6':tempCoordinates['F6']}
	boxes['X6'] = {'D7':tempCoordinates['D7'],'D8':tempCoordinates['D8'],'D9':tempCoordinates['D9'],'E7':tempCoordinates['E7'],'E8':tempCoordinates['E8'],'E9':tempCoordinates['E9'],'F7':tempCoordinates['F7'],'F8':tempCoordinates['F8'],'F9':tempCoordinates['F9']}
	boxes['X7'] = {'G1':tempCoordinates['G1'],'G2':tempCoordinates['G2'],'G3':tempCoordinates['G3'],'H1':tempCoordinates['H1'],'H2':tempCoordinates['H2'],'H3':tempCoordinates['H3'],'I1':tempCoordinates['I1'],'I2':tempCoordinates['I2'],'I3':tempCoordinates['I3']}
	boxes['X8'] = {'G4':tempCoordinates['G4'],'G5':tempCoordinates['G5'],'G6':tempCoordinates['G6'],'H4':tempCoordinates['H4'],'H5':tempCoordinates['H5'],'H6':tempCoordinates['H6'],'I4':tempCoordinates['I4'],'I5':tempCoordinates['I5'],'I6':tempCoordinates['I6']}
	boxes['X9'] = {'G7':tempCoordinates['G7'],'G8':tempCoordinates['G8'],'G9':tempCoordinates['G9'],'H7':tempCoordinates['H7'],'H8':tempCoordinates['H8'],'H9':tempCoordinates['H9'],'I7':tempCoordinates['I7'],'I8':tempCoordinates['I8'],'I9':tempCoordinates['I9']}

	for i in boxes:
		if key == i:
			for j in boxes[i]:
				if j == coordinateValue:
					for k in boxes[i].values():
						boxvalues.append(k)
					for l in range (0, len(boxvalues)):
						if boxvalues[l] == number:
							print ("\tThere exist that number in that box.")
							return False
					return True

def boardCheck (blankCoordinates, changedCoordinates):			# CHECKS IF THE BOARD IS COMPLETE WITH NO ERRORS
	if len(blankCoordinates) == len(changedCoordinates):
		return True
	else:
		return False

#		END --- END OF FUNCTIONS

#========================================================TEST CANVAS FOR CODES================================================================#