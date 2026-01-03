import random

def value_generator(max_val = 100):
    return random.randint(2,max_val)

def operator_generator():
    return random.choice(['*','+','-'])

def generate_question(level=1):
    if level == 1:
        x = value_generator(11)
        y = value_generator(11)
        ope = operator_generator()
        expr = f"{x} {ope} {y}"
        
    elif level == 2:
        x = value_generator()
        y = value_generator()
        ope = operator_generator()
        expr = f"{x} {ope} {y}"
    elif level == 3:
        x = value_generator()
        y = value_generator()
        z = value_generator()
        ope_1 = operator_generator()
        ope_2 = operator_generator()
        expr = f"{x} {ope_1} {y} {ope_2} {z}"
    else:
        x = value_generator()
        y = value_generator()
        z = value_generator()
        a = value_generator()
        ope_1 = operator_generator()
        ope_2 = operator_generator()
        ope_3 = operator_generator()
        expr = f"{x} {ope_1} {y} {ope_2} {z} {ope_3} {a}"
    answer = eval(expr)
    return expr, answer