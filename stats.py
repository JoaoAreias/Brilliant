"""
Routines to solve Brilliant.org's statistics
challanges
"""
from statistics import *

def middle_value(data):
	""" Return a group of
	measurements os the middle
	value
	"""
	y = list(map(lambda x: x[1], data))
	print(f'mean: {mean(y)}')
	print(f'median: {median(y)}')
	print(f'mode: {mode(y)}')


def ssr(data, func):
	""" Return the sum of square
	residuals given a regression
	function
	"""
	return sum(map(lambda x: (x[1] - func(x[0]))**2, data))

def sst(data):
	""" Return the total sum of
	squares
	"""
	y = list(map(lambda x: x[1], data))
	y_mean = mean(y)
	return sum(map(lambda y: (y_mean - y)**2, y))

def r_sq(data, func):
	""" Return the r^2 coefficient
	for our data
	"""
	return 1 - ssr(data, func)/sst(data)


if __name__ == '__main__':
	data1 = [(1, 1), (2, 3), (3, 2), (4, 6), (5, 8)]
	data2 = [(1, 1), (2, 6), (3, 2), (4, 6), (5, 8)]
	data3 = [(1, 1), (2, 2), (3, 5), (4, 6), (5, 9)]
	print(r_sq(data1, lambda x: 1.7*x - 1.1))
	print(r_sq(data2, lambda x: 1.4*x - 0.4))
	print(r_sq(data3, lambda x: 2*x - 1.4))
	