l1 = input("Enter the value: ")


result = []
def l2(data, i, length):
	if i == length:
		result.append(''.join(data) )
	else:
		for j in range(i, length):
			data[i], data[j] = data[j], data[i]
			l2(data, i + 1, length)
			data[i], data[j] = data[j], data[i]
l2(list(l1), 0, len(l1))

print(str(result))
