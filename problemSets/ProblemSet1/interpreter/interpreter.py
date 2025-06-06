userInput = input("Expression: ").strip()

x, y, z = userInput.split(" ")
x = int(x)
z = int(z)

match y:
    case '+':
        print(f"{x+z: .1f}")
    case '-':
        print(f"{x-z: .1f}")
    case '*':
        print(f"{x*z: .1f}")
    case '/':
        print(f"{x/z: .1f}")


