# user-based recommender on Last.FM data
# Nik van 't Slot, Karel Beckeringh, Wessel Reijngoud

import pickle
from collections import defaultdict

def get_train():
	"""Opens training dataset"""
	with open("train.dat","r") as data:
		train = {}
		for line in data.readlines():
			user, artist, count = line.strip().split("\t")
			try:
				train[user][artist] = int(count)
			except KeyError:
				train[user] = {}
				train[user][artist] = int(count)
	return train

def get_test():
	"""Opens test dataset"""
	with open("test.dat","r") as test:
		return test.readlines()

def recommend(sim, train, u1, n):
	"""For every user it creates a top n list containing the most similar users. The artists most listened to 
	by these similar users will be recommended, if not already followed by the user. The similarity score of 
	each similar user determines the weight of their recommendation."""
	scores = [] # will contain the similarity scores between the user and its similar users
	for u2 in sim[u1]:
		scores.append((sim[u1][u2],u2))

	already_listened = [] # will contain all artists that are already listened to by the user
	try:
		for artist in train[u1]:
			already_listened.append(artist)
	except KeyError:
		pass

	popular = defaultdict(int) # will contain each recommended artist and their cumulative weights
	top_n = sorted(scores,reverse=1)[:n]
	for tup in top_n:
		similarity, similar_user = tup
		try:
			for artist in train[similar_user]:
				if artist not in already_listened: # only consider new artists
					popular[artist] += similarity # weight recommendation by user similarity score
		except KeyError:
			pass

	# sort the defaultdict and return the 10 best recommendations
	return sorted(popular,key=popular.get,reverse=True)[:10]

def main():
	sim = pickle.load(open("user_sim01", "rb"))
	train, test = get_train(), get_test()
	score = 0
	for line in test:
		user, artist = line.split()[:2]
		# get 10 recommended artist for every user
		recommended = recommend(sim, train, user, n=10)
		hit = int(artist in recommended) # determine whether the artist was recommended/predicted or not
		score += hit
	print("Score: {} from {}\nAccuracy: {:.2f}%".format(score, len(test), 100*score/len(test)))

if __name__ == '__main__':
	main()