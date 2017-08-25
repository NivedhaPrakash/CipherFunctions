>>> def func(m,n):
	m=m-1
	import string
	from itertools import combinations_with_replacement as cwr
	s=[y for y in string.ascii_lowercase]
	alphabet = string.ascii_lowercase
	length = 2
	c=["".join(comb) for comb in cwr(alphabet, length)]
	s.extend(c)
	for x in range(m,n):
		print s[x]

		
>>> func(25,29)