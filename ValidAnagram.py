class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        s.sort()
        t=list(t)
        t.sort()
        if s==t:
            return True
        else:
            return False
                
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.lower()
        t=t.lower()
        s1=[]
        t1=[]
        for i in range(len(s)):
            if ord('a')<=ord(s[i])<=ord('z'):
                s1.append(s[i])
            else:
                continue
        for i in range(len(t)):
            if ord('a')<=ord(t[i])<=ord('z'):
                t1.append(t[i])
            else:
                continue
        t1.sort()
        s1.sort()
        if t1==s1:
            return True
        else:
            return False