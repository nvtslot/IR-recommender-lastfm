import pickle
from collections import Counter
from time import time

def get_training():
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
	with open("test.dat","r") as test:
		return test.readlines()

def recommend(sim, train, u1, n):
	#print(u1)
	already_listened = [] # will contain all artists that are already listened by the user
	try:
		for artist in train[u1]:
			already_listened.append((train[u1][artist],artist))
	except KeyError:
		pass
	top_n = sorted(already_listened,reverse=1)[:n]
	#print(top_n)
	popular = []
	for alr_tup in top_n:
		listencount = alr_tup[0]
		artist = alr_tup[1]
		scores = []
		try:
			for sim_artist in sim[artist]:
				similarity_score = sim[artist][sim_artist]
				scores.append((similarity_score,sim_artist))
		except KeyError:
			pass
		top_s = sorted(scores,reverse=1)[:n]
		#print(top_s)
		for sim_tup in top_s:
			similarity = sim_tup[0]
			similar_artist = sim_tup[1]

			weight = int(similarity*listencount)
			popular = popular + weight*[similar_artist]
	most_popular = [] # will contain the 10 most frequent artists from the popular list
	for popular_artist in Counter(popular).most_common(10):
		# count all frequencies in the list and form a top 10
		most_popular.append(popular_artist[0]) 
	return most_popular


def main():
	sim = pickle.load(open("item_sim01", "rb"))
	train = get_training()
	test = get_test()
	score = 0
	start = time()
	c =0
	for line in test:
		user, artist = line.split()[:2]
		# get 10 recommended vips for every user
		recommended = recommend(sim, train, user, n=10)
		hit = int(artist in recommended) # determine whether the vip was predicted or not
		score += hit
		if c % 500 == 0:
			print(c, time() - start)
		c+=1
	print("Score: {} from {}\nPercentage: {:.2f}%".format(score, len(test), 100*score/len(test)))

if __name__ == '__main__':
	main()