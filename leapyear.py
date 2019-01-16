def leapyear(year):
    if year % 4 != 0:
        return("not a leap year")
    elif year % 100 != 0:
        return("is a leap year")
    elif year % 400 == 0:
        return("is a leap year")
    else:
        return("not a leap year")
               
 
print(leapyear(2500))
               