# Write a Python program to add text to a file and display the text in python.txt file.
with open("poem.txt", "a") as f:
    f.write("barev!\t")

f = open("poem.txt", "r")
for line in f:
    print(line, end="")
    

