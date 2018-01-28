# friend-based recommender on Last.FM data
# Nik van 't Slot, Karel Beckeringh, Wessel Reijngoud

import pickle
from collections import defaultdict

def get_friends():
	try:
		return pickle.load(open("friends", "r"))
	except FileNotFoundError:
		friends = {}
		with open("user_friends.dat", "r", encoding='utf-8', errors='ignore') as data:
			for line in data.readlines()[1:]:
				user, friend = line.strip().split()
				try:
					friends[user][friend] = True
				except KeyError:
					friends[user] = {}
					friends[user][friend] = True
				try:
					friends[friend][user] = True
				except KeyError:
					friends[friend] = {}
					friends[friend][user] = True	
		pickle.dump(friends, open("friends", "wb"))
		return friends

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

def recommend(friends, train, u1):
	"""For every user it looks up their friends. The artists most listened to by these friends 
	will be recommended, if not already followed by the user. The listen count for each artist
	determines the weight of the recommendation."""
	already_listened = [] # will contain all artists that are already listened to by the user
	try:
		for artist in train[u1]:
			already_listened.append(artist)
	except KeyError:
		pass

	popular = defaultdict(int) # will contain each recommended artist and their cumulative weights
	for friend in friends[u1]:
		try:
			for artist in train[friend]:
				if artist not in already_listened: # only consider new artists
					weight = train[friend][artist] # weight recommendation by listen count
					popular[artist] += weight
		except KeyError:
			pass

	# sort the defaultdict and return the 10 best recommendations
	return sorted(popular,key=popular.get,reverse=True)[:10]

def main():
	friends = get_friends()
	train = get_train()
	test = get_test()
	score = 0
	for line in test:
		user, artist = line.split()[:2]
		# get 10 recommended artists for every user
		recommended = recommend(friends, train, user)
		hit = int(artist in recommended) # determine whether the artist was recommended/predicted or not
		score += hit
	print("Score: {} from {}\nAccuracy: {:.2f}%".format(score, len(test), 100*score/len(test)))

if __name__ == '__main__':
	main()