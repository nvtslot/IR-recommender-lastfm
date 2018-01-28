# item-based recommender on Last.FM data
# Nik van 't Slot, Karel Beckeringh, Wessel Reijngoud

from collections import defaultdict
from get import get_itemsim, get_train, get_test

def recommend(sim, train, u1, n):
	"""For every user it creates a top 10 most listened to artists, from that top 10 it creates
	a top 10 most similar artists to all artists in most listened to. It creates a weight for the similar artists
	from that weight it creates recommendations"""

	already_listened = [] # will contain all artists that are already listened by the user
	try:
		for artist in train[u1]:
			already_listened.append((train[u1][artist],artist))
	except KeyError:
		pass
	topNlistened = sorted(already_listened,reverse=1)[:n]
	
	popular = defaultdict(int) # will contain each recommended artist and their cumulative weights

	# create top N similar artists for top N listened artists
	for listen_tup in topNlistened:
		listencount, artist = listen_tup
		scores = []
		try:
			for sim_artist in sim[artist]:
				similarity_score = sim[artist][sim_artist]
				scores.append((similarity_score,sim_artist))
		except KeyError:
			pass
		topNsimilar = sorted(scores,reverse=1)[:n]
		
		# creates weight per similar artist and add to defaultdict
		for similarity_tup in topNsimilar:
			similarity, similar_artist = similarity_tup
			if artist not in already_listened: # only consider new artists
				weight = similarity*listencount # creates a weight using similarity scores and listencount
				popular[similar_artist] += weight

	return sorted(popular,key=popular.get,reverse=True)[:10]


def main():
	sim, train, test = get_itemsim(), get_train(), get_test()
	score = 0

	for line in test:
		user, artist = line.split()[:2]
		# get 10 recommended artists for every user
		recommended = recommend(sim, train, user, n=30)
		hit = int(artist in recommended) # determine whether the artist was recommended/predicted or not
		score += hit

	print("Score: {} from {}\nAccuracy: {:.2f}%".format(score, len(test), 100*score/len(test)))

if __name__ == '__main__':
	main()