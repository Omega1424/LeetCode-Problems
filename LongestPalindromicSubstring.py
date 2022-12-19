class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=0
        out=''
        #oddlength
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>length:
                    out=s[l:r+1]
                    length=r-l+1
                l-=1
                r+=1
        #evenlength
        for i in range(len(s)):
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>length:
                    out=s[l:r+1]
                    length=r-l+1
                l-=1
                r+=1

        return out    