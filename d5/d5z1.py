
#1
"""
def count_program(start, end, mejdu):
    def program(begin, last):
        if begin > last:
            return 0
        if begin == last:
            return 1
        result = 0
        result += program(begin + 1, last)
        result += program(begin + 2, last)
        result += program(begin * 2, last)
        return result

    a = program(start, mejdu)
    b = program(mejdu, end)
    return a * b

z = 3
x = 12
c = 10
print(count_program(z, x, c))
"""

#2
"""
def count_program(start, end, mejdu):
    def program(begin, last):
        if begin > last:
            return 0
        if begin == mejdu:
            return 0
        if begin == last:
            return 1
        result = 0
        result += program(begin + 1, last)
        result += program(2 * begin + 1, last)
        return result
    return program(start, end)
z = 1
x = 27
c = 26

print(count_program(z, x, c))
"""

# 3
"""
def count_program(start, end, yes, nope):
    def program(begin, last):
        if begin > last:
            return 0
        if begin == nope:
            return 0
        if begin == last:
            return 1
        result = 0
        result += program(begin + 1, last)
        result += program(begin + 2, last)
        return result
    a = program(start, yes)
    b = program(yes, end)
    return a * b

z = 2
x = 18
c = 9
v = 14
print(count_program(z, x, c, v))
"""