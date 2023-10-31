def count11(seq):
   count = 0
   # define this function and return the number of occurrences as a number
   p = [1,1]
   for i in range(0, len(seq)-1):
      tmp = seq[i:(i+len(p))]
      if tmp == p:
            count +=1
      
   return count

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2
