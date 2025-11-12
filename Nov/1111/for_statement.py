fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

person = {"name": "Alice", "age": 25, "city": "New York"}

for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

for i in range(3):
    print(i)
else:
    print("Loop finished without break.")

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Loop finished without break.")
