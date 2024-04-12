class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        min=9999
        shortest=""
        for i in strs:
            if len(i)<min:
                min=len(i)
                shortest=i
        for i in range(min):
            for j in strs:
                if j[i]!=shortest[i]:
                    return res
            res+=shortest[i]
        return res

        