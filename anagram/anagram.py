def detect_anagrams(w,l):
	subl = []
	for x in l:
		if x.lower() != w.lower() and sorted(x.lower()) == sorted(w.lower()):
			subl.append(x)
	return subl	
