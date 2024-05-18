#Первая задача

def merge_sorted_lists(list1, list2):
  res = []
  index1 = len(list1) - 1
  index2 = len(list2) - 1

  while index1 >= 0 and index2 >= 0:
      
    if list1[index1] >= list2[index2]:
      res.append(list1[index1])
      index1 -= 1
    else:
      res.append(list2[index2])
      index2 -= 1

  if index1 >= 0:
    res.extend(list1[index1::-1])
  if index2 >= 0:
    res.extend(list2[index2::-1])

  return res


# Тестим тесты
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

res = merge_sorted_lists(list1, list2)

print(res)