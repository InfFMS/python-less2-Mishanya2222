count = 9999
for i in range(90001):
    count = count + 1
    if count % 133 == 125 and count%134 == 111:
        print(count)
