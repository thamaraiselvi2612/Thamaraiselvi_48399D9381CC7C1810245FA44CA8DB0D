def LeapYear(year):
    if((year % 400 == 0) and (year % 100 == 0)):
        print('{} is a LearYear'.format(year))
    elif((year % 4 == 0) and (year % 100 != 0)):
        print('{} is a LearYear'.format(year))   
    else:
        print('{} is not  leapyear'.format(year))   


year = 2000 
LeapYear(year)