#conner martinez
#11/20/2021
#determine if year enter is a leap year

def is_leap(year):
    leap = False

    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    elif (year % 100 == 0 ) and (year % 100 !=0):
        leap = False
    elif (year % 400 == 0):
        leap = "yes it is a leap year"
    else:
        leap = "no, not a leap year"

    return leap

year = int(input("enter year to determine: "))
print(is_leap(year))