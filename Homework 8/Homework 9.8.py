def is_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num

num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
