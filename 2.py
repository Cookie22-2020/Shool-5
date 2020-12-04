import math
a = int(input('Введите число: '))
i = int(0)
b = int(0)
for i in range(1, a**2):
    if  i ==((i%1000)**2) or i ==((i%100)**2) or i ==((i%10)**2):
        print (math.sqrt(int(i)), '*' ,math.sqrt(int(i)), '=', i)
    else:
        b+0
