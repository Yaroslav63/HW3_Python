my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print (str(my_list))
list = []
for i in my_list:
  if i not in list:
    list.append(i)

print (str(list))