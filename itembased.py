import sys
import operator
import linecache
import pickle

# open files
similaritems = pickle.load(open("item_sim01", "rb"))
####listens = open('user_artists.dat', 'r')
itemlisten = pickle.load(open("itemlisten", "rb"))

def indexFile(similaritems):
	"""indexes the file so that it is faster afterwards"""
	nr = 1
	index = {}
	for line in similaritems:
		BAND1 = line.split(' ')[0]
		if (BAND1 not in index):
			index[BAND1] = [nr]
		else:
			index[BAND1].append(nr)
		nr += 1

	return index

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


def test(itemlisten,index,n):
	for testcase in itemlisten:
		print(itemlisten[testcase])

	

def main():
    index = indexFile(similaritems)
    #listendict = alreadyListens(listens)
    doeiets = test(itemlisten,index, 20)


if __name__ == "__main__":
    main()
