def leapyear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
               
for yyear in range(1900,2600):
    if leapyear(yyear) == True:
        print(yyear, " is a leapyear")
    
               