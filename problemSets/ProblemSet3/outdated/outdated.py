monthsWords = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True: 
    try:
        userInput = input("Date: ")
        if '/' in userInput:
            month, day, year = userInput.strip().split('/')
        elif ',' in userInput:
            month, day, year = userInput.strip().split(' ')
            month = month.capitalize()
            day = day.strip(',')
            if month.isalpha():
                if month in monthsWords:
                    month = monthsWords.index(month) +1
        month = int(month)
        year = int(year)
        day = int(day)
        if (month > 12) or (day > 31):
            continue
    except ValueError:
        continue
    except KeyError:
        continue
    except NameError:
        continue
    else: 
        break
print(f"{year}-{month:02}-{day:02}")