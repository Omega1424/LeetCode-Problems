# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         if len(p)>len(s):
#            return []
#         pcount, scount = {}, {}
#         for i in range(len(p)):
#             pcount[p[i]]=1+pcount.get(p[i],0)
#             scount[s[i]]=1+scount.get(s[i],0)
#         res = [0] if scount == pcount else []
#         l = 0
#         for r in range(len(p),len(s)):
#             scount[s[r]]=1+scount.get(s[r],0)
#             scount[s[l]]-=1
#             if scount[s[l]]==0:
#                 scount.pop(s[l])
#             l+=1
#             if scount == pcount:
#                 res.append(l)
#         return res
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        x=len(p)
        dict=defaultdict(int)
        
        for i in p:
            dict[i]+=1
        res=[]
        dict1=defaultdict(int)
        for i in range(x):
            if i<len(s):
                dict1[s[i]]+=1
        if dict1==dict:
            res.append(0)
        for i in range(1,len(s)-x+1):
            dict1[s[i-1]]-=1
            if dict1[s[i-1]]==0:
                del dict1[s[i-1]]
            dict1[s[i+x-1]]+=1
            if dict1==dict:
                res.append(i)
        return res
