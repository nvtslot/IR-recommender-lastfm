from collections import defaultdict
from get import get_artist_ID, get_itemsim, get_usersim, get_friends, get_train, get_test
from sys import stdin

sim = get_itemsim()
artist_ID = get_artist_ID()
train = get_train()
n=10

for line in stdin:
	u1 = line.strip()

	already_listened = [] # will contain all artists that are already listened by the user
	try:
		for artist in train[u1]:
			already_listened.append((train[u1][artist],artist))
	except KeyError:
		pass
	topNlistened = sorted(already_listened,reverse=1)[:n]
	for tup in topNlistened:
		print(tup[0], "\t", artist_ID[tup[1]], "(" + str(tup[1]) + ")")