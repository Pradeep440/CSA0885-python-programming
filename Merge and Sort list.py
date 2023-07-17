L1=[]  
L2=[]  
num1=int(input("Enter number of elements for first L:"))  
for i in range(1,num1+1):  
    b=int(input("Enter element:"))  
    L1.append(b)  
  
num2=int(input("Enter number of elements for second L:"))  
for i in range(1,num2+1):  
    d=int(input("Enter element:"))  
    L2.append(d)  
  
L3=L1+L2  
L3.sort()  
print("Sorted List is:",L3)
