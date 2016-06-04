def abbreviate(phrase):
        for x in [',','-']:
                if x in phrase:
                        phrase=phrase.replace(x,' ')
        acronym= ''
        for word in phrase.split():
                acronym += (word[0]).upper()
        return acronym

