# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def isPythagorean(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


elNumbro = -1
max = 1000
for a in range(1, max):
    for b in range(1, max):
        for c in range(1, max):
            if (a + b + c == max) and isPythagorean(a, b, c):
                elNumbro = a * b * c
                break
print(elNumbro)
