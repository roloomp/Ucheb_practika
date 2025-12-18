
#1
"""
def fibonachi(n):
    if n <= 1:
        return n
    l = [0, 1]
    for p in range(n - 1):
        l_n = l[0] + l[1]
        l[0] = l[1]
        l[1] = l_n
    return l[1]
z = int(input())
print(fibonachi(z))
"""

#2
"""
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n == 3:
    print(4)
else:
    l = [1, 2, 4]
    for i in range(n - 3):
        new = l[0] + l[1] + l[2]
        l[0] = l[1]
        l[1] = l[2]
        l[2] = new
    print(l[2])
"""

#3
"""
coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0,0, 0, 1]
    ]

for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            coins[i][j] = coins[i][j] + coins[i][j - 1]
        elif i != 0 and j == 0:
            coins[i][j] = coins[i][j] + coins[i - 1][j]
        else:
            coins[i][j] = max(coins[i - 1][j], coins[i][j - 1]) + coins[i][j]
print(coins[i][j])
"""

#3.2
"""
coins = [
    [0, 1, 1],
    [2, 1, 0],
    [4, 1, 1]
    ]
for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            coins[i][j] = coins[i][j] + coins[i][j - 1]
        elif i != 0 and j == 0:
            coins[i][j] = coins[i][j] + coins[i - 1][j]
        else:
            coins[i][j] = max(coins[i - 1][j], coins[i][j - 1]) + coins[i][j]
print(coins[i][j])
"""

#3.3
"""
coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0,0, 0, 1]
    ]
for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            coins[i][j] = coins[i][j] + coins[i][j - 1]
        elif i != 0 and j == 0:
            coins[i][j] = coins[i][j] + coins[i - 1][j]
        else:
            coins[i][j] = max(coins[i - 1][j], coins[i][j - 1]) + coins[i][j]
print(coins[i][j])

put = []
i, j = -1, -1
while -5 < i < 0 and -7 < j < 0:
    if i == -4 and j == -6:
        break
    if i != -4 and j != -6:
        if coins[i - 1][j] > coins[i][j - 1]:
            i -= 1
            put.append("D")
        elif coins[i - 1][j] < coins[i][j - 1]:
            j -= 1
            put.append("R")
    elif i == -4 and j != -6:
        j -= 1
        put.append("R")
    elif j == -6 and i != -4:
        i -= 1
        put.append("D")
put.reverse()
print(put)
"""























