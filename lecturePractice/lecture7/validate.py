import re # regular expression

email = input("Enter your email address: ").strip()

if re.search(".+@.+",email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")

#back slash is used to make put the actual . in re
# ^ and $ are used for making the end and starting as needed

if re.search(r"^.+@.+\.edu$",email): 
    print("valid")
else:
    print("invalid")
    
# same to make @ use only one time
if re.search(r"^[^@]+@[^@]+\.edu$",email): 
    print("valid")
else:
    print("invalid")
    
#if we don't want symbols then
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): 
    print("valid")
else:
    print("invalid")