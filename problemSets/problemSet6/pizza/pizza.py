import sys
import csv
from tabulate import tabulate
def main():
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
        sys.exit(1)
    else:
        if not sys.argv[1].endswith('.csv'):
            print("Not a CSV file")
            sys.exit(1)
        else:
            menu = []
            with open (sys.argv[1]) as file:
                # reader = csv.DictReader(file)
                # for row in reader:
                #     menu.append({"Sicilian Pizza" : row["Sicilian Pizza"],  "Small": row["Small"], "Large": row["Large"]})
            #headers = ["Sicilian Pizza" , "Small", "Large"]
                reader = csv.reader(file)
                for row in reader:
                    menu.append({"Sicilian Pizza" : row[0],  "Small": row[1], "Large": row[2]})
            print(tabulate(menu, headers = "firstrow",tablefmt = 'grid'))
        
if __name__ == "__main__":
    main()