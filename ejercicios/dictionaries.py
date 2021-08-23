# dictionaries
customer = [
    {
        "name": "Yon",
        "age": 23,
        "profesion": "programmer",
    },
    {
        "name": "alan",
        "age": 24,
        "profesion": "trader",
    },
]

# name, age, profesion = customer

customer1, customer2 = customer
name, age, profesion = customer1
name, age, profesion = customer2

customer1[name] = "Maria"

print(customer2[age])
print(customer2[profesion])
print(customer1[profesion])
print(customer1[name])

# phone number exercise

numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "sevent",
    "8": "eight",
    "9": "nine",
}

phone = input("phone number: ")
output = ""

for number in phone:
    output += numbers.get(number, "!") + " "

print(output)
