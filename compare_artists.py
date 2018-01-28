import pickle
import math
from cosine_sim import cosine_sim


def main():
	itemsim = {}
	tagged = pickle.load(open("tagged", "rb"))
	c = 1
	for a1 in tagged:
		for a2 in tagged:
			if c % 1000000 == 0:
				print(c/1000000,"M")
			#DONT compare same artists
			if int(a2) > int(a1):
				score = cosine_sim(tagged[a1],tagged[a2])
				#only include cosine similarities higher than a certain threshold
				if score > 0.50:
					try:
						itemsim[a1][a2] = score
					except KeyError:
						itemsim[a1] = {}
						itemsim[a1][a2] = score
					try:
						itemsim[a2][a1] = score
					except KeyError:
						itemsim[a2] = {}
						itemsim[a2][a1] = score
			c+=1

	pickle.dump(itemsim, open("item_sim50", "wb"))
		
	
	

if __name__ == '__main__':
	main()