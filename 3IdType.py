#id() function return the Memory Address of veriable 
a="rohit"
b="rohit"
print("Address of a",id(a))
print("Address of b",id(b))
if(id(a)==id(b)):
    print("Same memory block is Shared by a and b var")

#type() it is used to identify which type of data is contained by the variable
c=[]
d={}
e=()
f=10
g=10.0
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))



