from math import *

the_result = 0
Frist_number = float(input())
Operations = "Operations available: add(+), sub(-), mult(*), div(/), sqrt, pow(**)"
print(Operations)
Operation = str(input("Choose the operation!!!: "))
if Operation == "sqrt":
    the_result = sqrt(Frist_number)
else:
    Second_number = float(input())
    if Operation == "add":
        the_result = Frist_number + Second_number
    elif Operation == "sub":
        the_result = Frist_number - Second_number
    elif Operation == "mult":
        the_result = Frist_number * Second_number
    elif Operation == "div":
        the_result = Frist_number / Second_number
    elif Operation == "pow":
        the_result = Frist_number ** Second_number
    else:
        print("Operation invalid!!!")

print(the_result)
