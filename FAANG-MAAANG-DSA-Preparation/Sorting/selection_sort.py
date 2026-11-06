##Method Defination
##TC-o(n^2)
##SC-o(1)
def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
##Drivers Code
arr=[70,56,23,19,25,37,48]
result=selectionSort(arr)
print("Sorted Array:",result)