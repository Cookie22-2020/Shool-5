a = int(input())
b = int(input())

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

gcd = a + b
print(gcd)

def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


while 1:
    try:
        x = int(input('a = '))
        y = int(input('b = '))
        print('НОК:', lcm(x, y))
    except ValueError:
        break