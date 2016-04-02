#!/usr/bin/env python



""" 
	Class: 	ChessGame 
	Usage: 	Call from main to begin game, handles board and player turns

"""
class ChessGame(object):
	'Python chess game, built from scratch by Jesse Walton'

# private

	def __init__(self):
		
		# define instance variables
		self.turn = 0		# 0 = White
		self.checkmate = False
		self.player = ["White", "Black"]

		# create chess board
		self.chess_board = ChessBoard() 
		#self.chess_board.

	# toggle to next player
	def __togglePlayer(self):
		self.turn += 1
		self.turn %= 2

	# get user input, move pieces
	def __playTurn(self, player):
		pass


# public 

	# handles player turns and input
	def playGame(self):
		print "Begin Game"

		while(self.checkmate != True):

			
			# determine turn
			print "Begin %s Turn" % self.player[self.turn]

			#piece_uid = raw_input("Select Piece: ")
			#print "piece: ", piece_uid
			#print "selected %s @ [%s][%s]" % (self.white_pieces[piece_uid], self.white_pieces[piece_uid].x, self.white_pieces[piece_uid].y)

			#move = raw_input("Enter destination: ")
			#print "move to %s" % move

			""" 
			Player Turn:
				Select Piece (by uid)
					a. select destination (by x, y)
						confirm movement/ capture or alert player move is unavailable
							confirm
							cancel
					b. return to select piece
				Check for Checkmate
				Switch to other player
				End Turn

			"""


		
			if (self.__isCheckmate()):
				break

			self.__togglePlayer()

		print "Checkmate!"
		print "%s Player Wins!" % self.player[self.turn]
		print "Game Over"
	





""" 
	Class:	ChessBoard 
	Usage: 	Handles pieces, movement validation, movement and checkmate

"""
class ChessBoard(object):
		BOARD_SIZE = 8
		num_pieces = BOARD_SIZE * 2
		white_uid_range = range(1, 16)
		black_uid_range = range(17, 32)

	def __init__(self):

		# define instance variables
		self.turn = 0 		# 0 = white, 1 = black
		self.checkmate = False
		self.player = ["White", "Black"] 
		self.white_pieces = []
		self.black_pieces = []
		self.game_board = []	# might be easier to have pieces on separate
								# boards for movement/ capture checking?

		# initialize board
		self.__clearBoard()
		self.__resetPieces()
		self.__setBoard()
		

	# reset board
	def __clearBoard(self):
		print "clearBoard()"	#debug
		for y in range(0, 8):
			new_row = []
			for x in range(0, 8):
				new_row.append(0)
			self.game_board.append(new_row)
		self.__printBoard() #debug


	# put piece uid in x, y location
	def __setBoard(self):
		print "setBoard()"
		for piece in self.white_pieces:
			print "Board[%s][%s] -> %s %s" % piece.x, piece.y, self.player[piece.team], piece.name
			self.game_board[piece.y][piece.x] = piece.uid
		self.__printBoard() #debug


	# reset pieces
	def __resetPieces(self):
		print "resetPieces()" 	#debug

		 
		
		self.white_pieces.append( Pawn(1) ) 
		self.white_pieces.append( Pawn(2) )
		self.white_pieces.append( Pawn(3) )
		self.white_pieces.append( Pawn(4) )
		self.white_pieces.append( Pawn(5) )
		self.white_pieces.append( Pawn(6) )
		self.white_pieces.append( Pawn(7) )
		self.white_pieces.append( Pawn(8) )
		
		self.white_pieces.append( Rook(9) )
		self.white_pieces.append( Knight(10) )
		self.white_pieces.append( Bishop(11) )
		self.white_pieces.append( Queen(12) )
		self.white_pieces.append( King(13) )
		self.white_pieces.append( Bishop(14) )
		self.white_pieces.append( Knight(15) )
		self.white_pieces.append( Rook(16) )
		

		print "White Pieces"
		for piece in self.white_pieces:
			piece.printInfo()




		#for uid in range(self.BOARD_SIZE * 2, ):
		#	self.white_pieces[uid] = uid + 1


	def __isCheckmate(self):
		print "isCheckmate()" 	#debug
		if (True):
			return True



	def __printBoard(self):
		print "Game Board - White\n"
		for i in range(0, 8):
			print "\t\t",
			for j in range(0, 8):
				print "%4s" % self.game_board[i][j], 
			print "\n"

		print "Game Board - Black\n"
		for i in range(8, 0, -1):
			#print i
			print "\t\t",
			for j in range(8, 0, -1):
				print "%4s" % self.game_board[i-1][j-1],
			print "\n"


	# 







class ChessPiece(object):

	def __init__(self, uid):
		self.uid = uid
		self.x = 0
		self.y = 0
		self.move_x = 0
		self.move_y = 0
		self.team = 0
		self.name = ""

		"""
		# assign team
		if uid <= 16:
			self.team = 0 #white
		else:
			self.team = 1 #black
		"""

		# initialize location
		if uid <= 16: 				# white team
			if uid <= 8: 					# pawns
				#print "Pawn", 
				self.x = uid - 1 
				self.y = 6
				self.name = "Pawn"
			elif uid == 9 or uid == 16:		# rooks
				#print "Rook", 
				self.x = uid - 9
				self.y = 7
				self.name = "Rook"
			elif uid == 10 or uid == 15:	# knights
				#print "Knight", 
				self.x = uid - 9
				self.y = 7
				self.name = "Knight"
			elif uid == 11 or uid == 14:	# bishops
				#print "Bishop", 
				self.x = uid - 9
				self.y = 7
				self.name = "Bishop"
			elif uid == 12:					# queen
				#print "Queen", 
				self.x = 3
				self.y = 7
				self.name = "Queen"
			else:							# king
				#print "King", 
				self.x = 4
				self.y = 7
				self.name = "King"

			#self.game_board[self.x][self.y] = uid
			#print "Created"
				

		else:				# black team
			pass


	# display info for piece
	def printInfo(self):
		print "%s" % self.name
		print "\tuid: \t%s" % self.uid
		print "\tteam: \t%s" % self.team
		print "\tx:", self.x,
		print "\ty:", self.y

	# should be inherited by all pieces, use self.x and self.y to find current location and 
	# uid - piece id
	# x_coord - x coordinate destination
	# y_coord - y coordinate destination
	def movePiece(self, color, uid, x_coord, y_coord):
		valid_move = checkDestination(x_coord, y_coord)
		if valid_move:
			self.x = x_coord
			self.y = y_coord


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
			(0, 1), 			# cond: only if no pieces can be captured diag., desc: move forward one space
			(1, 1), 			# cond: diag. capture, desc: move diag. up-right
			(-1, 1)				# cond: diag. capture, desc: move diag. up-left
		]
		self.move_x = [0, 0, 1]
		self.move_y = [2, 1, 1] 
		self.multiple = 1 # mult. of move_


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


newGame = ChessGame()
#newGame.playGame()
