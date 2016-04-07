
import unittest
from chess_pieces import *



class MyTestCase(unittest.TestCase):
	
   
	def test_piece_white_pawn(self):
		white_pawn = ChessPiece(1)
		self.assertEqual(white_pawn.uid, 1)
		self.assertEqual(white_pawn.x, 0)
		self.assertEqual(white_pawn.y, 6)

class MyTestCase2(unittest.TestCase):
	def test_piece_black_pawn(self):
		black_pawn = ChessPiece(17)
		self.assertEqual(black_pawn.uid, 17)
		self.assertEqual(black_pawn.x, 0)
		self.assertEqual(black_pawn.y, 6)




if __name__ == '__main__':
	unittest.main()