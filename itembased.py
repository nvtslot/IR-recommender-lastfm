# item based recommender on LAST.fm data
# Nik van 't Slot, Karel Beckeringh, Wessel Reijngoud

import pickle
from collections import Counter
from time import time

def get_training():
	"""Opens training dataset"""
	with open("train.dat","r") as data:
		training = {}
		for line in data.readlines():
			user, artist, count = line.strip().split("\t")
			try:
				training[user][artist] = int(count)
			except KeyError:
				training[user] = {}
				training[user][artist] = int(count)
	return training

def get_test():
	"""Opens test dataset"""
	with open("test.dat","r") as test:
		return test.readlines()

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
	
	popular = []

	# create top N similar artists for top N listened artists
	for listen_tup in topNlistened:
		listencount = listen_tup[0]
		artist = listen_tup[1]
		scores = []
		try:
			for sim_artist in sim[artist]:
				similarity_score = sim[artist][sim_artist]
				scores.append((similarity_score,sim_artist))
		except KeyError:
			pass
		topNsimilar = sorted(scores,reverse=1)[:n]
		
		# creates weight per similar band and add to popular list
		for similarity_tup in topNsimilar:
			similarity = similarity_tup[0]
			similar_artist = similarity_tup[1]
			weight = int(similarity*listencount) # creates a weight using similarity scores and listencount
			popular = popular + weight*[similar_artist]

	
		most_popular = [] # will contain the 10 most frequent artists from the popular list
	for popular_artist in Counter(popular).most_common(10):
		# count all frequencies in the list and form a top 10
		most_popular.append(popular_artist[0]) 
	return most_popular


def main():
	"""Runs recommendation program, took 15 min to complete on our laptop"""

	sim = pickle.load(open("item_sim01", "rb")) # opens item similarity file (23million lines)
	train = get_training()
	test = get_test()
	score = 0

	start = time() #used to time
	c =0

	for line in test:
		user, artist = line.split()[:2]
		# get 10 recommended artists for every user
		recommended = recommend(sim, train, user, n=10)
		hit = int(artist in recommended) # determine whether the vip was predicted or not
		score += hit
		if c % 500 == 0: # prints time per 500 users done.
			print(c, time() - start)
		c+=1

	print("Score: {} from {}\nPercentage: {:.2f}%".format(score, len(test), 100*score/len(test))) # prints in desired format

if __name__ == '__main__':
	main()
