def bubble(lst):
  c = len(lst) - 1
  for x in list(range(len(lst)-1)):
    for y in list(range(c)):
      a = lst[y]
      z = lst[y + 1]
      if (a > z):
        b = z
        lst[y + 1] = a
        lst[y] = b
      c = c - 1
  print(lst)

#lst = [8, 6, 7, 5, 3, 0, 9, 1, 2, 4]
lst = [3, 2, 1]
print(lst)
print(len(lst))
bubble(lst) 
