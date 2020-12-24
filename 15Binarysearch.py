#BinarySearch -:it is only applied when int sequence is sorted.
#finding key in the List of Integer sir.
def BinarySearch(l,key):
    n=len(l)
    left=0
    right=n-1
    mid=(left+right//2)
    while(left<=right):
       
        if l[mid]<key :
             left=mid+1
        elif l[mid]>key :
            right=mid-1
        else:
            return mid
        mid=(left+right)//2    
    
    return -1


#taking input in the list
n=int(input("Enter size of list "))
list=[]
for i in range(n) :
    list.append(int(input("Enter elements")))
key=int(input("Enter the key"))
list.sort();
print(list);
index=BinarySearch(list,key) 
print("BINARY SEARCH HAS BEEN DONE") 
if index==-1:
    print("key not exist's")
else:
    print("KEY INDEX=",index+1)

