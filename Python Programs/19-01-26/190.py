def check_if_month_has_thirty_days(month_name):
    list_of_months = ["april","june","september","november"]
    if month_name.lower() in list_of_months:
        return True
    else:
        return False


month_name = input("Enter a month name: ")
print(check_if_month_has_thirty_days(month_name))