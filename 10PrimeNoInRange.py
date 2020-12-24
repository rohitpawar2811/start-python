#prime number in Range

def PrimeSeive(n,list):
    prime = [True for i in range(0,n + 1,1)]
    for i in range(3,n+1,2) :  # we are not checking for
      #  even as we know all even is non prime except 2
        if(prime[i]==True): 
            list.insert(0,i)
            for j in range(i*i,n+1,i):
                prime[j]=False
                 
    list.insert(0,2)
    list.sort()
    return list
#taking input            
a=int(input("Enter the range upto which you have to find prime number"))
list=[]
list=PrimeSeive(a,list)
print(list)

   
