def read_file(barev):
    try:
        with open(barev, 'r') as f:
            contents = f.read()
            return contents
    except FileNotFoundError:
        print("No file")
        return "No file"


file_contents = read_file("barev.txt")
if file_contents != "No file":
    print("File contents:", file_contents)
