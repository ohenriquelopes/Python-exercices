a = 12
b = 3

print(a + b) 
print(a - b)
print(a * b)
print(a / b)    # 4.0
print(a // b)   # Integer division, rounded down towards minus infinity
print(a % b)    # modulo: the remainder after integer division

print()


for i in range(1, a // b):
    print(i)

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

## Operator precedence acronums

"""
PEMDAS - Parentheses, exponents, multiplication/division, addition/subtraction
BEDMAS - Brackets, exponents, division/multiplication, addition/subtraction
BODMAS - Brackets, order, division/multiplication, addition/subtraction
BUDMAS - Brackets, index, division/multiplication, addition/subtraction
"""

print()

print(a / (b * a) / b)