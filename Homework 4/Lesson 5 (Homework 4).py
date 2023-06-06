string = "Barev, Aziz!"
n = 4

if n < 0 or n >= len(string):
    print("Invalid index.")
else:
    new_string = string[:n] + string[n+1:]
    print("Modified String:", new_string)
