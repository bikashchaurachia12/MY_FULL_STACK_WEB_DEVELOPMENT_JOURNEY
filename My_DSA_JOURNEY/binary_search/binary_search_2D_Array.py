##BINARY SEARCH IN A 2D ARRAY
##SORTED ARRAY
##TIME COMPLEXITY - o(log(R x C))
##SPACE COMPLEXITY - o(1)
def bin_sear_2d_array(arr,target):
    row=len(arr)
    column=len(arr[0])
    left=0
    right=row*column-1
    while left<=right:
        mid=left+(right-left)//2
        mid_element=arr[mid//column][mid%column]
        if mid_element==target:
            return mid
        elif mid_element<target:
            left = mid+1
        else:
            right = mid-1
    return -1
##DRIVERS CODE
arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=16
result=bin_sear_2d_array(arr,target)
print("Searching Element in a 2D array:",result)
