list =[]
def swap_case(s):
    for i in s:
        if i.isupper():
            list.append(i.lower())
        elif i.islower():
            list.append(i.upper())
        else:
            list.append(i)
    string = ''.join(list)
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)