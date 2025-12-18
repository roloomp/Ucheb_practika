# 1
"""
with open('39762.txt', 'r') as f:
    n = f.readlines()
    n = [int(e1) for e1 in n]
    print(n)
co = 0
max_sum = 0
for i in range(len(n) - 1):
    a = n[i]
    b = n[i + 1]
    if (a * b) % 15 == 0 and (a + b) % 7 == 0:
        co += 1
        if (a + b) > max_sum:
            max_sum = a + b
print(co)
print(max_sum)
"""

# 2
"""
with open('68279.txt', 'r') as f:
    n = f.readlines()
    n = [int(e1) for e1 in n]

co = 0
max_sum = 0
max_num = 0
for num in n:
    if num % 1000 == 562:
        if num > max_num:
            max_num = num
for i in range(len(n) - 3):
    z = n[i]
    x = n[i + 1]
    c = n[i + 2]
    v = n[i + 3]

    a = 10000 <= z <= 99999
    s = 10000 <= x <= 99999
    d = 10000 <= c <= 99999
    f = 10000 <= v <= 99999
    co5 = a + s + d + f
    if not (co5 < 1 or co5 > 2):
        co3 = (z % 3 == 0) + (x % 3 == 0) + (c % 3 == 0) + (v % 3 == 0)
        co7 = (z % 7 == 0) + (x % 7 == 0) + (c % 7 == 0) + (v % 7 == 0)
        if co3 < co7:
            total = z + x + c + v
            if max_num < total < 2 * max_num:
                co += 1
                if (z + x + c + v) > max_sum:
                    max_sum = z + x + c + v

print(co)
print(max_sum)
"""

# 3

with open('40992.txt', 'r') as f:
    n = f.readlines()
    n = [int(e1) for e1 in n]

co = 0
max_sum = 0
col = 0
sr = 0
for i in n:
    if i % 2 == 1:
        col += 1
        sr += i
sr = sr // col

for i in range(len(n) - 1):
    a = n[i]
    b = n[i + 1]
    if (a % 5 == 0 or b % 5 == 0) and (a < sr or b < sr):
        co += 1
        if max_sum < (a + b):
            max_sum = (a + b)
print(co, max_sum)