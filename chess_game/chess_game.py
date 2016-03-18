#!/usr/bin/env python

class ChessGame(object):
	
	# 2D array, stores piece UID at location
	game_board = []
	white_pieces = []
	black_pieces = []
	turn = 0
	checkmate = False

	def __init__(self):
		self.__resetBoard()
		self.__resetPieces()


	# reset board
	def __resetBoard(self):
		print "resetBoard()"

	# reset pieces
	def __resetPieces(self):
		print "resetPieces()"

	def __isCheckmate(self):
		return True

	# 
	def playGame(self):
		while(self.checkmate != True):
			print "Begin game"
			self.checkmate = True

			if (self.__isCheckmate()):
				break
		print "Checkmate!"
		print "Game Over"
	




	# x - x coordinate to check
	# y - y coordinate to check
	def checkDestination(self, x, y):
		
		return True


class ChessPiece(object):
	def __init__(self):
		pass

	# should be inherited by ALL pieces, use self.x and self.y to find current location and 
	# uid - piece id
	# x_coord - x coordinate destination
	# y_coord - y coordinate destination
	def movePiece(self, color, uid, x_coord, y_coord):
		destination_valid = checkDestination(x_coord, y_coord)
		if destination_valid:
			moveToDestination()

class Pawn(ChessPiece):
	pass


newGame = ChessGame()

newGame.playGame()