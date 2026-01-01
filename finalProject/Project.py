import random
import operator
import sys

class player:
    
    def __init__(self, name):
        if not name:
            raise ValueError("Name not present")
        self.name = name   

points = 0

operations = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}

def main():
    # print('1. Option based \n2. No options')
    #n = int(input('Your Choice:'))
    # x = value_generator()
    # y = value_generator()
    # z = value_generator()
    # ope_1 = operator_generator()
    # ope_2 = operator_generator()
    # #final_value = operations[ope_2]((operations[ope_1](x,y)),z)
    # expr = f"{x} {ope_1} {y} {ope_2} {z}"
    # final_value = eval(expr)
    # print("find value of", expr)
    # print(final_value)
    global points
    while(True):
        while(points < 3):
            final_val = level_1()
            user_input = no_option()
            ans_checker(final_val, user_input)
            print("Points: ",points,)
        print("You Won")
        restart_or_exit()
    
def level_1():
    x = value_generator(11)
    y = value_generator(11)
    ope = operator_generator()
    expr = f"{x} {ope} {y}"
    final_value = eval(expr)
    print("find value of", expr)
    return final_value

def level_2():
    x = value_generator()
    y = value_generator()
    ope = operator_generator()
    expr = f"{x} {ope} {y}"
    final_value = eval(expr)
    print("find value of", expr)
    return final_value

def level_3():
    x = value_generator()
    y = value_generator()
    z = value_generator()
    ope_1 = operator_generator()
    ope_2 = operator_generator()
    expr = f"{x} {ope_1} {y} {ope_2} {z}"
    final_value = eval(expr)
    print("find value of", expr)
    return final_value

def level_4():
    x = value_generator()
    y = value_generator()
    z = value_generator()
    a = value_generator()
    ope_1 = operator_generator()
    ope_2 = operator_generator()
    ope_3 = operator_generator()
    expr = f"{x} {ope_1} {y} {ope_2} {z} {ope_3} {a}"
    final_value = eval(expr)
    print("find value of", expr)
    return final_value


def value_generator(max_val = 100):
    return random.randint(2,max_val)

def operator_generator():
    return random.choice(['*','+','/','-'])

def no_option():
    user_input = int(input('Your Ans: '))
    return user_input

def ans_checker(final_value, user_input, level=1):
    global points
    if final_value == user_input:
        if level == 1:  
            points = points + 1
        elif level == 2:  
            points = points + 2
        elif level == 3:  
            points = points + 3
        elif level == 4:  
            points = points + 3
    else:
        print("Wrong Ans")
        restart_or_exit()

def restart_or_exit():
    global points
    re = int(input("Press 1 to restart:\n"))
    if re == 1:
        points = 0        
    else: 
        sys.exit("Thanks for playing")

if __name__ == '__main__':
    main()