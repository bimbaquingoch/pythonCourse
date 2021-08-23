prices = [10, 30, 20]
total = 0
for item in prices:
    total += item

print(f"total: {total}")
for item in ["hola", "nuevo", "luffy"]:
    print(item)

for i in range(10):
    print(i)


for i in range(5, 10, 2):
    print(i, "tt")

for x in range(2):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]

for item in numbers:
    # print("X" * item)
    output = ""
    for count in range(item):
        output += "x"
        print(count)
    print(output)
