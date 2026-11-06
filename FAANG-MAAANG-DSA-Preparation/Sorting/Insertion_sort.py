##Method Defination
##TC-o(n^2)
##SC-o(1)
def insertionSort(arr):
    for i in range(1,len(arr)):
        j=i-1
        key=arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
##Drivers Code
arr=[75,90,100,95,85,80]
result=insertionSort(arr)
print("Sorted Array:",result)
