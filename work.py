

def getBirthdays(cYear, bYear, bMonth, bDay):
    weekdayIndex = calendar.weekday(cYear, bMonth, bDay)
    dayName = calendar.day_name[weekdayIndex]
    age = cYear - bYear

    return age, dayName


import datetime
import calendar


def input_bdate():
    while True:
        print("""
Enter your Birthday:
Example: 25/12/2000
""")
        birthday = input("Your Birthday: ")

        try:
            day, month, year = birthday.split("/")

            try:
                day = int(day)
                if day < 1 or day > 31:
                    print("Please enter day as a digit between 1-31 !")
                    continue
            except ValueError:
                print("Please enter day as a digit between 1-31 !")
                continue

            try:
                month = int(month)
                if month < 1 or month > 12:
                    print("Please enter month as a digit between 1-12 !")
                    continue
            except ValueError:
                print("Please enter month as a digit between 1-12!")
                continue

            curYear = datetime.datetime.now().year
            try:
                year = int(year)
                if year < 1920 or year > curYear:
                    print(f"Please enter year as a digit between 1920 - {curYear} !")
                    continue
            except ValueError:
                print(f"Please enter year as a digit between 1920 - {curYear} !")
                continue

            try:
                datetime.datetime(year, month, day)
            except ValueError:
                print("Invalid date. Please enter a valid date !")
                continue

        except ValueError:
            print("Invalid input format. Please use the format DD/MM/YYYY !")
            continue

        return day, month, year, curYear
bDay, bMonth, bYear, curYear = input_bdate()

while (curYear - bYear) >= 0:
    age, dayName = getBirthdays(curYear, bYear, bMonth, bDay)
    print(f"Age: {age} - {dayName}")
    curYear -=1
