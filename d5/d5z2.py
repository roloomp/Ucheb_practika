
#1
"""
with open('27686.txt', 'r') as f:
    n = f.readlines()
max_count = 0
count_x = 0
for i in range(len(n[0])):
    if max_count < count_x:
        max_count = count_x
    if n[0][i] == 'X':
        count_x += 1
    else:
        count_x = 0
print(max_count)
"""

#2
"""
with open('36037.txt', 'r') as f:
    n = f.readlines()
max_count = 0
count_x = 0
for i in range(len(n[0]) - 3):
    if max_count < count_x:
        max_count = count_x
    if not (n[0][i:i+4] == 'XZZY'):
        count_x += 1
    else:
        count_x = 0
if not (n[0][-4:] == 'XZZY'):
    max_count += 3
print(max_count)
"""

#3
"""
with open('46982.txt', 'r') as f:
    n = f.readlines()
    n = n[0]
count = 0
for i in range(len(n)):
    if n[i] == 'E':
        for j in range(i + 1, len(n)):
            if n[j] == 'F':
                break
            elif n[j] == 'E':
                if j - i + 1 >= 12:
                    count += 1
                break
print(count)
"""