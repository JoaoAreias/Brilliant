"""
https://brilliant.org/problems/algebra-or-computer-science-ii/

20 can be obtained as a product of some positive integers (greater than 1) in 7 different ways as following;
20 = 2 * 2 * 5 = 2 * 5 * 2 = 2 * 10 = 4 * 5 = 5 * 2 * 2 = 5 * 4 = 10 * 2

Similarly, 18 can also be obtained in 7 different ways as following;
18 = 2 * 3 * 3 = 2 * 9 = 3 * 2 * 3 = 3 * 3 * 2 = 3 * 6 = 6 * 3 = 9 * 2

In how many ways can we can get nine nines by multiplying two or more numbers such that order of the factors matters?
"""

def prime_factorization(n):
	"""Returns a divtionary with the prime facotrs of
	n and it's prime factorization
	"""
	if n == 1:
		return {1:1}

	i = 2
	k = n**0.5
	prime_factors = {}

	while i <= k:
		if n%i == 0:
			n //= i
			k = n**0.5
			prime_factors[i] = prime_factors[i] + 1 if i in prime_factors else 1
			i -= 1

		i += 1
	if n != 1:
		prime_factors[n] = prime_factors[n] + 1 if n in prime_factors else 1

	return prime_factors


def find_factors(prime_factors, depth):
	"""Uses the result of prime_factorization to
	recursivelly find all the factors of a number"""
	if depth == len(prime_factors):
		return [1]

	factors = []
	key = list(prime_factors.keys())[depth]
	for i in range(prime_factors[key] + 1):
		for j in find_factors(prime_factors, depth+1):
			factors.append(j*(key**i))

	return factors

def factor(n):
	"""Returns a sorted list of all factors of n"""
	prime_factors = prime_factorization(n)
	factors = find_factors(prime_factors, 0)

	return sorted(factors)

def f(n):
	"""
	Let's calculate how in many ways can we write a number
	as a multiple of it's factors.
	"""

	# First we get a list of all factors of N excluding 1 and itself
	factors = factor(n)[1:-1]

	_sum = len(factors)
	for number in factors:
		_sum += f(n//number)

	return _sum


print(f(999999999))