import random
import branch

def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[i][j],
            if j != 2:
                print "|",
        print ""


def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            print turn, "won!!!"
            return True
        
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        print turn, "won!!!"
        return True

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "Draw"
        return True
        

    return False




            


def getVal(kPos):
	"""
	Get the symbol at a particular cell in the grid specified by (row,col)
	"""
	return map[kPos[0]][kPos[1]]


def setVal(kPos,val):
	"""
	Set the symbol at a particular position ins grid specified by val(either X or O)
	"""
	map[kPos[0]][kPos[1]] = val



def rowHasSysmbols(kCell,kSymbol):
	"""
	Check if other cells in the rows has symbol "X" or "O"
	"""
	rows = branch.getRwForCell(kCell)
	if rows != None:
		if getVal(rows[0]) == kSymbol and getVal(rows[1])==" " and getVal(kCell) == kSymbol:
			return rows[1],1,rows
		elif getVal(rows[1]) == kSymbol and getVal(rows[0])==" " and getVal(kCell) == kSymbol:
			return rows[0],0,rows
	return None,None,None



def colHasSymbols(kCell,kSymbol):
	"""
	Check if other cells in the column  has symbol "X" or "O"
	"""
	cols = branch.getColoumnsForCell(kCell)
	if cols != None:
		if getVal(cols[0]) == kSymbol and getVal(cols[1])==" " and getVal(kCell) == kSymbol:
			return cols[1],1,cols
		elif getVal(cols[1]) == kSymbol and getVal(cols[0])==" " and getVal(kCell) == kSymbol:
			return cols[0],0,cols

	return None,None,None


def diagonalHasSymbol(kCell,kSymbol):
	"""
	Check if other cells in the rows has symbol "X" or "O"
	"""
	if kCell == (1,1):
		#cell at the center is special case which lies on two diagonals
		dia = [(0,0),(2,2)]
		if getVal(dia[0]) == kSymbol and getVal(dia[1])==" " and getVal(kCell) == kSymbol:
			return dia[1],1,dia
		elif getVal(dia[1]) == kSymbol and getVal(dia[0])==" " and getVal(kCell) == kSymbol:
			return dia[0],0,dia
		
		dia = [(2,0),(0,2)]
		if getVal(dia[0]) == kSymbol and getVal(dia[1])==" " and getVal(kCell) == kSymbol:
			return dia[1],1,dia
		elif getVal(dia[1]) == kSymbol and getVal(dia[0])==" " and getVal(kCell) == kSymbol:
			return dia[0],0,dia
	else:
		dia = branch.getDiagonalForCell(kCell)
		if dia == None:
			return None,None,None
		if getVal(dia[0]) == kSymbol and getVal(dia[1])==" "  and getVal(kCell) == kSymbol:
			return dia[1],1,dia
		elif getVal(dia[1]) == kSymbol and getVal(dia[0])==" "  and getVal(kCell) == kSymbol:
			return dia[0],0,dia
	return None,None,None

		


def next_move(kPlayerMove):
	#print userSymbol," ",computerSymbol," ",kPlayerMove

	#check if winning position
	
	for kCell in branch.cellmap.keys():
		row,index,arr = rowHasSysmbols(kCell,computerSymbol)
		#print row,index,arr

		if row!= None and getVal(kPlayerMove) == computerSymbol:
			setVal(row,computerSymbol)
			return
		
		col,index,arr = colHasSymbols(kCell,computerSymbol)
		if col!= None and getVal(kPlayerMove) == computerSymbol:
			setVal(col,computerSymbol)
			return

		dia,index,arr = diagonalHasSymbol(kCell,computerSymbol)
		if dia!= None and getVal(kPlayerMove) == computerSymbol:
			setVal(dia,computerSymbol)
			return
			


	#get the position of cells in the row, col and diagonal of the cell.
	rows = branch.getRwForCell(kPlayerMove)
	cols = branch.getColoumnsForCell(kPlayerMove)
	dias = branch.getDiagonalForCell(kPlayerMove)

	"""
	if two cells in a row or col or diagonal has usersymbols then
	insert computer sysmbol in the blank cell on that specific row/col/diagonal
	"""

	if rows != None:
		if getVal(rows[0]) == userSymbol and getVal(rows[1])==" ":
			setVal(rows[1],computerSymbol)
			return
		if getVal(rows[1]) == userSymbol and getVal(rows[0])==" ":
			setVal(rows[0],computerSymbol)
			return
	
	if cols != None:
		if getVal(cols[0]) == userSymbol and getVal(cols[1])==" ":
			setVal(cols[1],computerSymbol)
			return
		if getVal(cols[1]) == userSymbol and getVal(cols[0])==" ":
			setVal(cols[0],computerSymbol)
			return
	
	if dias != None or kPlayerMove == (1,1):
		if kPlayerMove != (1,1):
			if getVal(dias[0]) == userSymbol and getVal(dias[1])==" ":
				setVal(dias[1],computerSymbol)
				return
			if getVal(dias[1]) == userSymbol and getVal(dias[0])==" ":
				setVal(dias[0],computerSymbol)
				return
		elif kPlayerMove == (1,1):
			dias = [(0,0),(2,2)]
			if getVal(dias[0]) == userSymbol and getVal(dias[1])==" ":
				setVal(dias[1],computerSymbol)
				return
			if getVal(dias[1]) == userSymbol and getVal(dias[0])==" ":
				setVal(dias[0],computerSymbol)
				return
			dias = [(2,0),(0,2)]
			if getVal(dias[0]) == userSymbol and getVal(dias[1])==" ":
				setVal(dias[1],computerSymbol)
				return
			if getVal(dias[1]) == userSymbol and getVal(dias[0])==" ":
				setVal(dias[0],computerSymbol)
				return

	"""
	If the grid is blank 
	then chose any of the blank cell
	"""
	if getVal((1,1)) == " ":	
		setVal((1,1),computerSymbol)
	elif getVal(rows[0]) == " ":
		setVal(rows[0],computerSymbol)
	elif getVal(cols[0]) == " ":
		setVal(cols[0], computerSymbol)

	



#default : the user symbol is "X" and computer sysmbol is  "O"
turn = "X"
userSymbol = "X"
computerSymbol = "O"

#ask the user for symbol choice

symbolSelected = False;

while symbolSelected != True:

	user_choice = raw_input("Select your sysmbol 'X' or 'O' : ")
	print "User choice is:",user_choice

	if user_choice == "O":
		turn = "O"
		userSymbol = "O"
		computerSymbol = "X"
		symbolSelected = True
	
	elif user_choice == "X":
		symbolSelected = True
	
	else:
		print "Invalid choice!! select either 'X' or 'O'"
	


map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False

playermove = None

while done != True:
    print_board()
    
    print turn, "'s turn"
    print

    moved = False
    while moved != True:
        print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
        print "1|2|3"
        print "4|5|6"
        print "7|8|9"
        print

        try:
			if turn == computerSymbol:
				#play the next move
				next_move(playermove)
				moved=True
				done = check_done()
			else:
				pos = input("Select: ")
				if pos <=9 and pos >=1:
					Y = pos/3
					X = pos%3
					if X != 0:
						X -=1
					else:
						X = 2
						Y -=1
				#	print "Y: ",Y," X :",X          
					if map[Y][X] == " ":
						map[Y][X] = turn
						moved = True
						playermove = tuple([Y,X])
						done = check_done()
			#toogle turns			
			if done == False:
				if turn == "X":
					turn = "O"
				else:
					turn = "X"
        except:
            print "You need to add a numeric value"
        
print_board()
