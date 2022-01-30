str=input("type a string:")
print("input string is:",str)
if(str.endswith("ing")):
    str=str+'ly'
else:
    str=str+'ing'
print("the formatted string is:",str)

