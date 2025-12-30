import re
import sys


def main():
    
    print(parse(input("HTML: ")))


def parse(s):
    try:
        match = re.search(r'.+src="(https?://(?:www.)?youtube\.com/embed/(?:.[^"]+))".+',s)
        final_URL = re.sub(r'https?://(?:www.)?youtube\.com/embed/',"https://youtu.be/",match.group(1))
        return final_URL
    except AttributeError:
        return None


if __name__ == "__main__":
    main()