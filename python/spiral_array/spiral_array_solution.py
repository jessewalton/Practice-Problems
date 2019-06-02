#!/usr/bin/env python

from itertools import izip
from math import sqrt

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
	n = len(ARRAY_NxM)
	m = len(ARRAY_NxM[0])
	size = n * m
	revolution = 0
	cycle = 0
	count = 0
	forward = 1
	backward = -1

	while(count < size):

		if (size - 1 == count) and (n % 2 == 1):
			x = (n - 1) / 2
			y = (n - 1) / 2
			#print "[",x,"][", y, "]: ", ARRAY_NxM[y][x]
			traverse_order.append(ARRAY_NxM[y][x])
			count += 1
		
		y = cycle
		for x in range(cycle, n - (1 + cycle), forward):
			#print "[",x,"][", y, "]: ", ARRAY_NxM[y][x]
			traverse_order.append(ARRAY_NxM[y][x])
			count += 1

		x = n - (1 + cycle)
		for y in range(cycle, (n - (1 + cycle)), forward):
			#print "[",x,"][", y, "]: ", ARRAY_NxM[y][x]
			traverse_order.append(ARRAY_NxM[y][x])
			count += 1
		
		y = n - (1 + cycle)
		for x in range((n - (1 + cycle)),(1 + cycle) - 1, backward):
			#print "[",x,"][", y, "]: ", ARRAY_NxM[y][x]
			traverse_order.append(ARRAY_NxM[y][x])
			count += 1

		x = cycle
		for y in range((n - (1 + cycle)),(1 + cycle) - 1, backward):
			#print "[",x,"][", y, "]: ", ARRAY_NxM[y][x]
			traverse_order.append(ARRAY_NxM[y][x])
			count += 1

		cycle += 1
		
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
		print "Lists Match"
		return True

# check order of list
def check_list(LIST):
	n = int(sqrt(len(LIST)))
	correct_order = []

	if n == 4:
		correct_order = [
			1,	2,	3,	4,
			8,	12,	16,	15,
			14,	13,	9,	5,
			6,	7, 	11, 10
		]

	elif n == 5:
		correct_order = [
			1, 	2, 	3, 	4, 	5,
			10, 15,	20,	25,	24,
			23,	22, 21, 16, 11,
			6, 	7, 	8, 	9, 	14,
			19, 18, 17, 12,	13
		]
		
	elif n == 6:
		correct_order = [
			1, 	2, 	3, 	4, 	5, 	6,
			12, 18, 24, 30, 36, 35,
			34, 33, 32, 31, 25, 19,
			13, 7, 	8, 	9, 	10, 11,
			17,	23, 29, 28, 27, 26,
			20, 14, 15, 16, 22, 21
		]


	print "Expected Order:\t", correct_order
	print "Actual Order:\t", LIST

	return compare_lists(correct_order, LIST)

# helper function - build, traverse and test
def build_and_test(n):
	_array = build_2d_array(n, n)
	print_2d_array(_array)
	_path = traverse_cw_spiral(_array)
	check_list(_path)




''' Main '''

# 4 by 4: build, navigate and test 
build_and_test(4)

# 5 by 5: Build, navigate and test
build_and_test(5)

# 6 by 6: Build, navigate and test
build_and_test(6)
