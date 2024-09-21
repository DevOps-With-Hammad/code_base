def sum_of_integers(n): # 5
  if n < 1:
    return 0


  i =0
  sum = 0
  while sum <= n :
    sum = sum + i
    i = 0


  return sum


#print(sum_of_integers(3))  # should print 6
# print(sum_of_integers(4))  # should print 10
# print(sum_of_integers(5))  # should print 15