if __name__ == '__main__':
 
 students = []
 scores = []
 
for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name, score])

mi = scores.sort()
ndmin = mi[1]

student = []
for i in students:
    for j in i:
        if j[1] == ndmin:
            student.append(j[0])
            
results = student.sort()

for i in results:
    print(i)
