
dictionary = 'words'  #'enable1.txt'
vowels = ['a','e','o','u','i']

def createDictionary(dictionary, match):
	validV = ['a','i','u']
	validC = ['r','y']
	dic = set()
	strings = [x.strip() for x in dictionary.split('\n')]
	for word in strings:
		#print(word)
		exword = exvowel(word.lower())
		if exword[0] in match[0] and  \
		exword[1] in match[1]:
			if len(exword[0]) > 1 or exword[0] in validC\
				 or len(exword[1]) > 1 or exword[1] in validV or len(word) > 1:
					dic.add((exword[0],exword[1], word.lower()))
	return list(dic)

def exvowel(string):
	global vowels
	string = string.split()
	vowelString = []
	consString = []
	for word in string:
		for letter in word:
			if letter in vowels:
				vowelString.append(letter)
			else: 
				consString.append(letter)
	return ''.join(consString),''.join(vowelString)

def envowel(strings, df=dictionary):
	global dictionary
	f = open(df, 'r')
	dic = f.read()
	f.close()
	dic = createDictionary(dic, strings)
	#print dic
	l = words(strings, dic)
	#l = [x for x in l if len([z for z in x if not z == " "]) == len(strings[0])+len(strings[1])]
	return l

def words(strings, dic):
	l = []
	doneV = False

	rI = range(1,len(strings[0])+1)
	if len(rI) == 0: rI = [0]
	#if strings[1] == '': rJ = [1]
	rJ = range(1,len(strings[1])+1)

	for i in rI:
		if not i == 0:
			restrictedI = [x for x in dic if x[0] == strings[0][:i]]
			compC = strings[0][i:] if not strings[0] == '' else strings[0]

		for j in rJ:
			compV = strings[1][j:] if not strings[1] == '' else strings[1]

			if not i == 0:
				validWords = [x[2] for x in restrictedI if x[1] == strings[1][:j]]
				complete(compC,compV,dic,validWords, l)

			if not doneV:
				validWords = [x[2] for x in dic if x[1] ==  strings[1][:j].lower() and x[0] == '']
				complete(strings[0],compV,dic,validWords, l)
		
		doneV = True
		if not i == 0: 
			validWords = [x[2] for x in restrictedI if x[1] == '']
			compV = strings[1]
			complete(compC,compV,dic,validWords, l)	

	return l


def complete(compC, compV, dic, validWords, l):
	newDic = []
	if not (compV == '' and compC == ''):
		newDic = [w for w in dic if w[0] in compC and w[1] in compV]
		if not len(newDic) == 0:
			completions = words((compC, compV),newDic)
			if not len(completions) == 0:
				for w in validWords:
					for completion in completions:
						l.append(w + " " + completion)
	else: 
		for w in validWords:
			l.append(w)



def main():
	global dictionary
	df = raw_input("Enter a dictionary file (nothing for default): ")
	if df == '': df = dictionary
	else: df = df
	string = raw_input("Enter a string to exvowel: ")
	o = exvowel(string)
	print o[0]
	print o[1]

	print "It will now be envoweled: "
	l = envowel(o, df)

	for phrase in l:
		print phrase








if __name__ == "__main__":
    main()

		