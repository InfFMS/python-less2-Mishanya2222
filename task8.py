a = int(input('число'))
b = int(input('число'))
c = int(input('число'))
d = int(input('число'))
if (b >8 or b <1 or d >8 or d<1):
    print('неверно')
elif (abs(a - c) == 2 and abs(b - d)==1)or (abs(a - c)==1 and abs(b - d)==2):
    print('да')
else:
    print('нет')