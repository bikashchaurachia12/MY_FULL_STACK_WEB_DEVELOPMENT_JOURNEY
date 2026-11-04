##3 SUM PROBLEM
##UNSORTED DATA
##DRIVERS CODE
nums=[-1,0,1,2,-1,-4]
#Output=[[-1,-1,2],[-1.0,1]]

#Step 1-Sort the Data
def SUM_3(nums):
    nums.sort()
    ans=[]
    n=len(nums)
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        if nums[i]>0:
            break
        left=i+1
        right=n-1
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total==0:
                ans.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right-=1
            elif total<0:
                left+=1
            else:
                right-=1
    return ans

#Call the function
print(SUM_3(nums))