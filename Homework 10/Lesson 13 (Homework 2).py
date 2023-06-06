# Write a Python function to count and display the total number of words in a text file.
f = open("poem.txt", "r")
word_count = 0
for line in f:
    words = line.split()
    word_count += len(words)
print(word_count)
