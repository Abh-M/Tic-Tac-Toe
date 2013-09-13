
	
cellmap  = {
(0,0) : { "ROW":[ (0,1), (0,2) ] ,  "COL" :[ (1,0), (2,0) ], "DIA": [ (1,1), (2,2) ] },
(0,1) : { "ROW":[ (0,0), (0,2) ] ,  "COL" :[ (1,1), (2,1) ], "DIA": None },
(0,2) : { "ROW":[ (0,0), (0,1) ] ,  "COL" :[ (1,2), (2,2) ], "DIA": [ (1,1), (2,0) ] },

(1,0) : { "ROW":[ (1,1), (1,2) ],   "COL":[ (0,0), (2,0) ], "DIA": None},
(1,1) : { "ROW":[ (1,0), (1,2) ],   "COL":[ (0,1), (2,1) ], "DIA": None},
(1,2) : { "ROW":[ (1,0), (1,1) ],   "COL":[ (0,2), (2,2) ], "DIA": None},


(2,0) : { "ROW":[ (2,1), (2,2) ],  "COL":[ (0,0), (1,0) ], "DIA":[ (1,1), (0,2) ] },
(2,1) : { "ROW":[ (2,0), (2,2) ],  "COL":[ (0,1), (1,1) ], "DIA":None },
(2,2) : { "ROW":[ (2,0), (2,1) ],  "COL":[ (0,2), (1,2) ], "DIA":[ (0,0), (1,1) ] }

}	








def getRwForCell(kCell):
	"""
	(tuple) -> list
	>>>getRowForCell((0,0))
	>>>[(0,0),(0,2)]
	>>>getRowForCell(None)
	>>>None
	"""
	#print "getting rows for cell ->",kCell
	rows = None
	for entry in cellmap.keys():
		if entry == kCell:
			rows = cellmap[kCell]["ROW"]
			break
	return rows

def getColoumnsForCell(kCell):
	"""
	get list of tuples in the column
	"""
	cols = None
	for entry in cellmap.keys():
		if entry == kCell:
			cols = cellmap[kCell]["COL"]
			break

	return cols


def getDiagonalForCell(kCell):
	"""
	get list of cells which are in diagonal for this cell
	"""

	dia = None
	for entry in cellmap.keys():
		if entry == kCell:
			dia = cellmap[kCell]["DIA"]
			break
	return dia



