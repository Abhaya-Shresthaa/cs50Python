import re

#walrus operator is used to assign and check bool at the same time

name = input ("What's your name? ").strip()
if matches := re. searcin(r"^(.+), *(.+)$" , name):
    name = matches.group (2) + " " + matches.group (1)
print (f"hello, {name}" )