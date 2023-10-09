year = int(input("Please enter the year to check is leap year or not : "))

if year % 400 == 0 : 
    print(year, " it's Leap Year")
else:
    if year % 4 == 0 and year % 100 != 0 :
        print(year, " it's Leap Year")
    else:
        print(year, " it's not an Leap Year")
        
    