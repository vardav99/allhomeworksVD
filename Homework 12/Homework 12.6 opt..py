strings = ['hello', 'world', 'brv', 'programming', 'list', 'php']

filtered_strings = [string for string in strings if any(char in 'aeiouAEIOU' for char in string)]

print("Original List:", strings)
print("Filtered List:", filtered_strings)
