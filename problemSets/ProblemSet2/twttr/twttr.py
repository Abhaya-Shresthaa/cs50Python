vowels = "aeiouAEIOU"
finalString = []
def main():
    userInput = input("Input: ")
    for l in userInput:
        addLetter = checkVowel(l)
        finalString.append(addLetter)
        
    result = ''.join(finalString)
    print(result)
        
def checkVowel(alphabet):
    if alphabet in vowels:
        return ''
    else:
        return alphabet
    
main()