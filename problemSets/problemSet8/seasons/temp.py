
    
from datetime import date
import sys
from num2words import num2words


# def splitDateToday(today):
#         year, month, day = str(today).split('-')
#         return [int(year), int(month), int(day)]
    
# def splitDateBorn(born):
#         year, month, day = born.split('-')
#         return [int(year), int(month), int(day)]
    
def userInput():
        today = date.today()
        userInput = input("Date of Birth: ")
        validateDate(userInput)
        return [today, userInput]
          
def validateDate(userInput):
        try:
            year, month, day = userInput.split('-')
        except:
            sys.exit("Invalid date")
            
def totalMin(today, born):
    year = today[0] - born[0]
    month = today[1] - born[1]
    day = today[2] - born[2]
    leap = int(year / 4)
    year = int(year + float(month/12) + float((day+leap)/365))
    
    total_min = year*365*24*60
    return total_min

def removeAnd(words):
    if isinstance(words,str):
        words = words.split()
    finalWord = [word for word in words if word != "and"]
    result = " ".join(finalWord)
    result = result.capitalize()
    return result
            
def main():
    dates = userInput()
    # today = splitDateToday(dates[0])
    # born = splitDateToday(dates[1])
    words = num2words(totalMin(today,born))
    print(removeAnd(words))
if __name__ == "__main__":
    main()