s=input("Enter a string")
d={}
for i in range(0,len(s)):
   if(s[i] in d):
       d[s[i]]+=1
   else:
        d[s[i]]=1

print(d)          
    
