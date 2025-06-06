

def main():
    userInput = input("What time is it? ")
    totalTime = convert(userInput)
    if 7.0 <= totalTime <= 8.0:
        print("breakfast time")
    elif 12.0 <= totalTime <= 13.0:
        print("lunch time")
    elif 18.0 <= totalTime <= 19.0:
        print("dinner time")


def convert(time):
    hours , minutes = time.split(':')
    minutes = int(minutes) / 60
    hours = int(hours) + minutes
    return hours

if __name__ == "__main__":
    main()
