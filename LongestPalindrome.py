class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        l=list(s)
        l.sort()
        
        dict={}
        count=1
        oddcount=0
        if len(l)==1:
            return 1
        else:
            
            for i in range(1,len(l)):
                if l[i]==l[i-1]:
                    count+=1
                else:
                    dict.update({l[i-1]:count})
                    count=1
                if i==len(l)-1:
                    dict.update({l[i]:count})
            print(dict.items())
            count=0
            for i in dict:
                if len(dict)==1:
                    return dict[i]
                else:
                    if dict[i]%2 != 0:
                        if oddcount==0:
                            oddcount=dict[i]

                        count+=(dict[i]-1)
                    else:
                        count+=dict[i]
            if oddcount==0:
                return count
            else:
                count+=1
                return count
                
                
            