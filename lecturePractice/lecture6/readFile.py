with open("name.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    print("hello,", line, end= '')
    #print("hello,", line.rstip()) or
   
   # or directly this 
# with open("name.txt", "r") as file:
#     for line in file:
#         print("hello,", line, end= '')

names = []
with open("name.txt") as file1: # defalut is read mode
    for line in file1:
        names.append(line.rstrip())
        
names = sorted(names)
for name in names:
    print(f"{name}")
    
#for descending order
names = sorted(names, reverse= True)
for name in names:
    print(f"{name}")