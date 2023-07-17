ab = input("enter the string")
s = ab.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))
