#Given an array of integers arr of size N and a number k.Return 
# the maximum sum of a subarray of size k.
#Time Complexity-o(n)
#Space Complexity-o(1)
def maximum_sum_subarray(arr,k):
    sum=0
    i=0
    while i <k:
        sum+=arr[i]
        i+=1
    ans=sum
    while i<len(arr):
        sum-=arr[i-k]
        sum+=arr[i]
        ans=max(ans,sum)
        i+=1
    return ans
##Drivers Code
arr=[100,200,300,400,500]
k=2
print(maximum_sum_subarray(arr,k))