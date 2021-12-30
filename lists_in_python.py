grocery=["soap","deo","lollipop","bhindi",567]
print(grocery)   # output:-['soap', 'deo', 'lollipop', 'bhindi']
print(grocery[3])  # output :-   bhindi
numbers=[2,5,8,9,6]
print(numbers)      # output :-  [2, 5, 8, 9, 6]
print(numbers[3])  # output :- 9
numbers.sort()  
print(numbers)   # output :-  [2, 5, 6, 8, 9]
numbers.reverse()
print(numbers)   #output:- [9, 8, 6, 5, 2]

# Now the  original numbers has been changed numbers=[9,8,6,5,2]  becuse of sort and reverse function
# slicing #
print(numbers[0:3])    #output:- [9, 8, 6]
print(numbers[0:])     #output :- [9, 8, 6, 5, 2]
print(numbers[:])      #output :- [9, 8, 6, 5, 2]
print(numbers[::2])     #output :-  [9, 6, 2]
print(numbers[::-1])     #output:- [2, 5, 6, 8, 9]
print(numbers[::-2])   # output:- [2, 6, 9]  it will print in reverse direction
print(max(numbers))
numbers.append(32)   # this function adds the number in the end  of the list
print(numbers)  #output:- [9, 8, 6, 5, 2, 32]
numbers.insert(1,46)       # this function inserts any element at any position  (1,46) :1 is index number, 46 is element to be inserted 
print(numbers)   #output :- [9, 46, 8, 6, 5, 2, 32]
numbers.remove(46)    # this function removes the  element  
print(numbers)
numbers.pop() # this function removes the last element from the lists 
print(numbers)  # output:- [9, 8, 6, 5, 2]
numbers[2]=567   # this function changes the value at any position with any value 
print(numbers)   # output:- [9, 8, 567, 5, 2]

# TUPLE #   tuple is immutable->means cannot be changed
tp=(1,2,4,5,9)
print(tp)     # output:- (1, 2, 4, 5, 9)
#tp[1]=5
#print(tp)  tuple cannot be changed 
tp1=(8)
print(tp1)  # output :- 8 kyuki yaha sirf ek hi element hai 

# swap #
a=9
b=6
t=a
a=b
b=t
print(a,b)

# but we are using python  so instead of using old method we can use the following method 
a=90
b=62
a,b=b,a
print(a,b)
 