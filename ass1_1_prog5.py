list1=[]
temp=[]
for i in range(5):
    list1.append(input())
print("Only 15 characters was allowed")
for el in list1:
    temp.append(el[:15])
print(temp)
print("reversed names of students are")
for el1 in temp:
    print(el1[::-1])