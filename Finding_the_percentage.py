if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for x in student_marks[query_name]:
        sum +=x
    average = float(sum/3)
    rnd = "{:.2f}".format(average)
    print(rnd)