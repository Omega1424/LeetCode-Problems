if __name__ == '__main__':
    list=[]
    scores =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name,score])
        scores.append(score)
    list.sort(key= lambda x:x[1])
    scores.sort()
    list1=[]
    scores1=[]
    for student_ in list:
        if student_[1]!= min(scores):
            list1.append(student_)
            scores1.append(student_[1])
            
    
            
    final_list =[]

    for student in list1:
        if student[1] ==min(scores1):
            final_list.append(student[0])
    final_list.sort()
    for x in final_list:
        print (x)