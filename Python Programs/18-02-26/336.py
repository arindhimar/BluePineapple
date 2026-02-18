def check_28_days(month_name, year):
    month_name = month_name.lower()
    if month_name == "february":
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            return False
        else:
            return True
    else:
        return False
