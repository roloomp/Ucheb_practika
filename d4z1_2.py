
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
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }
    shir = len(mz[0])
    visot = len(mz)
    for i in range(visot):
        for j in range(shir):
            if mz[i][j] == 'S':
                start_pos = [i, j]
    bili = []
    def move(pos):
        x, y = pos[0], pos[1]
        if x < 0 or x >= visot or y < 0 or y >= shir:
            return None
        if mz[x][y] == '#' or pos in bili:
            return None
        if mz[x][y] == 'X':
            return []
        bili.append(pos)
        for name, (move_x, move_y) in dvij.items():
            new_pos = (x + move_x, y + move_y)
            result = move(new_pos)
            if result is not None:
                return [name] + result
    return move(start_pos)
print(*solve(maze))

























