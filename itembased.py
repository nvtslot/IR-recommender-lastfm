import sys
import operator
import linecache
import pickle

# open files
similaritems = pickle.load(open("item_sim01", "rb"))
#listens = open('user_artists.dat', 'r')
itemlisten = pickle.load(open("itemlisten", "rb"))
testfile = open("test.txt", "r")

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
	suggestions = {}
	similarband = {}
	for line in testfile:
		user, band, count = line.rstrip().split('\t')
		listensalready = itemlisten[user]
		for band in listensalready:
			try:
				similarband = similaritems[band]
				topNsimilarBands = sorted(similarband.items(),key=operator.itemgetter(1), reverse=True)
				
				
			except KeyError:
				pass
		
		for x in topNsimilarBands:
			if x[0] not in listensalready:
				print(user,x)
		#print(user, '\t', topNsimilarBands)
	
		




def main():
    index = indexFile(similaritems)
    #listendict = alreadyListens()
    doeiets = test(itemlisten,index, 10)


if __name__ == "__main__":
    main()
