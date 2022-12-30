class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomeNote=sorted(ransomNote)
        magazine=sorted(magazine)
        rcount={}
        mcount={}
        if len(ransomNote)>len(magazine):
            return False
            
        for i in range(len(magazine)):
            if i<len(ransomNote):
                rcount[ransomNote[i]]=1+rcount.get(ransomNote[i],0)
            mcount[magazine[i]]=1+mcount.get(magazine[i],0)
        print(rcount)
        print(mcount)
        for i in rcount:
            if i not in mcount:
                return False
            if rcount[i]>mcount[i]:
                return False
        return True