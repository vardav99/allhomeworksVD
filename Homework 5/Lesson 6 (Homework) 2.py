numbers = list(map(int, input("Enter a list of integers separated by space: ").split()))
s = 0
for item in numbers:
   s += item
print("Sum of the list:", sum(numbers))