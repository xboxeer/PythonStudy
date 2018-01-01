class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroStartIndex=-1
        currentIndex=0
        count=len(nums)
        while(currentIndex<count):
            if(nums[currentIndex]==0 and zeroStartIndex<0):
                zeroStartIndex=currentIndex
            elif(nums[currentIndex]!=0 and zeroStartIndex>=0):
              nums[zeroStartIndex]=nums[currentIndex]
              nums[currentIndex]=0  
              zeroStartIndex=zeroStartIndex+1  
            currentIndex=currentIndex+1

#nums = [0, 1, 0, 3, 12,0,2,5,2,0,3,0,3,2,1,0,1,0,0,0,0,1]
nums=[0]
temp=Solution()
temp.moveZeroes(nums)
print(nums)