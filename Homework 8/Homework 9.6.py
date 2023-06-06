def find_length_of_values(dictionary):
    length_dict = {}
    for key, value in dictionary.items():
        length_dict[value] = len(value)
    return length_dict

dict1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
print("Original Dictionary:")
print(dict1)
print("Length of dictionary values:")
print(find_length_of_values(dict1))

dict2 = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
print("Original Dictionary:")
print(dict2)
print("Length of dictionary values:")
print(find_length_of_values(dict2))
