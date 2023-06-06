a = set()
b = set()


for i in range(10):
    t = int(input(f"Enter number {i + 1} for list A: "))
    a.add(t)

a = set(a)
b = set(b)

print("Set A:", a)
print("Set B:", b)


print("Condition A{} == B{}:", a == b)


print("Condition A{} (Union) B{}:", a.union(b))


print("Condition A{} (intersection) B{}:", a.intersection(b))


print("Condition A{} (difference) B{}:", a.difference(b))
print("Condition B{} (difference) A{}:", b.difference(a))
