#use of re.sub

import re

url = input("URL: ")

# re.sub(pattern, replace, string, count, flags)

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

#by just doing this it catches first group not the one needed
#so need to use not catching group (non-capturing version)
username = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if username: 
    print(f"UserName: {username.group(1)}")