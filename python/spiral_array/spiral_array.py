#!/usr/bin/env python

from itertools import izip

'''

	::: Description ::: 

	Define 'traverse_cw_spiral(ARRAY)' to navigate a given array, starting at
	the top left and traversing it in a clockwise spiral. Return the order as a
	list. 


	::: Example ::: 

	Array
	 1 	 2 	 3 	 4
	 5 	 6	 7	 8	
	 9 	10	11	12
	13	14	15	16

	Solution 
	[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

'''




''' Functions '''

# traverse array and return as a list
def traverse_cw_spiral(ARRAY_NxM):
	traverse_order = []

	# code goes here!

	return traverse_order

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

# check elements in two lists
def compare_lists(CORRECT_LIST, PROPOSED_LIST):
	needed_matches = len(CORRECT_LIST)
	actual_matches = 0

	for list_1_item, list_2_item in izip(CORRECT_LIST, PROPOSED_LIST):
		if list_1_item == list_2_item:
			actual_matches += 1
	
	if actual_matches == needed_matches:
		return True

# check the solution to a 4 by 4 array
def check_4by4(CHECK_LIST_ORDER):
	correct_order = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 12, 10]

	print "Expected Order:\t", correct_order
	print "Actual Order:\t", CHECK_LIST_ORDER

	if compare_lists(correct_order, CHECK_LIST_ORDER):
		print "4 by 4: Lists match"
		return True
	else: 
		print "4 by 4: Lists do not match"
		return False





''' Main ''' 

# create and fill 4 by 4 array
array_4by4 = build_2d_array(4, 4)

# display formatted array
print_2d_array(array_4by4)

# traverse array
traverse_order_4by4 = traverse_cw_spiral(array_4by4)

# check traversal
check_4by4(traverse_order_4by4)

