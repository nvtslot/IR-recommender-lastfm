# random recommender on Last.FM data
# used as a reference frame for our other recommenders
# Nik van 't Slot, Karel Beckeringh, Wessel Reijngoud

from random import shuffle
from get import  get_train, get_test

def main():
	train, test = get_train(), get_test()
	all_artists = list(train)
	score = 0
	for line in test:
		user, artist = line.split()[:2]
		# get 10 random artists for every user
		shuffle(all_artists)
		recommended = all_artists[:10]
		hit = int(artist in recommended) # determine whether the artist was recommended/predicted or not
		score += hit
	print("Score: {} from {}\nAccuracy: {:.2f}%".format(score, len(test), 100*score/len(test)))

if __name__ == '__main__':
	main()