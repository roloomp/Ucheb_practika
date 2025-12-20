import csv

#1
"""
with open("36031.csv", "r") as f:
    n = list(csv.reader(f))
    l = []
    for i in range(len(n)):
        a = n[i][0].split(';')
        a = [int(el) for el in a]
        l.append(a)
l = l[::-1]
[i.reverse() for i in l]

for i in range(len(l)):
    for j in range(len(l[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            l[i][j] = l[i][j] + l[i][j - 1]
        elif i != 0 and j == 0:
            l[i][j] = l[i][j] + l[i - 1][j]
        else:
            l[i][j] = max(l[i - 1][j], l[i][j - 1]) + l[i][j]

put = []
i, j = -1, -1
while -len(l) - 1 < i < 0 and -len(l[i]) - 1 < j < 0:
    if i == -len(l) and j == -len(l[i]):
        break
    if i != -len(l) and j != -len(l[i]):
        if l[i - 1][j] < l[i][j - 1]:
            j -= 1
            put.append("L")
        else:
            i -= 1
            put.append("U")
    elif i == -len(l) and j != -len(l[i]):
        j -= 1
        put.append("L")
    elif j == -len(l[i]) and i != -len(l):
        i -= 1
        put.append("U")

l = l[::-1]
[i.reverse() for i in l]
[print(i) for i in l]
print(l[0][0],*put)
"""

#2
"""
with open ("59778.csv", "r") as f:
    n = list(csv.reader(f))
    l=[]
    for i in range(len(n)):
        a = [int(el) for el in n[i]]
        l.append(a)

c_strok=0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i].count(l[i][j])==4:
            repeat = l[i][j]
            x = []
            for j in range(len(l[i])):
                if l[i][j] not in x and l[i][j] != repeat:
                    x.append(l[i][j])
            summa_repeat = repeat * 4
            average_sum = sum(x) / 3
            if average_sum > summa_repeat:
                c_strok+=1
print(c_strok//4)
"""

#3
"""
with open("29666.csv", "r") as f:
    n = list(csv.reader(f))
    l = []
    for i in range(len(n)):
        n[i] = [float(el) for el in n[i]]
        l.append(n[i][0])

max_sum = 0
a = []

for i in range(len(l) - 1):
    if l[i] > l[i + 1]:
        a.append(l[i])
    else:
        a.append(l[i])
        summ = sum(a)
        if summ > max_sum:
            max_sum = summ
        a = []
        summ = 0
print(max_sum)
"""






















































































































