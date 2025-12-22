
#1
"""
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    elif n == 1:
        return 1
print(factorial(3))
"""


#2
"""
def remove_vowels(a):
    b = "eyuioaEYUIOA"
    for i in a:
        if i in b:
            a = a.replace(i, "", 1)
            remove_vowels(a)
    return a

print(remove_vowels("apple"))
print(remove_vowels("orange"))
print(remove_vowels("Big Chonky Apple"))
"""

#3
"""
def pascal(n):
    if n == 0:
        return [1]
    past_a = pascal(n - 1)

    new_a = [0] * (n + 1)
    new_a[0] = 1
    new_a[-1] = 1

    for i in range(1, n):
        new_a[i] = past_a[i - 1] + past_a[i]
    return new_a

print(pascal(0))
print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
"""

###  FINAL BOSS  ###


maze = [
    'S----',
    '##---',
    '---##',
    '----X'
]

def solve(mz):
    dvij = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }
    shir = len(mz[0])
    visot = len(mz)
    for i in range(visot):
        for j in range(shir):
            if mz[i][j] == 'S':
                pos = [i, j]
    bili = []
    def dvij(pos):
        if pos[0] < 0 or pos[0] >= shir or pos[1] < 0 or pos[1] >= visot:
            return None
        if mz[pos[i]][pos[i][j]] == '#' or pos in bili:
            return None
        if mz[pos[i]][pos[i][j]] == 'X':


        return dvij


print(solve(maze))

























