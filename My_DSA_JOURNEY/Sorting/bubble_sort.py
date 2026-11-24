##BUBBLE SORT
##TC-o(n^2)
##SC-o(1)
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                ##Swap the element
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
##DRIVERS CODE
arr=[70,20,50,60,35,47]
result=bubblesort(arr)
print("Bubble Sorted Data:",result)