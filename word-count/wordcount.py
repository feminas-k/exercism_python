def word_count(phrase):
	for x in ['_',',','.','!','&','@','$','%','^',':']:
		if x in phrase:
			phrase=phrase.replace(x,' ')	
	phrase = phrase.lower()
	phrase_words = phrase.split()
	new_dict = {}
	for word in phrase_words:
		if word not in new_dict:
			new_dict[word] = 1
		else:
			new_dict[word] += 1
	return new_dict
