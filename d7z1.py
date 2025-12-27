
#1
"""
#sp = [6, 2, 5, 4, 2, 5, 6]
sp = [7, 3, 2, 6, 5, 4, 7, 2, 8, 5, 9, 6]
qw = [1] * len(sp)

for i in range(1, len(sp)):
    for j in range(i):
        if sp[i] > sp[j]:
            if qw[j] + 1 > qw[i]:
                qw[i] = qw[j] + 1

len_posledo = max(qw)
otv = []
flag = False
for i in range(len(qw) - 1, -1, -1):
    if qw[i] == len_posledo:
        if flag == False or sp[i] < otv[-1]:
            otv.append(sp[i])
            len_posledo -= 1
            flag = True
otv.reverse()

print(qw)
print(*otv)
print(len(sp) - len(otv))
"""

#2
"""
len_sp = int(input())
sp = list(map(int, input().split()))
qw = [1] * len_sp

for i in range(1, len_sp):
    for j in range(i):
        if sp[i] > sp[j]:
            if qw[j] + 1 > qw[i]:
                qw[i] = qw[j] + 1
len_posled = max(qw)
otv = []
flag = False
for i in range(len(qw) - 1, -1, -1):
    if qw[i] == len_posled:
        if flag == False or sp[i] < otv[-1]:
            otv.append(sp[i])
            len_posled -= 1
            flag = True
otv.reverse()

print(*otv)
print(len(sp) - len(otv))
"""

