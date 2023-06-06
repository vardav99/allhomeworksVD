def swap_elements(lst, pos1, pos2):
    if pos1 < 0 or pos1 >= len(lst) or pos2 < 0 or pos2 >= len(lst):
        print("Invalid positions!")
        return
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]


lst = input("Enter elements of the list separated by spaces: ").split()

lst = [int(element) for element in lst]

pos1 = int(input("Enter the first position to swap: "))
pos2 = int(input("Enter the second position to swap: "))

print("Original List:", lst)

swap_elements(lst, pos1, pos2)

print("Updated List:", lst)
