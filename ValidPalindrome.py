class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=True
        l=[]
        for i in range(len(s)):
            if 65<=ord(s[i])<=90 or 97<=ord(s[i])<=122:
                l.append(s[i].lower())
            elif 48<=ord(s[i])<=57:
                l.append(s[i])
            else:
                continue
        for i in range(len(l)):
            if l[i]!=l[(len(l))-1-i]:
                res = False
            else:
                continue
        return res
            