#taking input in list 
n=int(input("Enter size of list "))
list=[]
for i in range(n) :
    list.append(int(input("Enter elements")))

ans=max(list)
print(list,"Max of list is",ans,sep="\n")