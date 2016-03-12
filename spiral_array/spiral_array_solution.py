#!/usr/bin/env python

'''
	Problem: 
		Given a n*m array, start at the top left and traverse it in a clockwise
		spiral

'''


''' Functions '''

# build a 2 dimensional array and fill with values 1 to NxM
def build_2d_array(N, M):
	count = 0
	array_2d = []
	for i in range(0, N):
		row = []
		for j in range(0, M):
			count += 1
			row.append(count)
		array_2d.append(row)
	return array_2d

# print array as a formatted table
def print_2d_array(ARRAY):
	print 
	for row in ARRAY:
		for item in row:
			print "\t", item,
		print 
	print



''' Main ''' 

# create and fill array
array_2d = build_2d_array(4, 4)


# display array
print_2d_array(array_2d)




