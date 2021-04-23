import textwrap

def wrap(string, max_width):
    list1=[]
    for i in range(0,len(string),max_width):
        list1.append(string[i:i+max_width])
        
    return '\n'.join(list1)
        
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)