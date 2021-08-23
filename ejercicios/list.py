names = ["yon", "bob", "mario", "sara", "nayeli"]
print(names[2:4])

numbers = [3, 5, 14, 3, 67, 45, 32, 1]
maxN = numbers[0]
for item in numbers:
    if item > maxN:
        maxN = item

print(maxN)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in matrix:
    print(row)
    for number in row:
        print(number)

numbers = [5, 2, 1, 7, 4]

numbers.append(3)
print(numbers)
numbers.insert(0, 4)
print(numbers)
numbers.remove(7)
print(numbers)
# numbers.clear()
numbers.pop()
print(numbers)
print(numbers.index(4))
print(7 in numbers)
print(numbers.count(4))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
copy = numbers.copy()
print(copy)
copy.append(33)
print(copy)

# remove the duplicates

numbers = [5, 2, 1, 7, 4, 5, 2, 1, 33, 45]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)
