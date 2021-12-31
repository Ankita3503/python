# palindrome number 
a=input("enter any number to check whether it is palindrome or not ")
b=a[::-1]

print(b)
if (a==b ):    # every conditional statement is ended with : 
          # koi bhi conditional statement ke baad agar next line mein kuch likh rahe hai toh kuch space chod ke likhna hai
    print(" palindrome number")
else:
    print("not a palindrome number")
