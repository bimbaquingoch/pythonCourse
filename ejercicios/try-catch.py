try:
    age = int(input("Edad: "))
    income = 30000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("age cannot be 0.")
except ValueError as identifier:
    print(f"must be a number\n{identifier}")
