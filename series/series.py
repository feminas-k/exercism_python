def slices(series,slicelength):
	if slicelength==0 or len(series)<slicelength:
		raise ValueError("Overly long or short slice!")

	elements=[]
	for i in range(len(series)-slicelength+1):
		elements.append(map(int,list(series[i:i+slicelength])))
	return elements

