def check_season(month):
    season = " "
    if month == "December" or month == "January" or month == "February":
        season = "WINTER"
    elif month == "March" or month == "April" or month == "May":
        season = "SPRING"
    elif month == "June" or month == "July" or month == "August":
        season = "SUMMER"
    elif month =="September" or month == "October" or month == "November":
        season ="AUTUMN"
    else:
        season = "INVALID"
    return season
month = input("What month is it over there?\n").title()
print("Oh it is ", check_season(month))