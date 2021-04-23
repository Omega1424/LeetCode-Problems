if __name__ == '__main__':
    s = input()
    str1=()
    str2=()
    str3=()
    str4=()
    str5=()
    for i in range(0,len(s)):
        if s[i].isalnum() ==True:
            str1=(True)
            break
        else:
            str1=(False)
    for i in range(0,len(s)):
        if s[i].isalpha() ==True:
            str2=(True)
            break
        else:
            str2=(False)
    for i in range(0,len(s)):
        if s[i].isdigit() ==True:
            str3=(True)
            break
        else:
            str3=(False)
    for i in range(0,len(s)):
        if s[i].islower() ==True:
            str4=(True)
            break
        else:
            str4=(False)
    for i in range(0,len(s)):
        if s[i].isupper() ==True:
            str5=(True)
            break
        else:
            str5=(False)
    print(str1)
    print(str2)
    print(str3)
    print(str4)
    print(str5)
