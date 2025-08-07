import calendar
month=int(input("Enter your month:"))
year=int(input("Enter your year:"))
cal=calendar.month(year,month)
print(cal)
print(f"Your Selected month is {month} and the year is {year}")
