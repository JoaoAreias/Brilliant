"""Chaos has emerged in a 1×1 field; The fabric of space will never be healed.
The limits of light have been replaced: All matter is teleported to a random place!

How far is the average point displaced?

This rule of space should not be disregarded: You might teleport to exactly where you started.
"""
from time import sleep
import threading
import numpy as np

total = 0
dist = 0

def point():
	return np.random.rand(2)

def simulation(runs=1):
	global total
	global dist
	
	while runs:
		p1 = point()
		p2 = point()

		dist += np.linalg.norm(p2-p1)

		total += 1
		runs  -= 1
	return dist/total

def run_simulation(runs=1, threads=4):
	global dist
	global total

	default_threads = threading.active_count()
	total_runs = runs
	
	while runs:
		active_threads = threading.active_count()
		if active_threads - default_threads < threads:
			print("%d%% finnished" % (100 - int(100*runs/total_runs)))
			if runs >= 10000:
				threading.Thread(target=simulation, kwargs={'runs':10000}).start()
				runs -= 10000
			else:
				threading.Thread(target=simulation, kwargs={'runs':runs}).start()
				runs = 0
	while default_threads != threading.active_count():
		pass

	return dist/total

print("--- Stating simulation ---")
print(simulation(runs=10000000))
print(simulation(runs=10000000))
print(simulation(runs=10000000))
print(simulation(runs=10000000))
print(simulation(runs=10000000))
print(simulation(runs=10000000))
print(simulation(runs=10000000))
print(simulation(runs=10000000))
print(simulation(runs=10000000))
print(simulation(runs=10000000))