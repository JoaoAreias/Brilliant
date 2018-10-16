"""
Routines to solve Brilliant.org's statistics
challanges
"""
from statistics import *
import numpy as np

Data = [
	[3, 4, 5, 6, 7, 7, 10],
]


def middle_value(data):
	""" Return a group of
	measurements os the middle
	value
	"""
	print(f'mean: {mean(data)}')
	print(f'median: {median(data)}')
	print(f'mode: {mode(data)}')


def ssr(data, func):
	""" Return the sum of square
	residuals given a regression
	function
	"""
	pass


if __name__ == '__main__':
	main()