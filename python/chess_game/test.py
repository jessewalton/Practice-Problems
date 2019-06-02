
import sys
import unittest
import logging
from chess_pieces import *

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logger = logging.getLogger()


class testPieceCreation(unittest.TestCase):
	def test_initialPieceCoords(self):

		all_pieces = createPieces()

		# test number of pieces created
		self.assertEqual(len(all_pieces), 32)
		
		#test pawn 1 location (UID: 1)
		self.assertEqual(all_pieces[0].uid, 1)
		self.assertEqual(all_pieces[0].x, 0)
		self.assertEqual(all_pieces[0].y, 6)

		#test pawn 8 location (UID: 8)
		self.assertEqual(all_pieces[7].uid, 8)
		self.assertEqual(all_pieces[7].x, 7)
		self.assertEqual(all_pieces[7].y, 6)

		#test left rook location
		self.assertEqual(all_pieces[8].uid, 9)
		self.assertEqual(all_pieces[8].x, 0)
		self.assertEqual(all_pieces[8].y, 7)

		#test right rook location
		self.assertEqual(all_pieces[15].uid, 16)
		self.assertEqual(all_pieces[15].x, 7)
		self.assertEqual(all_pieces[15].y, 7)





class testMovePiece(unittest.TestCase):
	def test_movePieceByUid(self):
		pass
	def test_movePieceByCoords(self):
		pass


if __name__ == '__main__':
	stream_handler = logging.StreamHandler(sys.stdout)
	logger.addHandler(stream_handler)

	"""
	print("\t1. print")
	logging.debug("\t2. debug")
	logging.info("\t3. info")
	logging.warning("\t4. warning")
	logging.error("\t5. error")
	logging.critical("\t6. critical")
	"""

	unittest.main()