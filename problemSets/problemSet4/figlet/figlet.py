import sys
from pyfiglet import Figlet
from random import choice

figlet =Figlet()
allFonts = figlet.getFonts()
if sys.argv[2] not in allFonts:
    sys.exit("Invalid usage")

if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    userInput = input("Input: ")
    try: 
        f = Figlet(font = sys.argv[2])
        print(f.renderText(userInput))
    except:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    userInput = input("Input: ")
    try: 
        f = Figlet(font= choice(allFonts)) #or use allFonts[randint(0, len(allFonts))
        print(f.renderText(userInput))
    except:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")