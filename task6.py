count = 99
N = 3
for i in range(900):
    count = count + 1
    t = count%10
    f= (count%100 - t)/10
    g=(count -count%100)/100
    if count == t**N + f**N + g**N:
        print(count)