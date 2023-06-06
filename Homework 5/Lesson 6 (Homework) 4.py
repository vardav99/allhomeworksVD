list_ = [5, 10, 15, 20, 25, 30]
if 20 in list_:
   index_20 = list_.index(20)
   list_.remove(20)
   list_.insert(index_20, 200)
   print("20 is found and replaced with 200.")
else:
   print("20 is not found in the list.")


print("Updated list:", list_)