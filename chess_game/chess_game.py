#!/usr/bin/env python

from chess_pieces import *
import sys
from io import TextIOWrapper
sys.stdout = TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')




""" 
	Class: 	ChessGame 
	Usage: 	Call from main to begin game, handles board and player turns

"""
class ChessGame(object):

	'Python chess game, built from scratch by Jesse Walton'

	def __init__(self):
		# define instance variables
		self.turn = 0		# 0 = White
		self.checkmate = False
		self.player = ['White','Black']
		# create chess board
		self.chess_board = ChessBoard() 


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
		print ("Begin Game")

		while(self.checkmate != True):
			print("Begin %s Turn" % (self.player[self.turn]))

			#piece_uid = raw_input("Select Piece:")
			#print ("piece:", piece_uid
			#print ("selected %s @ [%s][%s]" % (self.all_pieces[piece_uid], self.all_pieces[piece_uid].x, self.all_pieces[piece_uid].y)

			#move = raw_input("Enter destination:")
			#print ("move to %s" % move

			'''
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

			'''
		
			if (self.__isCheckmate()):
				break

			self.__togglePlayer()

		print ("Checkmate!")
		print ("%s Player Wins!" % self.player[self.turn])
		print ("Game Over")
	


	def test(self):

		# test move
		moveByOrigin = False
		self.chess_board.printBoard()
	
		if (moveByOrigin):
			print("Move UID 8 from (7,6) to (7,4)")
			self.chess_board.movePieceByOrigin(7,6,7,4)
		else:
			print("Move UID 8 from (7,6) to (7,4)")
			self.chess_board.movePieceByUid(8, 7, 4) 

		self.chess_board.printBoard()





""" 
	Class:	ChessBoard 
	Usage: 	Handles pieces, movement validation, movement and checkmate

"""
class ChessBoard(object):

	# static vars
	BOARD_SIZE = 8
	num_pieces = BOARD_SIZE * 2
	white_uid_range = range(1, 16)
	black_uid_range = range(17, 32)
	player = ['White', 'Black']




	# create board and pieces, then set board with pieces
	def __init__(self):

		# instance vars
		self.turn 		= 	0 		# 0 = white, 1 = black
		self.checkmate 	= 	False
		self.all_pieces = 	[]
		self.game_board = 	[]	

		# initialize board
		self.__createBoard()
		self.__createPieces()
		self.__setBoard()
		



	# create 2d game board
	def __createBoard(self):
		print ("createBoard()")	#debug
		self.game_board = []
		for y in range(0, 8):
			new_row = []
			for x in range(0, 8):
				new_row.append(0)
			self.game_board.append(new_row)




	# put ref to piece in x, y location
	def __setBoard(self):
		print ("setBoard()") 
		for piece in self.all_pieces:
			self.game_board[piece.y][piece.x] = piece
		



	# create all pieces, add to list
	def __createPieces(self):
		print("createPieces()")
		self.all_pieces = []

		for team in [0, 1]:
			offset = team * 16
			for count in range(1, 17):
				new_piece = None

				if count <= 8:
					new_piece = Pawn(count + offset)
				elif count == 9 or count == 16:
					new_piece = Rook(count + offset)
				elif count == 10 or count == 15:
					new_piece = Knight(count + offset)
				elif count == 11 or count == 14:
					new_piece = Bishop(count + offset)
				elif count == 12:
					new_piece = Queen(count + offset)
				elif count == 13:
					new_piece = King(count + offset)
				else:
					print("ERROR")

				self.all_pieces.append(new_piece)
				#new_piece.printInfo()
				



	def __isCheckmate(self):
		print ("isCheckmate()") 	#debug
		if (True):
			return True




	def getPieceFromCoords(self, x, y):
		return self.game_board[y][x]




	def getPieceFromUid(self, uid):
		for piece in self.all_pieces:
			if piece.uid == uid:
				return piece




	def movePieceByOrigin(self, x_start, y_start, x_dest, y_dest):
		
		# get reference to piece
		piece = self.getPieceFromCoords(x_start, y_start)

		# move piece if destination is valid
		self.__movePiece(piece, x_dest, y_dest)




	def movePieceByUid(self, uid, x_dest, y_dest):
		
		# get reference to piece
		piece = self.getPieceFromUid(uid)

		# move piece if destination is valid
		self.__movePiece(piece, x_dest, y_dest)

	


	def __movePiece(self, piece, x_dest, y_dest):

		# get all available moves
		move_list = self.getValidMoves(piece)
		
		# go through each tuple in move_list
		for x_avail, y_avail in move_list:

			# check if desired destination is in list of available destinations
			if x_dest == x_avail and y_dest == y_avail:

				# remove piece from current location
				self.game_board[piece.y][piece.x] = 0

				# remove enemy piece at destination
				self.game_board[y_dest][x_dest] = 0

				# move piece to destination
				self.game_board[y_dest][x_dest] = piece




	# compare current position against piece movement options generate
	# list of all available locations that are within bounds and do
	# not contain own team pieces
	def getValidMoves(self, piece):
		curr_x = piece.x
		curr_y = piece.y


		#all_moves = piece.moves 	 #holds movement tuples		

		#return valid_moves

		test_list = [] #simulate a valid move for uid #1
		test_list.append((7, 4))
		test_list.append((7, 5))
		
		return test_list



	# display game board by iterating through all elements of 2d board array 
	# and showing the uid of the piece at that location, the unicode character
	# or text (to be implemented)
	def printBoard(self):
		Unicode = False		# unicode vs uid (depreciated)
		display_type = 1 	# select: 1. uid, 2. text, 3. unicode (MV TO ARG)
		var = 1 			# used to determine color of square (not in use)
		display_row = []	# list of board rows


		# build title
		display_title = ("\nGame Board - White\n")

		# add title to list
		display_row.append(display_title)


		# build col header
		col_header = ("\t\t  ")
		for col in range(0, 8):
			 col_header += ("{%2s}" % col)
		col_header += ("\n")

		# add col header to list
		display_row.append(col_header)


		# build current row
		for row in range(0, 8):
			curr_row = ""

			# row header
			curr_row += "\t {%2s}" % row

			# check each col for piece/ empty space
			for col in range(0, 8):

				# if there is a piece, append it's uid/ text/ unicode
				if isinstance(self.game_board[row][col], ChessPiece):

					# by uid
					if(display_type == 1):
						curr_row += ("%4s" % self.game_board[row][col].uid)
					
					# by text
					elif(display_type == 2):
						curr_row += ("%4s" % self.game_board[row][col].uid)

					# by unicode
					else:
						curr_row += ("%4s" % self.game_board[row][col].uid) #placeholder
				
				# if there is no piece, append blank space
				else:

					# as 0
					if (display_type == 1):
						curr_row += ("%4s" % "0")

					# as "  " 
					elif (display_type == 2):
						curr_row += ("    ")

					# as square
					else:
						curr_row += ("%4s" % "0") #placeholder

			curr_row += ("\n")

			# add current row to list
			display_row.append(curr_row)



		for row in display_row:
			print(row)


		"""
		print ("\nGame Board - Black\n")

		# print col header
		print ("\t\t  ", end="")
		for col in range(7, -1, -1):
			print ("{%2s}" % col, end="")
		print ("\n")

		# print board
		for row in range(8, 0, -1):
			var += 1 

			# row header
			print ("\t {%2s}" % (row-1), end="")

			# col values
			for col in range(8, 0, -1):
				var += 1

				# chess piece
				if isinstance(self.game_board[row-1][col-1], ChessPiece):

					# print uid
					if (Unicode):
						print ("%4s" % self.game_board[row-1][col-1].uid , end="")

					# print piece
					else:
						print ("%4s" % chr(self.game_board[row-1][col-1].display_char) , end="")
				
				# empty space
				else:

					# print 0
					if (Unicode):
						print ("%4s" % (0), end="")

					# print square
					else:

						# alternate white/ black squares
						if (var % 2 == 0):
							print (" %s  " % (chr(9632)), end="")

						else:
							print (" %s  " % (chr(9633)), end="")					

			print ("\n")
		"""






if __name__ == '__main__':

	newGame = ChessGame()
	newGame.test()

	"""
	print ("Display pieces using unichr()")
	for i in range(9812, 9824):
		print (chr(i), end=" ")
	print("")
	"""

	#newGame.playGame()
