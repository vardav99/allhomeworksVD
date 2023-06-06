import random


def count_positive_negative(numbers):
    positive_count = 0
    negative_count = 0
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
    return positive_count, negative_count


numbers = [random.randint(-100, 100) for _ in range(10)]

print("Generated List:", numbers)

positive_count, negative_count = count_positive_negative(numbers)

print("Positive Count:", positive_count)
print("Negative Count:", negative_count)
