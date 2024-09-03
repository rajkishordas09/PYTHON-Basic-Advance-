names = input("Enter a list of names separated by spaces: ").split()

capitalized_names = [name.capitalize() for name in names]

print("Capitalized names:")
for name in capitalized_names:
    print(name,end=" ")
