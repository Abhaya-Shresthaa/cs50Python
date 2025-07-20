import re 
import sys

def main():
    #convert(input("Hours: "))
    print(convert(input("Hours: ")))


def convert(s):
    # try:
        if re.search(r"^(1[0-2]|[0-9])(:[0-5]?[0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5]?[0-9])? (AM|PM)$",s):
            match = re.search(r"(1[0-2]|[0-9])(?::([0-5]?[0-9]))? (AM|PM) to (1[0-2]|[0-9])(?::([0-5]?[0-9]))? (AM|PM)",s)
            
            hour1 , min1,tim1, hour2, min2, tim2 = match.groups()
            hour1, hour2 = int(hour1), int(hour2)
            if tim1 == 'PM' and hour1 != 12:
                hour1 += 12
            if tim2 == 'PM' and hour2 != 12:
                hour2 += 12
            if tim1 == 'AM' and hour1 == 12:
                hour1 = 0
            if tim2 == 'AM' and hour2 == 12:
                hour2 = 0
            if min1:
                min1 = int(min1)
            else:
                min1 = 0
            if min2:
                min2 = int(min2)
            else:
                min2 = 0
            
            return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"

        else:
            raise ValueError
    # except ValueError:
    #     pass

if __name__ == "__main__":
    main()
    
        # if re.search(r"^(1[0-2]|[0-9])(:[0-5]?[0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5]?[0-9])? (AM|PM)$",s):
        #     match = re.search(r"(1[0-2]|[0-9])(?::[0-5]?[0-9])? (AM|PM) to (1[0-2]|[0-9])(?::[0-5]?[0-9])? (AM|PM)",s)
        #     first = match.group(1)
        #     second = match.group(3)
        #     if match.group(2) == 'PM':
        #         first = int(first) + 12
        #     if match.group(4) == 'PM':
        #         second = int(second) + 12
        #     needed = s
        #     if re.search(r"(?:1[0-2]|[0-9])(:[0-5]?[0-9])? PM to",needed):
        #         match1 = re.search(r"(?:1[0-2]|[0-9])(:[0-5]?[0-9])? PM to",needed)
        #         if match1.group(1) == None:
        #             nextPart = ''
        #         else:
        #             nextPart = match1.group(1)
        #         needed= re.sub("(1[0-2]|[0-9])(?::[0-5]?[0-9])? PM to",f"{first}{nextPart} to",needed)
                
        #     if re.search(r"to (?:1[0-2]|[0-9])(:[0-5]?[0-9])? PM",needed):
        #         match2 = re.search(r"to (?:1[0-2]|[0-9])(:[0-5]?[0-9])? PM",needed)
        #         if match2.group(1) == None:
        #             nextPart = ''
        #         else:
        #             nextPart = match2.group(1)
        #         needed= re.sub("to (1[0-2]|[0-9])(?::[0-5]?[0-9])? PM",f"to {second}{nextPart}",needed)
            
        #     while True:
        #         if re.search("AM", needed):
        #             needed= re.sub(" AM","",needed)
        #         else: 
        #             break
        #     # needed= re.sub("(AM|PM) ","",s)
        #     # needed = re.sub("(AM|PM)","",needed)
            
        #     print(needed)
        #     # if match := re.search(r"(1[0-2]|[0-9])(?::[0-5]?[0-9])? PM",s):
        #     #     upgraded = int(match.group(1)) + 12
        #     #     print(upgraded)
        #     # print("Valid")
        
# def convert(s):
#     match = re.match(
#         r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$",
#         s
#     )
#     if not match:
#         raise ValueError

#     h1, m1, p1, h2, m2, p2 = match.groups()

#     h1, h2 = int(h1), int(h2)
#     m1 = int(m1) if m1 else 0
#     m2 = int(m2) if m2 else 0

#     # Convert to 24-hour
#     if p1 == "PM" and h1 != 12:
#         h1 += 12
#     if p1 == "AM" and h1 == 12:
#         h1 = 0
#     if p2 == "PM" and h2 != 12:
#         h2 += 12
#     if p2 == "AM" and h2 == 12:
#         h2 = 0

#     return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"