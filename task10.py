a = int(input('число'))
b = int(input('число'))
c = int(input('число'))
d = int(input('число'))
if (b >8 or b <1 or d >8 or d<1):
    print('неверно')
elif (b-d-a+c == 0 or b - d +a -c or b == d or a == c) and (b != d or a !=c):
    print('да')
else:
    print('нет')