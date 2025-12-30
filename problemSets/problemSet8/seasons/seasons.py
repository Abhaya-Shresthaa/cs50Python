from datetime import date
import sys
import inflect

def validateDate(userInput):
        try:
            year, month, day = userInput.split('-')
        except:
            sys.exit("Invalid date")
            
def splitDateBorn(born):
        year, month, day = born.split('-')
        birthDate = date(int(year), int(month), int(day))
        return birthDate
    
def calculateMin(today, birthDate):
    difference = today - birthDate
    totalDays = difference.days
    totalMins = totalDays*24*60
    return totalMins
    
def removeAnd(words):
    if isinstance(words,str):
        words = words.split()
    finalWord = [word for word in words if word != 'and']
    result = " ".join(finalWord)
    result = result.capitalize()
    return result


def main():
    birthDay = input("Date of Birth: ")
    validateDate(birthDay)
    birthDate = splitDateBorn(birthDay)
    today = date.today()
    words = inflect.engine().number_to_words(calculateMin(today, birthDate))
    minsInwords = removeAnd(words) 
    print(minsInwords, "minutes")


if __name__ == "__main__":
    main()