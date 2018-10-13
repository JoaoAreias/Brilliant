"""Three points are chosen uniformly at random from the
perimeter of a unit circle. Use Monte Carlo simulation
to compute the probability of the points forming an acute
triangle, what is the probability?
"""
import numpy as np


def point():
	theta = 2*np.pi*np.random.rand()
	x = np.cos(theta)
	y = np.sin(theta)
	return np.array((x, y))

def simulation(runs=1):
	total = 0
	acute = 0
	
	while runs:
		p1, p2, p3 = (point(), point(), point())
		# Size of vectors formed by those points
		v1 = np.linalg.norm(p2 - p1)
		v2 = np.linalg.norm(p3 - p2)
		v3 = np.linalg.norm(p1 - p3)
		
		# Angles can be found using cosine law
		theta1 = np.arccos((v1**2 + v2**2 - v3**2)/(2*v1*v2))
		theta2 = np.arccos((v2**2 + v3**2 - v1**2)/(2*v2*v3))
		theta3 = np.arccos((v3**2 + v1**2 - v2**2)/(2*v3*v1))
		
		if theta1 < np.pi/2 and theta2 < np.pi/2 and theta3 < np.pi/2:
			acute += 1

		total += 1
		runs  -= 1
	return acute/total

print(simulation(runs=100000))