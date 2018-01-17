class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        ret=0
        i=0
        while(i<len(cost)-1):
            carry=cost[-1-i] if cost[-1-i]<cost[-2-i] else cost[-2-i]
            ret=ret+carry
            i=i+2 if cost[-1-i]>cost[-2-i] else i+1
        return ret
temp=Solution()
costs=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(temp.minCostClimbingStairs(costs))
