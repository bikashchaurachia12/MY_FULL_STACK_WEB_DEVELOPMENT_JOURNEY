##BINARY SEARCH IN AN ARRAY USING RECURSION
##SORTED ARRAY
##Time Complexity-o(log n)
##Space Complexity-o(1)
def binary_search(arr,target,left,right):
    while left <= right:
        mid = left +(right-left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr,target,mid+1,right)
        else:
            return binary_search(arr,target,left,mid-1)
    return -1
##DRIVERS CODE
arr=[10,20,30,40,50,60,70,80,90]
target=80
left = 0
right = len(arr)-1
result=binary_search(arr,target,left,right)
print("Search Number Through Index:",result)