
x=[list(range(1,4)),list(range(4,7)),list(range(7,10))]
y=[list(range(10,13)),list(range(13,16)),list(range(16,19))]
result=[[0,0,0],[0,0,0],[0,0,0]]
print("Multiplication of",sep="\n",end="\n")
print("X=",x,sep="\n",end="\n")
print("Y",y,sep="\n",end="\n")

for i in range(len(x)):
   
   for j in range(len(y[0])):
       
       for k in range(len(y)):
           result[i][j] += x[i][k] * y[k][j]

print("is=",result,sep="\n")
