with open("a.txt", "w") as f:
    f.write("barev")

with open("b.txt", "w") as g:
    g.write("ap")

with open("a.txt", "r") as f:
    with open("b.txt", "w") as g:
        for line in f:
            g.write(line)
