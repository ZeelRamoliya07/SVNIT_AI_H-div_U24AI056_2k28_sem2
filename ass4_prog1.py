'''to make a string palindrome we can only decrease a character for example if there is "c" we can only make it "b", like we can not make it "d"'''
#This function takes the string as a input and return how many steps we have to do make it palindrome.
def palindrome(str):
	n=len(str)
	start,end,c=0,-1,0
	while(start<n//2):
		if(str[start]>str[end]):
			c+=(ord(str[start]))-(ord(str[end]))
		elif(str[end]>str[start]):
			c+=(ord(str[end]))-(ord(str[start]))
		start+=1
		end-=1
	return c

t=int(input()) #No of strings to be taken              
l=[]
for i in range(t):
	l.append(input())
print()
for i in l:
	print(palindrome(i))