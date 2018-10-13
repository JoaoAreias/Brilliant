"""
Danielle, Lilliana, and Melody play a fighting video game in tournament mode. 
In this mode, two players play a match, and the winner of the match plays a
new match against the player who was sitting out. This continues until a player
wins two matches in a row. Danielle and Lilliana play the first match.

If they are all equally skilled at the game,
then what is the probability that Melody will win the tournament?
"""
from numpy.random import choice

total = 0
wins = 0

def play():
	players = ['D', 'L', 'M']
	winner = choice(['D', 'L'])
	loser = 'D' if winner == 'L' else 'L'
	waiting = 'M'

	while True:
		match = [winner, waiting]
		w2 = choice(match)
		if winner == w2:
			return winner
		winner = w2
		waiting = loser
		loser = match[0] if match[0] != w2 else match[1]

def run(runs=1000):
	global total
	global wins

	total += runs

	while runs:
		if play() == 'M':
			wins += 1
		runs -= 1

	return wins / total

print(run(1000000))
print(run(1000000))
print(run(1000000))
print(run(1000000))
print(run(1000000))
print(run(1000000))
print(run(1000000))
print(run(1000000))
print(run(1000000))
