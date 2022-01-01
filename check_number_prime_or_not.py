num=int(input("Enter any number to check prime or not "))
count=0
for x in range(2,num):
   if num%x==0:
       count=count+1
       break

if count==0:
    print("a prime  number")
else:
     print(" Not a prime  number ")
