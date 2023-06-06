inputted_string = input("input your word")
if len(inputted_string) < 3:
    print(inputted_string)
elif inputted_string[-3:] == 'ing':
    print(inputted_string + 'ly')
else:
    print(inputted_string + 'ing')
