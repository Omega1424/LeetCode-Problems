class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        map={}
        n=len(time)
        count=0
        res=[]
        for i in range(n):
            comp = (60-(time[i]%60))%60
            if comp in map:
                count+=map[comp]
            if time[i]%60 in map:
                map[time[i]%60]+=1
            else:
                map[time[i]%60]=1
        return count


if __name__ == "__main__":
    solution = Solution()  # Create an instance of the Solution class
    with open('user.out', 'w') as f:
        for case in map(loads, stdin):
            result = solution.numPairsDivisibleBy60(case)
            f.write(f"{result}\n")
    exit(0)