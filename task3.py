year = int(input('ведите ваш возраст'))
if year%10 <= 4 and year%10 != 1 and (year < 10 or year > 20) and year%10 != 0:
    print(year, ( "года"))
elif year%10 ==1 and (year < 10 or year > 20):
    print(year, 'год')
else:
    print(year, "лет")