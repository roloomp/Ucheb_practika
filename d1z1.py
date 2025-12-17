# 1
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
    xr = abs(x1 - x2)
    yr = abs(y1 - y2)
    if (xr == 2 and yr == 1) or (xr == 1 and yr == 2):
        print("да")
    else:
        print("нет")
else:
    print("вышло за границы")
"""

#2
"""
k = int(input())
n = int(input())
summ = 0
for num in range(k, n + 1):
    if num % 2 == 0:
        summ += num
print(summ)
"""

#3
"""
summ = 0
while True:
    x = int(input())
    if x == 0:
        break
    summ += x
print(summ)
"""

#4
"""
n = int(input())
facto = 1
for num in range(1, n + 1):
    facto *= num
print(facto)
"""




