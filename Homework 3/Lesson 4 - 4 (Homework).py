range(100,600)
for x in range(100, 600):
    if x % 3 == 0 and x % 11 == 0 and x % 7 != 0:
        print(x)