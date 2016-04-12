





""" 
	Class:	ChessPiece 
	Usage: 	contains team, current location, type, uid and movement patterns

"""
class ChessPiece(object):
	BOARD_SIZE 	= 	8
	CHAR_OFFSET = 	9811
	PAWN 	 	= 	8
	ROOK_L 	 	= 	9
	KNIGHT_L 	= 	10
	BISHOP_L 	= 	11
	QUEEN 	 	= 	12
	KING 	 	= 	13
	BISHOP_R 	= 	14
	KNIGHT_R 	= 	15
	ROOK_R 	 	= 	16
	
	def __init__(self, uid):
		self.uid 		= 	uid
		self.team 		=	0

		self.init_x	 	=	0		# orig. location (test - first move)
		self.init_y 	=	0		# orig. location (test - first move)
		self.x 			=	0
		self.y 			=	0

		self.moves 		=	[]		# movement tuple
		self.name 		=	""
		self.icon 		=	""
		self.first_move =	True
		
		# assign team
		if uid < 17:
			self.team = 0 #white
		else:
			self.team = 1 #black
		
		# normalize value for both teams
		piece_type = ((uid-1) % 16) + 1

		
		# initialize piece location
		if piece_type  	<= 	self.PAWN: 			# pawns
			self.x = 	piece_type - 1
			self.y = 	6
			self.name = "Pawn"
			self.icon = self.CHAR_OFFSET + 6

		elif piece_type == 	self.ROOK_L:		# rook
			self.x = 	piece_type - 9
			self.y = 	7
			self.name = "Rook"
			self.icon = self.CHAR_OFFSET + 3

		elif piece_type == 	self.KNIGHT_L:		# knight
			self.x = 	piece_type - 9
			self.y = 	7
			self.name = "Knight"
			self.icon = self.CHAR_OFFSET + 5

		elif piece_type == 	self.BISHOP_L:		# bishop
			self.x = 	piece_type - 9
			self.y = 	7
			self.name = "Bishop"
			self.icon = self.CHAR_OFFSET + 4

		elif piece_type == 	self.QUEEN:			# queen
			self.x = 	3
			self.y = 	7
			self.name = "Queen"
			self.icon = self.CHAR_OFFSET + 2

		elif piece_type == 	self.KING:			# king
			self.x = 	4
			self.y = 	7
			self.name = "King"
			self.icon = self.CHAR_OFFSET + 1

		elif piece_type == 	self.BISHOP_R:		# bishop
			self.x = 	piece_type - 9	
			self.y = 	7
			self.name = "Bishop"
			self.icon = self.CHAR_OFFSET + 4

		elif piece_type == 	self.KNIGHT_R:		# knight
			self.x = 	piece_type - 9
			self.y = 	7
			self.name = "Knight"
			self.icon = self.CHAR_OFFSET + 5

		elif piece_type == 	self.ROOK_R:			# rook
			self.x = 	piece_type - 9
			self.y = 	7
			self.name = "Rook"
			self.icon = self.CHAR_OFFSET + 3

		else:
			print("Error: Coordinates not set")


		# invert coords if on black
		self.x = abs(self.x - (self.team * (self.BOARD_SIZE - 1)) )
		self.y = abs(self.y - (self.team * (self.BOARD_SIZE - 1)) )
		self.icon = self.icon + (self.team * 6)




	# display info for piece
	def printInfo(self):
		player = ["White","Black"]
		print ("(%2s) %s %s \t" % (self.uid, player[self.team], self.name), end="")
		print ("(%s, %s) -> %s" % (self.x, self.y, self.icon))
		



	""" unnessecary here? """
	# should be inherited by all pieces, use self.x and self.y to find current location and 
	# uid - piece id
	# x_coord - x coordinate destination
	# y_coord - y coordinate destination
	def movePiece(self, x_coord_dest, y_coord_dest):
		#valid_move = checkDestination(x_coord_dest, y_coord_dest)
		#if valid_move:
		self.x = x_coord_dest
		self.y = y_coord_dest
	



class Pawn(ChessPiece):
	def __init__(self, uid):
		super(Pawn, self).__init__(uid)
		self.multiple = 1
		self.moves = [	 		# valid coord move offset from current position
			( 0, 2), 			# cond: first move only, desc: move forward two spaces
			( 0, 1), 			# cond: no diag cap., desc: move forward one space
			( 1, 1), 			# cond: diag. capture, desc: move diag. up-right
			(-1, 1)				# cond: diag. capture, desc: move diag. up-left
		]


class Rook(ChessPiece):
	def __init__(self, uid):
		super(Rook, self).__init__(uid)
		self.multiple = 7
		self.moves = [
			( 0,  1),
			( 1,  0),
			( 0, -1),
			(-1,  0)
		]


class Knight(ChessPiece):
	def __init__(self, uid):
		super(Knight, self).__init__(uid)
		self.multiple = 1
		self.moves = [
			( 1,  2),
			( 1, -2),
			(-1,  2),
			(-1, -2),
			( 2,  1),
			( 2, -1),
			(-2,  1),
			(-2, -1)
		]


class Bishop(ChessPiece):
	def __init__(self, uid):
		super(Bishop, self).__init__(uid)
		self.multiple = 7
		self.moves = [
			( 1,  1),
			( 1, -1),
			(-1,  1),
			(-1, -1)
		]

class Queen(ChessPiece):
	def __init__(self, uid):
		super(Queen, self).__init__(uid)
		self.multiple = 7
		self.moves = [
			( 0,  1),
			( 1,  0),
			( 0, -1),
			(-1,  0),
			( 1,  1),
			( 1, -1),
			(-1,  1),
			(-1, -1)
		]


class King(ChessPiece):
	def __init__(self, uid):
		super(King, self).__init__(uid)
		self.multiple = 1
		self.moves = [
			( 0,  1),
			( 1,  0),
			( 0, -1),
			(-1,  0)
		]



# init all game pieces, return as list
def createPieces():	
	chess_pieces = []
	
	for uid in range(1, 33):
		#print("Current uid is: %s" % uid)

		piece_type = ((uid-1) % 16) + 1

		if (piece_type <= 8):
			chess_pieces.append(Pawn(uid))
		
		elif (piece_type in (9, 16)):
			chess_pieces.append(Rook(uid))

		elif (piece_type in (10, 15)):
			chess_pieces.append(Knight(uid))

		elif (piece_type in (11, 14)):
			chess_pieces.append(Bishop(uid))

		elif (piece_type == 12):
			chess_pieces.append(Queen(uid))

		elif (piece_type == 13):
			chess_pieces.append(King(uid))

		else:
			print("Error: Piece not created (uid = %s)" % uid)

	return chess_pieces

if __name__ == '__main__':
	
	pieces = createPieces()

	for piece in pieces:
		piece.printInfo()
		
	#temp = chess_pieces.pop(30)
	#chess_pieces.insert(30, temp)