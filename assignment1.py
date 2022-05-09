import random
import time


def createArray(n):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(0, n*10))
    return rand_list

def partitioning(arr, l, h):
    i = l
    j = h - 1
    p = random.randint(l,h)
    pivot=arr[p]
    arr[h], arr[p] = arr[p], arr[h]
    while i < j:
        while (i < h) and arr[i] < pivot:
            i = i + 1
        while (j > l) and arr[j] >=pivot:
            j = j - 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i],arr[h]= arr[h], arr[i]
    return i

def quicksort ( arr , l ,h ):
    begin = time.time()
    if l <h :
        index=partitioning(arr,l,h)
        quicksort(arr,l,index-1)
        quicksort(arr,index+1,h)
  #  time.sleep(0.2)
    end = time.time()
    return end-begin

def selectionsort(list):
    begin = time.time()
    n=len(list)
    for i in range (n-1):
        min = i
        for j in range (i+1,n):
            if ( list[j]<list[min]):
                min =j
        temp=list[i]
        list[i]=list[min]
        list[min]=temp
       # print (list)
   # time.sleep(0.2)
    end = time.time()
    return end - begin

def mergeSort(arr):
    begin = time.time()
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    #time.sleep(0.1)
    end = time.time()
    return end - begin

def insertionsort (arr):
    begin = time.time()
    for i in range (1, len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
   # time.sleep(0.2)
    end = time.time()
    return end - begin

def hybrid(arr,threshold):
    begin = time.time()
   # print(arr)
    if len(arr) <= threshold:
       selectionsort(arr)
    else :
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        hybrid(left,threshold)
        hybrid(right,threshold)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    #time.sleep(0.1)
    end = time.time()
    return end - begin

def findN(arr,l,h,k):
    i=partitioning(arr,l,h)
    if i==k:
        print(f"the {k}th smallest element is {arr[i-1]}")
    else :
        if k>i:
            findN(arr,i+1,h,k)
        else :
            findN(arr,l,i-1,k)


arr=createArray(1000)
print(arr)
k=4
findN(arr,0,len(arr)-1,k)
print("**************************************")

list =createArray(1000)
t=selectionsort(list)
print(list)
print (f"execution time of selection sort {t}")
print("**************************************")

arr = createArray(1000)
f=quicksort ( arr , 0 , len(arr)-1)
print(arr)
print (f"execution time of quick sort {f}")
print("**************************************")

arr=createArray(1000)
h=insertionsort(arr)
print(arr)
print (f"execution time of insertion sort {h}")
print("**************************************")

arr =createArray(1000)
k=mergeSort(arr)
print(arr)
print(f"Total runtime of the merge sort is {k}")
print("**************************************")

arr =createArray(1000)
threshold=5
k=hybrid(arr,threshold)
print(arr)
print(f"Total runtime of the hybrid sort is {k}")