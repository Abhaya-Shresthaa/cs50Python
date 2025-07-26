import re

# (..) capturing group 
# (assigning the value to variable by giving something in regular expression to ())


name = input("Enter your name: ")

matches = re.search(r"^(.+), ?(.+)$", name)
#using * there we can remove the more no of white spaces that was used as well
if matches:
    # last = matches.group()
    # first = matches.group()
    # name = matches.group(2) + ' ' + matches.group(1)
    #print(matches.group(0)) group(0) prints the whole thing in group like below
    last, first = matches.groups()
    name = f"{first} {last} "


# if ',' in name:
#     last, first = name.split(', ')
#     name = f"{first} {last} "

print(f"hi! {name}")