#int ,float data type
a=int(input("Enter no:")) 
b=int(a)
c=float(a)

print(a,"in integer form:",b) 
print(a,"in float form",c)

#list data type

lst=[]
n=int(input("Enter the length of the list:")) 
for i in range(0,n):
     x=int(input("Enter value:")) 
     lst.append(x)

print("List is:") 
print(lst)

#String data type
String1 = 'Welcome everyone'
print("String with the use of Single Quotes: ") 
print(String1)
String1 = "Hello "
print("\nString with the use of Double Quotes: ") 
print(String1)
String1 = '''SVVV "Student"'''
print("\nString with the use of Triple Quotes: ") 
print(String1)
String1 = '''Students Studying
in SVVV'''
print("\nCreating a multiline String: ") 
print(String1)

#set data type
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)
set1 = set([1, 2, 'Hello', 4, 'SVVV', 6, 'Students']) 
print("\nSet with the use of Mixed Values")
print(set1)

# dictionary data type
Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict = dict({1: 'AAA', 2: 'BBB', 3:'CCC'})
print("\nDictionary with the use of dict(): ") 
print(Dict)
Dict = dict([(1, 'Hello'), (2, 'World')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict)
#tupule data type
tuple1 = (0, 1, 2, 3) 
tuple2 = ('Hello', 'world')
print("Concatenation of two tuples:") 
print(tuple1 + tuple2)
