class Solution:
    def intToRoman(self, num: int) -> str:
        res=""
        dic={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        while num//1000>0:
            res+=dic[1000]
            num=num-1000
        while num//900>0:
            res+=dic[900]
            num=num-900
        while num//500>0:
            res+=dic[500]
            num=num-500
        while num//400>0:
            res+=dic[400]
            num=num-400
        while num//100>0:
            res+=dic[100]
            num=num-100
        while num//90>0:
            res+=dic[90]
            num=num-90
        while num//50>0:
            res+=dic[50]
            num=num-50
        while num//40>0:
            res+=dic[40]
            num=num-40
        while num//10>0:
            res+=dic[10]
            num=num-10
        while num//9>0:
            res+=dic[9]
            num=num-9
        while num//5>0:
            res+=dic[5]
            num=num-5
        while num//4>0:
            res+=dic[4]
            num=num-4
        if num>0:
            for i in range(num):
                res+="I"
        return res

