 
def squareRoot(a) : 
    temp = a #a whose root we have to find
    l=0.00001
         
    while (1) :
          
        root = 0.5 * (temp + (a / temp))  
        if (abs(root - temp) < l): 
            break;  
        temp = root; 
    return root 

#taking input
a=int(input("ENTER THE VALUE FOR SQRT CALC -"))
ans=squareRoot(a)
print("square root of",a,"is",ans)          