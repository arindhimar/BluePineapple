#Write a function to print the season for the given month and day.

def get_season(month, day):
    if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day < 20):
        return "Winter"
    elif (month == 3 and day >= 20) or (4 <= month <= 5) or (month == 6 and day < 21):
        return "Spring"
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day < 22):
        return "Summer"
    elif (month == 9 and day >= 22) or (10 <= month <= 11) or (month == 12 and day < 21):
        return "Fall"
    else:
        return "Invalid date"
    
month = 3
day = 15
print(get_season(month, day))