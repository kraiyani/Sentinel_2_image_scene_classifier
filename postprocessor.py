#!/usr/bin/env python
# coding: utf-8

from collections import Counter

def Most_Common(lst):
	data = Counter(lst)
	value = data.most_common(1)[0][0]
	return value

def get_adjacent_indices(i, j, m, n, matrix):
	adjacent_values = []
	adjacent_indices = []

	adjacent_indices.append((i,j))
	# in middle
	if (i > 0) and (j > 0) and (i < m) and (j < n) and (i != m - 1) and (j != n - 1):
		# row above
		adjacent_indices.append((i-1,j-1))
		adjacent_indices.append((i-1,j))
		adjacent_indices.append((i-1,j+1))
		# same row
		adjacent_indices.append((i,j-1))
		adjacent_indices.append((i,j+1))
		# row below
		adjacent_indices.append((i+1,j-1))
		adjacent_indices.append((i+1,j))
		adjacent_indices.append((i+1,j+1))
	# four corners
	elif (i == 0) and (j == 0):
		# top left
		adjacent_indices.append((i,j+1))
		adjacent_indices.append((i+1,j))
		adjacent_indices.append((i+1,j+1))
	elif (i == m - 1) and (j == 0):
		# bottom left
		adjacent_indices.append((i-1,j))
		adjacent_indices.append((i-1,j+1))
		adjacent_indices.append((i,j+1))
	elif (i == m - 1) and (j == n - 1):
		# bottom right
		adjacent_indices.append((i,j-1))
		adjacent_indices.append((i-1,j-1))
		adjacent_indices.append((i-1,j))
	elif (i == 0) and (j == n - 1):
		# top right
		adjacent_indices.append((i,j-1))
		adjacent_indices.append((i+1,j-1))
		adjacent_indices.append((i+1,j))
	# top row no corner
	elif (i == 0) and (0 < j < n):
		# same row
		adjacent_indices.append((i,j-1))
		adjacent_indices.append((i,j+1))
		# row below
		adjacent_indices.append((i+1,j-1))
		adjacent_indices.append((i+1,j))
		adjacent_indices.append((i+1,j+1))
	# bottom row no corner
	elif (i == m - 1) and (0 < j < n):
		# same row
		adjacent_indices.append((i,j-1))
		adjacent_indices.append((i,j+1))
		# row above
		adjacent_indices.append((i-1,j-1))
		adjacent_indices.append((i-1,j))
		adjacent_indices.append((i-1,j+1))
	# first column no corner
	elif (j == 0) and (0 < i < m):
		adjacent_indices.append((i-1,j))
		adjacent_indices.append((i-1,j+1))
		adjacent_indices.append((i,j+1))
		adjacent_indices.append((i+1,j))
		adjacent_indices.append((i+1,j+1))
	# last column no corner
	elif (j == n - 1) and (0 < i < m):
		adjacent_indices.append((i-1,j))
		adjacent_indices.append((i-1,j-1))
		adjacent_indices.append((i,j-1))
		adjacent_indices.append((i+1,j-1))
		adjacent_indices.append((i+1,j))

	for x,y in adjacent_indices:
		adjacent_values.append(matrix[x][y])
	value = Most_Common(adjacent_values)
	if value == 0:
		return matrix[i][j]
	else:
		return value