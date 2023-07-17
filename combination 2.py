def permutations(string, step = 0):
    if step == len(string):
        print ("".join(string))
    for i in range(step, len(string)):
        s2 = [c for c in string]
        s2[step], s2[i] =s2[i], s2[step]
        permutations(s2, step + 1)
#print (permutations ('one'))
ab=input("enter value: ")
from itertools import permutations
print ([''.join(p) for p in permutations(ab)])
