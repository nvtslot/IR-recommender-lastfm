import sys
import operator
import linecache
import pickle

# open files
similaritems = pickle.load(open("item_sim01", "rb"))
#listens = open('user_artists.dat', 'r')
itemlisten = pickle.load(open("itemlisten", "rb"))
testfile = open("test.dat", "r")
trainingfile = open("train.dat", "r")

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

"""
#####FUNCTION NOT NEEDED ANYMORE AS IT IS NOW INCLUDED IN A PICKLE BUT PLEASE LEAVE HERE FOR CREATION OF NEW PICKLE.
def alreadyListens(listens):
	#creates a dict of key:value where key=user value=artist to show what artists user listens to already
	listendict = {}
	for line in listens.readlines()[1:]:
		
		user, artist, count = line.strip().split("\t")
		if user in listendict:
			listendict[user].append(artist)
		else:
			listendict[user] = [artist]
	pickle.dump(listendict, open("itemlisten", "wb"))
	#print(listendict)
	return listendict


"""
def recommend(sim, itemlisten,u1, n):
	scores = []
	already_listened = []
	similarartist = {}
	try:
		for artist in itemlisten[u1]:
			already_listened.append(artist) #user already listend to these artist
	except KeyError:
		pass
	try:
		for artist in already_listened:
			similarartist[u1] = similaritems[artist]
			
			
	except KeyError:
		pass
	
	print(u1,'\t',similarartist)
	
		


def main():
	sim = pickle.load(open("item_sim01", "rb"))
	training = get_training()
	test = get_test()
	score = 0
	for line in test:
		user, artist = line.split()[:2]
		# get 10 recommended vips for every user
		recommended = recommend(sim, training, user, n=10)
		#hit = int(artist in recommended) # determine whether the vip was predicted or not
		# print(user, vip, " ".join(most_popular), hit)
		#score += hit
	#print("Score: {} from {}\nPercentage: {:.2f}%".format(score, len(test), 100*score/len(test)))



if __name__ == "__main__":
    main()
