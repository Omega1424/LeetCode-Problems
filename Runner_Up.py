if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
arr1 = set(arr)
arr2=[x for x in arr1 if x!=max(arr1)]
print(max(arr2))