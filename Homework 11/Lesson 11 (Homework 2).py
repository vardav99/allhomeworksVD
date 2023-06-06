my_list = input("Write your numbers: ").split()

try:
    def sum_of_numbers(numbers):
        return sum(numbers)


    numbers = [int(num) for num in my_list]
    result = sum_of_numbers(numbers)
    print(result)

except ValueError:
    print("Asum em write your number vay")
    result = None
