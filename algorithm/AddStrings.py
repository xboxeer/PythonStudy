class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1List = list(num1)
        num2List = list(num2)
        len1 = len(num1List)
        len2 = len(num2List)
        lenNum = len1 if len1 >= len2 else len2
        lenOutput = len1+1 if len1 >= len2 else len2+1
        result = [0]*lenOutput
        currentIndex = 0
        while (currentIndex <= lenNum):
            left=int(num1List[len1-currentIndex-1]) if len1-currentIndex-1>=0 else 0
            right=int(num2List[len2-currentIndex-1]) if len2-currentIndex-1 >=0 else 0
            addResult = left +right + result[lenOutput-currentIndex-1]
            if(lenOutput-currentIndex-2>=0):
                result[lenOutput-currentIndex-2] = 1 if addResult >= 10 else 0
            result[lenOutput-currentIndex-1] = addResult % 10
            currentIndex = currentIndex + 1
        resultStrList = [str(item) for item in result]
        if(resultStrList[0]=='0'):
            resultStrList=resultStrList[1:]
        return "".join(resultStrList)