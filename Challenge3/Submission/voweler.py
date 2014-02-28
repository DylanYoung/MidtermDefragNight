
dictionary = 'words'
vowels = ['a','e','o','u','i']

def createDictionary(dictionary, match):
	dic = []
	strings = [x.strip() for x in dictionary.split('\n')]
	for word in strings:
		#print(word)
		exword = exvowel(word)
		if exword[0].lower() in match[0].lower() and  \
		exword[1].lower() in match[1].lower():
			dic.append((exword[0],exword[1], word))
	return dic

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

def envowel(strings):
	global dictionary
	f = open(dictionary, 'r')
	dic = f.read()
	f.close()
	dic = createDictionary(dic, strings)
	l = words(strings, dic)
	l = [x for x in l if len([z for z in x if not z == " "]) == len(strings[0])+len(strings[1])]
	return l

def words(strings, dic):
	l = []
	for i in range(1,len(strings[0])+1):
		for j in range(1,len(strings[1])+1):
			for word in dic:
				if (strings[0][:i].lower() == word[0].lower()): 
					if (strings[1][:j].lower() == word[1].lower()):
						#if len(strings[1][j:]) == 0:
						#	l.append(word[2])
						#else: 
							completions = words((strings[0][i:], strings[1][j:]),dic)
							for completion in completions:
								l.append(word[2] + " " + completion)

	return l



def main():
	string = raw_input("Enter a string to exvowel: ")
	o = exvowel(string)
	print o[0]
	print o[1]

	l = envowel(o)

	print "It will now be envoweled"

	for phrase in l:
		print phrase








if __name__ == "__main__":
    main()

		