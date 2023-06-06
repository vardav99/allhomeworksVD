a = int(input("range from: "))
b = int(input("to: "))

count = 0
for i in range(a, b+1):
    if i % 7 == 0:
        count += 1

print("bajanvum en 7-i", count, "hat tiv")
