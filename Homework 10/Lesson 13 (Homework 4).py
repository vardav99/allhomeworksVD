with open("poem.txt", "r") as f:
    for line in f:
        words = line.split()
        for word in words:
            if len(word) < 4:
                print(word)
