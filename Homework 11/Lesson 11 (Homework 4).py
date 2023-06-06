def first_last_product():
    try:
        numbers = [int(num) for num in input("Enter a list of integers: ").split()]
        product = numbers[0] * numbers[-1]
        return product
    except IndexError:
        print("List is empty or has only one element")
        return None
result = first_last_product()
if result is not None:
    print("Product of first and last elements:", result)

