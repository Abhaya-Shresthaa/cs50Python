camelCaseInput = input("camelCase: ")
snake_case = []
for l in camelCaseInput:
    if l.isupper():
        snake_case.append('_')
        snake_case.append(l.lower())
    else:
        snake_case.append(l)
final_snake_case = "".join(snake_case)
print(final_snake_case)
        
