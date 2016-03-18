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
		print "isCheckmate()"
		if (True):
			return True

	def __currentPlayer(self):
		if self.turn == 0:
			self.turn = 1
			return "White"
		elif self.turn == 1:
			self.turn = 0
			return "Black"
	# 
	def playGame(self):
		print "Begin Game"
		while(self.checkmate != True):

			# determine turn
			player = self.__currentPlayer()
			print "Begin %s Turn" % player
			

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