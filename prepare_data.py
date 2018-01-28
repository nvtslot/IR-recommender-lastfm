import pickle
import codecs

def get_artist_ID():
	try:
		return pickle.load(open("artist_ID", "rb"))
	except FileNotFoundError:
		artist_ID = {}
		with open("artists.dat", "r") as data:
			for line in data.readlines():
				ID, artist = line.split("\t")[:2]
				artist_ID[ID] = artist
		pickle.dump(artist_ID, open("artist_ID", "wb"))
		return artist_ID

def get_tag_ID():
	try:
		return pickle.load(open("tag_ID", "rb"))
	except FileNotFoundError:
		tag_ID = {}
		with codecs.open("tags.dat", "r", encoding='utf-8', errors='ignore') as data:
			for line in data.readlines():
				ID, tag = line.split("\t")[:2]
				tag_ID[ID] = tag.strip()
		pickle.dump(tag_ID, open("tag_ID", "wb"))
		return tag_ID

def get_tagged():
	try:
		return pickle.load(open("tagged", "rb"))
	except FileNotFoundError:
		tagged = {}
		with open("user_taggedartists.dat", "r") as data:
			for line in data.readlines()[1:]:
				artist, tag = line.split("\t")[1:3]
				if artist not in tagged:
					tagged[artist] = {}
				if tag in tagged[artist]:
					tagged[artist][tag] += 1
				else:
					tagged[artist][tag] = 1
		pickle.dump(tagged, open("tagged", "wb"))
		return tagged

def main():
	#artist_ID = get_artist_ID()
	#tag_ID = get_tag_ID()
	tagged = get_tagged()
	"""i = "1642"
				print(artist_ID[i])
				for x in tagged[i]:
					print(tagged[i][x], tag_ID[x])"""

if __name__ == '__main__':
	main()