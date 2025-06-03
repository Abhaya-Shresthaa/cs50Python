name =  input("Enter your name: ")

#like switch case
#for default we use underscore( _ )

match name:
    case "Abhaya":
        print("firstName")
    case "Shrestha":
        print("Surname")
    case "firstname":
        print("Abhaya")
    case _:
        print("Unknown")
        
match name:
    case "Abhaya" | "Hello":
        print("First name")
    case "Shrestha" | "Hi":
        print("Surname")
        