class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length=len(nums)
        maxNum=nums[0]
        current=nums[0]
        for i in range(1,length):
            current=max(current+nums[i],nums[i])
            maxNum=max(current,maxNum)
        return maxNum
temp=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(temp.maxSubArray(nums))