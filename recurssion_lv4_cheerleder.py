"""
A human pyramid is built up by several layers. At the top, 
there is one person, and each subsequent layer has 1 additional
person. Each person is supported by the 2 people that are
beneath them.

Consider a 9 layer pyramid, which comprises 45 people.
Assuming that all the cheerleaders weigh 128 pounds each, and
that the weight is equally distributed amongst both supporters,
what is the most weight supported by anyone in this pyramid?
"""

def weight(m):
	""" 
	Weight on the layer m
	"""
	memo_table = [[0. for _ in range(m)] for _ in range(m)]
	memo_table[0][0] = 128.

	for layer in range(m):
		for person in range(layer+1):
			memo_table[layer][person] = 0.5*(memo_table[layer-1][person-1] + memo_table[layer-1][person]) + 128

	return memo_table[m-1]

assert sum(weight(9)) == 128*45
print(weight(9))
