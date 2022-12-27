class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        window={}
        tcount = {}
        res,reslen=[-1,-1],float("infinity")
        for c in t:
            tcount[c] = 1+tcount.get(c,0)
        have,need = 0, len(tcount)
        l=0
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            if s[r] in tcount and tcount[s[r]]==window[s[r]]:
                have+=1     
            while have == need:
                if r-l+1<reslen:
                    res=[l,r]
                    reslen=r-l+1
                window[s[l]]-=1
                if s[l] in tcount and window[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1

        l,r=res
        return s[l:r+1] if reslen!= float("infinity") else  ""