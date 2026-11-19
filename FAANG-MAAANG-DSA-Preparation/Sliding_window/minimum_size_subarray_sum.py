##Minimum size subarray sum
##Time complexity-o(n)
##Space Complexity-o(1)

def minimum_size_subarray_sum(nums,target):
    left=0
    curr_sum=0
    min_len=float("inf")
    for right in range(len(nums)):
        curr_sum+=nums[right]
        while curr_sum>=target:
            min_len=min(min_len,right-left+1)
            curr_sum-=nums[left]
            left+=1
    return 0 if min_len==float("inf") else min_len
##Drivers code
nums=[2,3,1,2,4,3]
target=7
print(minimum_size_subarray_sum(nums,target))