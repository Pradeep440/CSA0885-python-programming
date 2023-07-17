list1 = []
li=int(input("enter range: "))
for i in range (0,li):
    ele=int(input("element: "))
    list1.append(ele)
print(list1)

even_count, odd_count = 0, 0

for num in list1:

	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
