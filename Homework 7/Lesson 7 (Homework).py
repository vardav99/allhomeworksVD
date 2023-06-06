angleren_hayeren = {
    "Variable": "Փոփոխական",
    "Declaration": "Հայտարարում",
    "Assignment": "Վերագրում",
    "Data types": "Տվյալների տիպեր",
    "Integer": "Թվային տիպ",
    "String": "Տողային տիպ",
    "Boolean": "Բուլյան տիպ",
    "true": "Ճշմարիտ",
    "else": "Հակառակ դեպքում",
    "array": "Զանգված",
    "if": "Եթե",
    "false": "Կեղծ"
}
hayeren_angleren = {
    "Փոփոխական": "Variable",
    "Հայտարարում": "Declaration",
    "Վերագրում": "Assignment",
    "Տվյալների տիպեր": "Data types",
    "Թվային տիպ": "Integer",
    "Տողային տիպ": "String",
    "Բուլյան տիպ": "Boolean",
    "Ճշմարիտ": "true",
    "Հակառակ դեպքում": "else",
    "Զանգված": "array",
    "Եթե": "if",
    "Կեղծ": "false"
}
word_to_translate_to_Armenian = str(input("Input your word: \t"))
if word_to_translate_to_Armenian in angleren_hayeren:
    print(angleren_hayeren[word_to_translate_to_Armenian])
else:
    print("There is no such word")
word_to_english = str(input("Input your armenian word: \t"))
if word_to_english in hayeren_angleren:
    print(hayeren_angleren[word_to_english])
else:
    print("There is no such armenian word")
