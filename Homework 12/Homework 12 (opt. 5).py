reverse_dict = lambda d: {v: k for k, v in d.items()}


original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = reverse_dict(original_dict)

print("Original Dictionary:", original_dict)
print("Reversed Dictionary:", reversed_dict)
