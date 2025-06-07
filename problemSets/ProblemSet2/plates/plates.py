def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) <7 and start_2_letters(s) and s.isalnum():
        for index in range(len(s)):
            if s[index].isdigit():
                return last_only_num(index, s)
        return True
            
    else:
        return False
    
def start_2_letters(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False
    
def last_only_num(index, s):
    if s[index] == '0':
        return  False
    for n in range(index, len(s)):
        if s[n].isalpha():
            return False
        
    return True

main()