##BINARY SEARCH IN AN ARRAY
##SORTED ARRAY
##Time Complexity-o(log n)
##Space Complexity-o(1)
def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left +(right-left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right =mid - 1
    return -1
##DRIVERS CODE
arr=[10,20,30,40,50,60,70,80,90]
target=20
result=binary_search(arr,target)
print("Search Number Through Index:",result)
