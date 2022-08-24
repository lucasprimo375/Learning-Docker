import calendar

print("Hello there! Welcome to the calendar application!")

try:
    year = int(input("Please, enter a year: "))
except ValueError:
    print("Invalid year!")
    exit()

if year < 0:
    print("Invalid year!")
    exit()

try:
    month = int(input("Please, enter a month: "))
except ValueError:
    print("Invalid month!")
    exit()

if month < 0 or month > 12:
    print("Invalid month!")
    exit()

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if month == 2:
    if year % 4 != 0:
        days = 28
    elif year % 100 != 0:
        days = 29
    elif year % 400 != 0:
        days = 28
    else:
        days = 29
        
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
else:
    days = 30

c = calendar.Calendar()
it = c.itermonthdays(year, month)

print()

print("          ", months[month - 1], str(year))

print("Mo   Tu   We   Th   Fr   Sa   Su")

monthDay = 0
for i in it:
    if monthDay % 7 == 0:
        if i != 0:
            print(i, end = '')
        else:
            print(" ", end = '')
    else:
        if i > 10:
            print("  ", i, end = '')
        else:
            if i != 0:
                print("   ", i, end = '')
            else:
                print("     ", end = '')
    
    if monthDay % 7 == 6:
        print("")

    monthDay += 1

print("\n\nHave a wonderful day!")