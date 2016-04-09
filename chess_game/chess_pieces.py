


""" 
	Class:	ChessPiece 
	Usage: 	contains team, current location, type, uid and movement patterns

"""
class ChessPiece(object):
	PAWN 	 = 8
	ROOK_L 	 = 9
	KNIGHT_L = 10
	BISHOP_L = 11
	QUEEN 	 = 12
	KING 	 = 13
	BISHOP_R = 14
	KNIGHT_R = 15
	ROOK_R 	 = 16


	def __init__(self, uid):
		self.uid = uid
		self.x = 0
		self.y = 0
		self.move_x = 0
		self.move_y = 0
		self.team = 0
		self.name = ""

		
		# assign team
		if uid <= 16:
			self.team = 0 #white
		else:
			self.team = 1 #black
		
		# normalize value for both teams
		piece_type = uid % 17

		# initialize piece location

		if piece_type 	<= 	PAWN: 			# pawns
			self.x = 	uid - 1 
			self.y = 	6
			self.name = "Pawn"

		elif piece_type == 	ROOK_L:			# rook
			self.x = 	uid - 9
			self.y = 	7
			self.name = "Rook"

		elif piece_type == 	KNIGHT_L:		# knight
			self.x = 	uid - 9
			self.y = 	7
			self.name = "Knight"

		elif piece_type == 	BISHOP_L:		# bishop
			self.x = 	uid - 9
			self.y = 	7
			self.name = "Bishop"

		elif piece_type == 	QUEEN:			# queen
			self.x = 	3
			self.y = 	7
			self.name = "Queen"

		elif piece_type == 	KING:			# king
			self.x = 	4
			self.y = 	7
			self.name = "King"

		elif piece_type == 	BISHOP_R:		# bishop
			self.x = 	uid - 9	
			self.y = 	7
			self.name = "Bishop"

		elif piece_type == 	KNIGHT_R:		# knight
			self.x = 	uid - 9
			self.y = 	7
			self.name = "Knight"

		elif piece_type == 	ROOK_R:			# rook
			self.x = 	uid - 9
			self.y = 	7
			self.name = "Rook"

		else:
			print("Error")


	# display info for piece
	def printInfo(self):
		print ("%s" % self.name)
		print ("\tuid: \t%s" % self.uid)
		print ("\tteam: \t%s" % self.team)
		print ("\tx:", self.x, end="")
		print ("\ty:", self.y)


	# should be inherited by all pieces, use self.x and self.y to find current location and 
	# uid - piece id
	# x_coord - x coordinate destination
	# y_coord - y coordinate destination
	def movePiece(self, x_coord_dest, y_coord_dest):
		#valid_move = checkDestination(x_coord_dest, y_coord_dest)
		#if valid_move:
		self.x = x_coord_dest
		self.y = y_coord_dest


	# check if destination is available (if no other teamate is there)
	def checkDestination(self, x, y):
		return True



	# generate a list of (x, y) tuples for valid destinations
	# need: current location, bounds of board, type of piece, team
	def getValidMoves(self):
		validMoves = []
		return validMoves





class Pawn(ChessPiece):
	def __init__(self, uid):
		super(Pawn, self).__init__(uid)

		first_move = False		#toggle to true when piece is moved for first time
		self.moves = [	 		# valid coord move offset from current position
			(0, 2), 			# cond: first move only, desc: move forward two spaces
			(0, 1), 			# cond: no diag cap., desc: move forward one space
			(1, 1), 			# cond: diag. capture, desc: move diag. up-right
			(-1, 1)				# cond: diag. capture, desc: move diag. up-left
		]
		#self.move_x = [0, 0, 1]
		#self.move_y = [2, 1, 1] 
		#self.multiple = 1 # mult. of move_


class Rook(ChessPiece):
	def __init__(self, uid):
		
		super(Rook, self).__init__(uid)
		self.move_x = [0, 1]
		self.move_y = [1, 0]
		self.multiple = 7


class Knight(ChessPiece):
	def __init__(self, uid):
		super(Knight, self).__init__(uid)
		self.move_x = [2, 1]
		self.move_y = [1, 2]
		self.multiple = 1


class Bishop(ChessPiece):
	def __init__(self, uid):
		super(Bishop, self).__init__(uid)
		self.move_x = [1]
		self.move_y = [1]
		self.multiple = 7


class Queen(ChessPiece):
	def __init__(self, uid):
		super(Queen, self).__init__(uid)
		self.move_x = [0, 1, 1] # vertical, diagnal, horizontal
		self.move_y = [1, 1, 0]
		self.multiple = 7


class King(ChessPiece):
	def __init__(self, uid):
		super(King, self).__init__(uid)
		self.move_x = [0, 1, 1]
		self.move_y = [1, 1, 0]
		self.multiple = 1



if __name__ == '__main__':

	"""

	chess_pieces = []

	# init all game pieces
	for team in range(2):
		for uid in range(1, 17):

			print("%2s" % (uid + (team*16)), end=" ")

			if (team == 0):
				print("White", end=" ")
			else:
				print("Black", end=" ")


			if (uid <= 8):
				print("Pawn")
				chess_pieces.append(Pawn(uid))

			elif (uid == 9 or uid == 16):
				print("Rook")
				chess_pieces.append(Rook(uid))

			elif (uid == 10 or uid == 15):
				print("Knight")
				chess_pieces.append(Knight(uid))

			elif (uid == 11 or uid == 14):
				print("Bishop")
				chess_pieces.append(Bishop(uid))

			elif (uid == 12):
				print("Queen")
				chess_pieces.append(Queen(uid))

			elif (uid == 13):
				print("King")
				chess_pieces.append(King(uid))

			else:
				print()

	for piece in chess_pieces:
		piece.printInfo()

	temp = chess_pieces.pop(30)
	chess_pieces.insert(30, temp)

	for piece in chess_pieces:
		piece.printInfo()

	"""