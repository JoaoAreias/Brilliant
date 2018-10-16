"""
Miller-Rabin primality test
"""
from math import log

def gcd(x, y):
	return y if not (x%y) else gcd(y, x%y)

def miller_rabin(n):
	# Value checks
	if not (type(n) is int):
		raise ValueError("input must be an integer") 
	if n < 2:
		return False
	if n == 2:
		return True


	# Step 1: Determine k and m such that n-1 = (2^k)m 
	k = round(log(gcd(n-1, 2**1024), 2))
	m = (n-1) // (2**k)
	while not (m%2):
		k += round(log(gcd(m, 2**1024), 2))
		m = (n-1) // (2**k)

	# Step 2: Choose a shuch that 1 < a < n-1
	a = 2

	# Step 3: Compute b0 = a^m mod n and b_{n} = b_{n-1}^2 mod n
	b = pow(a, m, n)
	if b == 1 or b == n-1:
		return True

	S = set([b])
	
	while True:
		b = pow(b, 2, n)
		if b == 1 or b in S:
			return False
		elif b == n-1:
			return True
		S.add(b)
		
if __name__ == '__main__':
	print("Starting Miller-Rabin")
	print(miller_rabin(7337488745629403488410174275830423641502142554560856136484326749638755396267050319392266204256751706077766067020335998122952792559058552724477442839630133))


