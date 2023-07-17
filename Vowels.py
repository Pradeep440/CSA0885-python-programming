str=input("Enter str:")
vowels=0
str = (str.lower())
for i in str:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)
