class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways=0
        ahead1=0
        ahead2=0
        for i in range(n+1):
            if(i==1):
                ahead1=1
                ways=1
            elif(i==2):
                ahead2=2
                ways=2
            else:
                ways=ahead1+ahead2
                ahead1=ahead2
                ahead2=ways
        return ways