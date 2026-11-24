##BASIC TWO POINTER
##ARRAY SORTED
def two_pointer_sum(arr,target):
    i=0
    j=len(arr)-1
    while i <= j:
        x=arr[i]+arr[j]
        if x==target:
            return i,j
        elif x<target:
            i+=1
        else:
            j+=1
    return -1
##DRIVERS CODE
arr=[10,20,30,40,50]
target=70
result=two_pointer_sum(arr,target)
print(result)