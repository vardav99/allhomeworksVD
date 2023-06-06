number = [12, 75, 150, 180, 145, 525, 50]
for val in number:
   if val >= 150:
       continue
   elif val >= 500:
       break
   if val % 5 == 0:
       print(val)
