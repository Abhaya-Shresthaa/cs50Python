import cowsay
import sys

print(cowsay.char_names)

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])