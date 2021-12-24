if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score , name])
    first = min(students , key=lambda x:x[0])
    for stu in  range(len(students)):
        lowest = min(students , key=lambda x: x[0])
        if(lowest[0] == first[0]):
            students.remove(lowest)
        else:
            break;
    lowestStudents = [x for x in students if(x[0] == lowest[0])]
    lowestStudents.sort()
    for student in lowestStudents:
        print(student[1])
