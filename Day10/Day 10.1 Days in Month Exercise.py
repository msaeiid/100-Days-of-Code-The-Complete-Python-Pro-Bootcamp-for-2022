def leap_year(year: int):
    result = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
        else:
            result = True
    return result


def days_in_month(year: int, month: int):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return "Invalid month"
    if leap_year(year) and month == 2:
        return month_days[month-1]+1
    else:
        return month_days[month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
