
def convert(text):
    changedStr = text.replace(':)', '🙂').replace(':(','🙁')
    return changedStr

def main():
    userInput = input()
    converted = convert(userInput)
    print(converted)

main()

