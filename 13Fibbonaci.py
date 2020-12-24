
def fibbonaci(n):
    a=0
    b=1
    print("fibbonaci series-->")
    for i in range(1,n):
        c=a+b
        print(a)
        a=b
        b=c

#printing n terms of fibbonaci
n=int(input("Enter the no. of terms"))
fibbonaci(n)