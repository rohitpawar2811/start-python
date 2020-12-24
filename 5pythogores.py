#distance=((x2-x1)^2 + (y2-y1)^2 )^(1/2)
import math
#taking input x1,y1,x2,y2

x1=int(input("Enter x1 and y1 ->"))
y1=int(input())
x2=int(input("Enter x2 and y2 ->"))
y2=int(input())
#print(x1,y1,x2,y2)

a=x2-x1
b=y2-y1
distance=math.sqrt(a**2 +b**2)
print(distance)
