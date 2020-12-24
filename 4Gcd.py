def gcd(a,b):
     if (a==0) :
         return b
     return gcd(b%a,a);

#Taking input 
a=int(input("Enter two number for GCD->"))
b=int(input("Enter two number for GCD->"))       
#calling gcd() function and printing ans
ans=gcd(a,b)
print("Gcd of",a,"&", b,"is = ",ans)
