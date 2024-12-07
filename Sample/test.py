

import random
#random.shuffle(mylist)



f=open('msg.txt')
lines=f.readlines()
for line in lines:
	l=line.split()
	#print(l)
	random.shuffle(l)
	l=l[3:]
	#print(l)

	s=''
	for l1 in l:
		s+=' '+l1
	print(s)


