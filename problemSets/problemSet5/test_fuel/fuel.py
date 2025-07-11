def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            print(gauge(percentage))
            break  
        except (ValueError, ZeroDivisionError):
            continue 

def convert(fraction):
    x, y = fraction.split('/')
    x, y = int(x), int(y)
    
    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0 or x > y:
        raise ValueError
    
    return round((x / y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()