#indentation Error
# wrong code
"""
def multiply(a,b):
    mul=a*b
print(mul)     #indentation error here
              #print is out of the function
"""

#Right code
def multiply(a,b) :
    mul=a*b;
    print(a*b)

#taking input
a=int(input("enter 2 number for multi"))    
b=int(input())
multiply(a,b)