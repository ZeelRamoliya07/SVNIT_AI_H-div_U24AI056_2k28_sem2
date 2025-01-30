word=input("Enter word of your choice")
result=[]
for i in range (len(word)):
    if i%2==0:
        result.append(word[i].lower())
    else:
        result.append(word[i].upper())
result1=''.join(result)
print(result1)    

    
    
    
    