# while True:
#     input("enter a name:")

# s = {
#     "hello" : "hi",
#     "man" :"woman"
# }
# print(s["hey"])
items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
        item = input("Item: ").title()
        total = total + items[item]
        print(f"Total: ${total:.2f}")
    except EOFError:
        break
    except KeyError:
        continue
