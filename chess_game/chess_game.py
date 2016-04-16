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

	# setup game
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

	# mess with functions
	def test(self):
		
		# print board
		print ("Initial\n")
		self.chess_board.printBoard(0, 0)

			
		print ("Move forward 2\n")
		self.chess_board.movePieceByUid(1, 0, 4) 
		self.chess_board.printBoard(0, 0)


		print ("Move forward 1\n")
		self.chess_board.movePieceByUid(1, 0, 3) 
		self.chess_board.printBoard(0, 0)


		print ("Move forward 1\n")
		self.chess_board.movePieceByUid(1, 0, 2) 
		self.chess_board.printBoard(0, 0)


		print ("Move forward 1 - Capture 23\n")
		self.chess_board.movePieceByUid(1, 1, 1) 
		self.chess_board.printBoard(0, 0)




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
			return False




	def getPieceFromCoords(self, x, y):
		return self.game_board[y][x]




	def getPieceFromUid(self, uid):
		for piece in self.all_pieces:
			if piece.uid == uid:
				return piece




	def movePieceByOrigin(self, x_start, y_start, x_dest, y_dest):
		

		# check coordinates
		if self.getPieceFromCoords(x_start, y_start) == 0:
			return 0

		# get reference to piece
		piece = self.getPieceFromCoords(x_start, y_start)

		# move piece if destination is valid
		self.__movePiece(piece, x_dest, y_dest)

		return 1




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

				# set new piece coordinates
				piece.x = x_dest
				piece.y = y_dest

				# set first_move
				piece.first_move = False



	# force move piece to new coords with no restrictions
	def debugMove(self, uid, x_dest, y_dest):

		# get piece
		piece = self.getPieceFromUid(uid)

		# remove piece from current location
		self.game_board[piece.y][piece.x] = 0

		# remove enemy piece at destination
		self.game_board[y_dest][x_dest] = 0

		# move piece to destination
		self.game_board[y_dest][x_dest] = piece

		# set first_move
		piece.first_move = False


	# check coordinates, return -1 if empty, 0 if white piece, 1 if black piece
	def whatIsHere(self, x, y):
		if isinstance(self.game_board[y][x], ChessPiece):
			if self.game_board[y][x].team == 0:
				return 0  	# white piece
			else:
				return 1 	# black piece
		else:
			return -1 		# empty space



	# return a list coordinate tuples that are valid moves for the piece
	def getValidMoves(self, piece):

		# debug
		print ("Move list: %s %s (%s)" % (piece.color, piece.name, piece.uid), end=" ")
		print ("at (%s, %s)" % (piece.x, piece.y))

		valid_moves = []

		# Pawn move/ attack logic
		if isinstance(piece, Pawn):

			# track if there is a diag. attack
			attack = False

			# invert movement direction of white pieces
			pawn_mv_dir = 1 if (piece.team == 1) else -1

			# check all move 
			for index, (x, y, first, atk) in enumerate(piece.all_moves):
				
				# calc coord offset based on team
				x_mod = x * pawn_mv_dir
				y_mod = y * pawn_mv_dir

				# add offset to current location
				dest_x = piece.x + x_mod
				dest_y = piece.y + y_mod

				# debug
				sign = "+" if (piece.team == 1) else "-"
				print("[%s] (%s, %s) %s" % (index, piece.x, piece.y, sign), end=" ")
				print("(%2s, %2s) --> (%2s, %2s)\t" % ( x, y, dest_x, dest_y), end=" ")
	
				# skip value if out of range
				if dest_x < 0 or dest_x > 7 \
				or dest_y < 0 or dest_y > 7:
					print("out of range")
					continue

				# determine empty/ white piece/ black piece
				teamAtDest = self.whatIsHere(dest_x, dest_y)

				# piece is in attack range, ignore standard moves
				if index >= 2 and attack == True:
					print("attack found, skip index")
					continue


				# check attack spaces (diagonal)
				if index == 0 or index == 1:

					# ally at location, invalid
					if teamAtDest == piece.team:
						print ("ally at diag, no add")

					# empty at location, invalid
					elif teamAtDest == -1:
						print ("blank at diag, no add")
					
					# enemy at location, valid
					else:
						print("enemy at diag, add (%s, %s)" % (dest_x, dest_y))
						valid_moves.append((dest_x, dest_y))
						attack = True


				# check for first move (2 spaces)
				if index == 2:

					# has this piece moved before?
					if piece.first_move == first:

						# ally at location, invalid
						if teamAtDest == piece.team:
							print ("ally at 2 ahead, no add")

						# empty at location
						elif teamAtDest == -1:
							print("empty at 2 ahead, add (%s, %s)" % (dest_x, dest_y))
							valid_moves.append((dest_x, dest_y))

						else:
							print ("enemy at 2 ahead, no add")
							

				# check single move
				if index == 3:

					# ally at location, invalid
					if teamAtDest == piece.team:
						pass

					# empty at location
					elif teamAtDest == -1:
						print("empty at 1 ahead, add (%s, %s)" % (dest_x, dest_y))
						valid_moves.append((dest_x, dest_y))
					
					# enemy at location, invalid
					else: 
						print("enemy at 1 ahead, no add")
					

				


	

		# other piece type
		else:
			for x, y in piece.all_moves:
				print ("x: %s\ty: %s" % (x, y * pawn_mv_dir))



		

		

		#return valid_moves

		#test_list = [] #simulate a valid move for uid #1
		#test_list.append((7, 4))
		#test_list.append((7, 5))
		#valid_moves = test_list
		
		return valid_moves



	# display game board by iterating through all elements of 2d board array 
	# and showing the uid of the piece at that location, the unicode character
	# or text (to be implemented)
	# col/ row dir = direction of column and row
	def printBoard(self, col_dir, row_dir):
		Unicode = False		# unicode vs uid (depreciated)
		display_type = 3 	# select: 1. uid, 2. text, 3. unicode (MV TO ARG)
		var = 1 			# used to determine color of square (not in use)
		display_row = []	# list of board rows

		#specify range for forward/ backward print
		board_range = [ 
			[0, 8, 1], 
			[7, -1, -1]
		]

		# set col range args
		c_start = board_range[col_dir][0]
		c_end 	= board_range[col_dir][1]
		c_incr 	= board_range[col_dir][2]

		r_start = board_range[row_dir][0]
		r_end = board_range[row_dir][1]
		r_incr = board_range[row_dir][2]

		# build title
		display_title = ("\nGame Board - White\n")

		# add title to list
		display_row.append(display_title)


		# build col header
		col_header = ("\t\t  ")
		for col in range(c_start, c_end, c_incr):
			col_header += ("{%2s}" % col)
		col_header += ("\n")

		# add col header to list
		display_row.append(col_header)


		# build current row
		for row in range(r_start, r_end, r_incr):
	
			# string to build row display
			curr_row = ""

			# row header
			curr_row += "\t {%2s}" % row

			# check each col for piece/ empty space
			for col in range(c_start, c_end, c_incr):

				# if there is a piece, append it's uid/ text/ unicode
				if isinstance(self.game_board[row][col], ChessPiece):

					# by uid
					if(display_type == 1):
						curr_row += ("%4s" % self.game_board[row][col].uid)
					
					# by text
					elif(display_type == 2):
						curr_row += ("%4s" % self.game_board[row][col].text)

					# by unicode
					else:
						curr_row += ("%4s" % chr(self.game_board[row][col].icon)) #placeholder
				
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
						curr_row += ("%4s" % "    ") #placeholder

			curr_row += ("\n")

			# add current row to list
			display_row.append(curr_row)


		for row in display_row:
			print(row)







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
