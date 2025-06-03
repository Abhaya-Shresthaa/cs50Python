x= input("value of x? ")
y= input("value of y? ")
#takes x and y as string
z = x + y
print(f"sum of 2 numbers is {z}")

z = int(x) + int(y)
print(f"sum of 2 numbers is {z}")

# or put int in the input
x= int(input("value of x? "))
y= int(input("value of y? "))

print(x+y)
print()
print("floating value")
x= float(input("value of x? "))
y= float(input("value of y? "))
z = round(x+y)
a = round(x+y, 2)
print(z)
print(a)
print(f"adding comma in numbers {z:,}")

print()
print("now for division")
x= float(input("value of x? "))
y= float(input("value of y? "))

z = round(x/y, 2)
a = x/ y
print(z)
print("value of a", a)
print(f"{a: .2f}")