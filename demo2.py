from collections import defaultdict
from get import get_artist_ID, get_itemsim, get_usersim, get_friends, get_train, get_test
from sys import stdin

sim = get_itemsim()
artist_ID = get_artist_ID()
train = get_train()

for line in stdin:
	artist = line.strip()
	scores = []
	for sim_artist in sim[artist]:
		similarity_score = sim[artist][sim_artist]
		scores.append((similarity_score,sim_artist))
	topNsimilar = sorted(scores,reverse=1)[:10]
	for tup in topNsimilar:
		print(artist_ID[tup[1]], tup[0])