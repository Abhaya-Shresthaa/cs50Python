import random

def value_generator(max_val=11):
    return random.randint(2, max_val)

def operator_generator():
    return random.choice(['+', '-', '*'])

def generate_question(level=1):
    if level == 1:
        x = value_generator(11)
        y = value_generator(11)
        expr = f"{x} + {y}"
    elif level == 2:
        x = value_generator()
        y = value_generator()
        expr = f"{x} * {y}"
    else:
        x = value_generator()
        y = value_generator()
        z = value_generator()
        expr = f"{x} + {y} * {z}"

    answer = eval(expr)
    return expr, answer