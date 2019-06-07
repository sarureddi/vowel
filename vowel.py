n22=input()
c2=0
l2=['a','e','i','o','u','A','E','I','O','U']
for i2 in n22:
	if i2 in l2:
		c2=c2+1
		break
if(c2>0):
	print('yes')
else:
	print('no')
