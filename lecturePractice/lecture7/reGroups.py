# use of ? for 0 or 1 times
import re

email = input("Enter your email address: ").strip()

#here this will be used for hi@helllo.edu and hi@cs50.helllo.edu
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email): 
    print("valid")
else:
    print("invalid")