n = 'mommy'
print("The original string is : " + str(n))
flag=0
sub_list = [n[i: j] for i in range(len(n))
		for j in range(i + 1, len(n) + 1)]

print("substring"+str(sub_list))
for sub in sub_list:
    if len(sub)>1:
        if (sub == sub[::-1]):
            flag=1
            #print("yes",sub)
        else:
            #print("no")
            flag=0
    if flag==1:
        print("yes",sub)
    #else:
        #print("no palindrome")
