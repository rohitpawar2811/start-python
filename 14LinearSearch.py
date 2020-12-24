#Linear search programme

s=input("Enter the string -")
find=input("enter the char which you to find -")
index=-1
for i in range(len(s)):
    if s[i]==find :
         index=i
         break
print("Linear search for",find,"done",end=" ")
if index!=-1 :        
    print(" At index -",index+1)
else:
     print(" but ",find," not found -1 ")
