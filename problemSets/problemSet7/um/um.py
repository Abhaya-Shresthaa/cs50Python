import re
import sys

countt = 0
def main():
    print(count(input("Text: ")))


def count(s):
    countt = len(re.findall(r'\bum\b', s, re.IGNORECASE))
    return countt

if __name__ == "__main__":
    main()