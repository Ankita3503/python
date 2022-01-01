num=int(input("Enter any number to find factorial "))
fact=1;
for x in range(num,0,-1):
    fact=fact*x
print(" factorial of ",num,"=",fact)
