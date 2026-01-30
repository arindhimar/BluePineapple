def odd_days_in_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 2  
    else:
        return 1  
    
print(odd_days_in_year(2021))  