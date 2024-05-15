class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dict={  '2':['a','b','c'],'3':['d','e','f'],
                '4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
                '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res=[""]
        for digit in digits:
            new = []
            for i in res:
                for j in dict[digit]:
                    new.append(i+j)
            res = new
        return res


        

            
        