lst = list(map(int, input("Enter a list of integers separated by space: ").split()))
multiply = 1
for num in lst:
   multiply *= num
print("Product:", multiply)