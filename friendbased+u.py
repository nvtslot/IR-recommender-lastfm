# friend-based recommender on Last.FM data
# improved by implementing user similarity scores
# Nik van 't Slot, Karel Beckeringh, Wessel Reijngoud

from collections import defaultdict
from get import get_usersim, get_friends, get_train, get_test

def recommend(sim, friends, train, u1):
	"""For every user it looks up their friends. The artists most listened to by these friends 
	will be recommended, if not already followed by the user. The listen count for each artist
	determines the weight of the recommendation.
	Friends who are not similar are not taken into account. Also, recommondations are now also weighted by
	the corresponding user similarity scores."""
	already_listened = [] # will contain all artists that are already listened to by the user
	try:
		for artist in train[u1]:
			already_listened.append(artist)
	except KeyError:
		pass

	popular = defaultdict(int) # will contain each recommended artist and their cumulative weights
	for friend in friends[u1]:
		if friend in sim[u1]:
			similarity = sim[u1][friend]
			try:
				for artist in train[friend]:
					if artist not in already_listened: # only consider new artists
						# weight recommendation by similarity and listen count
						weight = similarity * train[friend][artist]
						popular[artist] += weight
			except KeyError:
				pass

	# sort the defaultdict and return the 10 best recommendations
	return sorted(popular,key=popular.get,reverse=True)[:10]

def main():
	sim, friends, train, test = get_usersim(), get_friends(), get_train(), get_test()
	score = 0
	for line in test:
		user, artist = line.split()[:2]
		# get 10 recommended artists for every user
		recommended = recommend(sim, friends, train, user)
		hit = int(artist in recommended) # determine whether the artist was recommended/predicted or not
		score += hit
	print("Score: {} from {}\nAccuracy: {:.2f}%".format(score, len(test), 100*score/len(test)))

if __name__ == '__main__':
	main()