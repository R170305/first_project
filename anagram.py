def check(s1,s2):
	if(sorted(s1)==sorted(s2)):
		print("the srtings are anagrams")
	else:	
		print("the strings are not anagrams")
s1="abcc"
s2="cabc"
check(s1,s2)
