
#1
"""
def perevod(num):
    n = ''
    alph = 'ABCDE'
    while num > 0:
        a = num % 15
        if a > 9:
            a -= 9
            for j in range(len(alph)):
                if j == a - 1:
                    a = str(alph[j])
        n = n + str(a)
        num //= 15
    return n[::-1]

for i in '0123456789ABCDE':
    b = int(f'123{i}5', 15)
    x = int(f'1{i}233', 15)
    if (b + x) % 14 == 0:
        c = (b + x) // 14
        break

print(perevod(c))
"""

#2
"""
for i in range(16, 100):
    num1 = 10 * (i ** 6) + 11 * (i ** 5) + 2 * (i ** 4) + 6 * (i ** 3) + 7 * (i ** 2) + 13 * (i ** 1) + 1
    num2 = 15 * (i ** 6) + 0 * (i ** 5) + 2 * (i ** 4) + 4 * (i ** 3) + 10 * (i ** 2) + 8 * (i ** 1) + 9
    if (num1 + num2) % (i - 1) == 0:
        print(i)
        break
"""

#3
"""
for i in range(9):
    a = int(f'{i}B09', 17)
    b = int(f'{i}8E8', 15)
    if (a + b) % 155 == 0:
        print((a + b) // 155)
        break
"""

#4
"""
for x in '01234567':
    for y in '01234567':
        n1 = int(f'{y}04{x}5', 11)
        n2 = int(f'253{x}{y}', 8)
        if (n1 + n2) % 117 == 0:
            print((n1+n2) // 117)
            break
"""

#5
"""
x = 7 * (512 ** 1912) + 6 * (64 ** 1954) - 5 * (8 ** 1991) - 4 * (8 ** 1980) - 2022
sp = ''
co = 0
while x > 0:
    sp += str(x % 8)
    x //= 8
sp = sp[::-1]
print(sp)
for i in sp:
    if i == '7':
        co += 1
print(co)
"""






















































































