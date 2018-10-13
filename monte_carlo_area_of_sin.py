"""Using monte carlo method find the area of a sine curve from 0
to 3pi, what is the area?

Details and Assumptions
Consider the area below the x-axis as negative area.
"""
import numpy as np


def point():
	(x, y) =  np.random.rand(2)
	x = 3*np.pi*x
	y = 2*y - 1
	return (x, y)

def simulation(runs=1):
	total   = 0
	positive = 0
	negative = 0

	while runs:
		(x, y) = point()
		if y < 0:
			if y >= np.sin(x):
				negative += 1
		else:
			if y <= np.sin(x):
				positive += 1
		total += 1
		runs  -= 1

	positive_area = 6*np.pi*positive/total
	negative_area = 6*np.pi*negative/total

	return positive_area-negative_area

area = simulation(runs=100000)
print(area)

