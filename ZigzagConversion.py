class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l=0
        height=0
        if numRows ==1 or numRows>=len(s):
            return s
        res=[]
        for i in range(numRows):
            res.append([])

        for i in range(len(s)):
            res[height].append(s[i])
            if height == 0:
                l=1
            elif height == numRows-1:
                l=-1
            height+=l
        for i in range(numRows):
            res[i] = ''.join(res[i])
        return ''.join(res)




