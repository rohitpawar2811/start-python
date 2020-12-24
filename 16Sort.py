#selection sort logic 
def selectionSort(l):
    for k in range(0,len(l)):
        min=k    
        for j in range(k+1,len(l)):
            if l[min]>l[j] :
                min=j
        #swap
        temp=l[min]
        l[min]=l[k]
        l[k]=temp
    return l    

def insertionSort(arr): 

    for i in range(1, len(arr)): 
  
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key
    return arr 

def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r)
    return arr         

def merge(arr,l,m,r):
     n1 = m - l + 1
     n2 = r- m 
     L = [0] * (n1) 
     R = [0] * (n2) 
     for i in range(0 , n1): 
        L[i] = arr[l + i] 

     for j in range(0 , n2): 
        R[j] = arr[m + 1 + j]           
     i = 0 
     j = 0     
     k = l     
     while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
     while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
     while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
#taking input in the list
n=int(input("Enter size of list "))
list=[]
for i in range(n) :
    list.append(int(input("Enter elements")))
print("sorting list-->",list)    
l=selectionSort(list)  
print("sorted list by selection sort",l)
l=insertionSort(list) 
print("sorted list by Insertion sort",l)  
l=mergeSort(list,0,len(list)-1)    
print("sorted list by Merge sort",l)  

