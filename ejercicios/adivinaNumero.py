secret_number = 9
newNumber = 0
limit_count = 1
limit = 3

while limit_count <= limit:
    numero = int(input("guess: "))
    limit_count += 1
    if numero == secret_number:
        print("you won!")
        break
else:
    print("Sorry you fail!")
