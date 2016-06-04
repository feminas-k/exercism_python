def encode(s):
        r = ''
        if len(s)==0:
                return ''
        if len(s)==1:
                return s+''
        count = 1
        i = 1
        while i<len(s):
                if s[i]==s[i-1]:
                        count +=1
                else:
                        r = r+s[i-1]+str(count)
                        count = 1
                i+=1
        if count == 1:
                r = r+s[i-1]
        else:
                r=r+s[i-1]+str(count)
        r = r.replace('1','')
        return r

def decode(s):
	return
