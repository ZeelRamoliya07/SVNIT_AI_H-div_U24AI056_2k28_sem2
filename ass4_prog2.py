import math as m

def squareroot(a,b):
	c=0
	for i in range(a,b+1):
		if m.sqrt(i)%1==0.0:
			c+=1
	return c
	
T=int(input())
l=[]
for i in range(T):
	no_pair=list(map(int,input().split()))
	l.append(no_pair)
print()
for i in l:
	print(squareroot(i[0],i[1]))