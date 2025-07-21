from validator_collection import checkers

def main():
    print(validate(input("What's your email address? ")))
    
def validate(user_email):
    if checkers.is_email(user_email):
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == '__main__':
    main()