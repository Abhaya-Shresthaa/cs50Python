vowel = "AEIOUaeiou"
addLetter =''

def main():
    userInput = input()
    final_shorten = shorten(userInput)
    print(final_shorten)
     
def shorten(word):
    finalString = []
    for l in word:
        if l in vowel:
            addLetter = ''
        else:
            addLetter = l
        finalString.append(addLetter)
        
    result = ''.join(finalString)
    return result

if __name__ == "__main__":
    main()