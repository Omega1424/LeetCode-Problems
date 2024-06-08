class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        l = list(s)
        total_shifts = [0]*len(l)
        
        #compute shifts for each 
        total=0
        for i in range(len(shifts)-1,-1,-1):
            total+=shifts[i]
            total_shifts[i]=total

        
        #do all shifts at once
        for i in range(len(l)):
            #calculate new position
            new_pos = (ord(l[i])-ord('a')+total_shifts[i])%26
            l[i] = chr(ord('a')+new_pos)
        return ''.join(l)

