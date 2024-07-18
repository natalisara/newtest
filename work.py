print("test")

def getBirthdays(cYear, bYear, bMonth, bDay):
    weekdayIndex = calendar.weekday(cYear, bMonth, bDay)
    dayName = calendar.day_name[weekdayIndex]
    age = cYear - bYear

    return age, dayName
