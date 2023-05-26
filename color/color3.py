from crayons import red, blue

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

greeting = f"Greetings, {red(first_name)} {blue(last_name)}."

print(greeting)

