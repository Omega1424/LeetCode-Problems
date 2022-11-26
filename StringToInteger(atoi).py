class Solution:
    def myAtoi(self, s: str) -> int:
        res = 1
        s=s.strip()
        l=""
        i=0
        if not s:
            return 0
        if len(s)==1 and not s[0].isdigit():
            return 0
        if s[i]=='+':
            i+=1
        if s[i]=='-':
            i+=1
            res*=-1
        if i==2:
            return 0
        
        for x in range(i,len(s)):
            if not s[x].isnumeric():
                break
            elif s[x].isnumeric():
                l+=s[x]
        if l=="":
            return 0

        res*=float(l)
        if res<(-(2**31)):
            res=-(2**31)
        elif res>((2**31) - 1):
            res=(2**31)-1
        return int(round(res,0))
        
                
            