numbers = input("Enter a list of integers separated by space: ").split()

squared_numbers = []
for num in numbers:
    squared_numbers.append(int(num) * int(num))

print("Updated list:", squared_numbers)
