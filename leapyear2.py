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
        
    if yyear % 100 == 0 and yyear % 4 == 0:
        print(yyear," is evenly divisible by 100 and 4")
        
        if yyear % 400 == 0:
            print(yyear,"is also evenly divisible by 400 so is a leap year!!")
            
        else:
            print(yyear,"is not evenly divisible by 400 NOT LEAP YEAR")
            
            
    
               