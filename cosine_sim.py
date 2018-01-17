import math

def cosine_sim(v1, v2):
	numer = 0
	dena = 0
	for key1 in v1:
		val1 = v1[key1]
		numer += val1*v2.get(key1,0)
		dena += val1**2
	denb = 0
	for val2 in v2.values():
		denb += val2**2
	return numer/math.sqrt(dena*denb) 