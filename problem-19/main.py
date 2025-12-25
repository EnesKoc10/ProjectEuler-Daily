def countSundays():
    total_sundays = 0
    day_of_week = 1
    
    for month in range(1, 13):
        if month in [4, 6, 9, 11]:
            days_in_month = 30
        elif month == 2:
            days_in_month = 28
        else:
            days_in_month = 31
        day_of_week = (day_of_week + days_in_month) % 7

    for year in range(1901, 2001):
        for month in range(1, 13):
            if day_of_week == 0:
                total_sundays += 1
            
            if month in [4, 6, 9, 11]:
                days_in_month = 30
            elif month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    days_in_month = 29
                else:
                    days_in_month = 28
            else:
                days_in_month = 31
            
            day_of_week = (day_of_week + days_in_month) % 7
            
    return total_sundays


print(countSundays())