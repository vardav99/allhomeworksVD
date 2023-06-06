
sentence = input("Input your sentence:\t").split()
print(sentence)
word_count = {}
for word in sentence:
   if word in word_count:
       word_count[word] += 1
   else:
       word_count[word] = 1
print(word_count)
for key, value in word_count.items():
   print(f'word: {key}, count: {value}')

