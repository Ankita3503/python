name="ankita one day you will be placed in  Google.and one day  you will make your family proud  "
name1="an\tki\tta"
name2="{0} one day you will be placed in  {1}."
name4="ankita1"
print(len(name))     # it gives the length of string
print(name.upper())    # converts all lowercase characters in a string into uppercase
print(name.title())    #   it coonverts all the first letter into uppercase  - output - Ankita  Will Be Placed In Google
print(name.capitalize())   #converts only  the first letter of the string into uppercase  - output:- Ankita  will be placed in google
print(name.casefold())    # it converts all the string into lowercase - output:- ankita  will be placed in google
print(name.count("the"))    # it counts  how many times is the word  "the"/ or(other)  written in a string 
                            # it denotes  number of times a substring occurs in a given string 
print(name.count("in",0 , ))    # denotes the number of times a substring occurs in the given interval of string
print(name.endswith("."))  # returns true or false if the certain condition is met or not -  output:- false
print(name1.expandtabs())    # it  sets the tab size of the string where the "\t" is put in the string - output:- an      ki      ta
print(name.find("one",0,))   # it will return the position(without counting the gap) when the string is found but only once if repeated it not see the repeated one
  # find string (find())--
"""The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. 

"""
print(name.find("yas"))
#print(name.index("yash"))   #  output:- print(name.index("yash"))  ValueError: substring not found
print(name.index("ankita"))  #output :- 0 because it is found at first position
print(name2.format("Baabu","google"))
# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
 
print(name4.isalnum())
