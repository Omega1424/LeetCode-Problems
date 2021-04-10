#Problem Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arr = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                arr2 = [i,j,k]
                if (i+j+k !=n): 
                    arr.append(arr2)
            
    print (arr)