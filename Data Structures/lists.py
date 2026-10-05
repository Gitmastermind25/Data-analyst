# ==========================================
# LISTS IN PYTHON
# ==========================================


# 1. INTRODUCTION TO LISTS
# A list stores multiple values in one variable.
# Lists are ordered, changeable, and allow duplicates.

numbers = [10, 20, 30, 40, 50]

print(numbers)


# 2. CREATING LISTS

numbers = [10, 20, 30, 40, 50]
names = ["Yogita", "Rahul", "Aman"]
mixed = [10, "Python", 8.5, True]

print(numbers)
print(names)
print(mixed)

# Empty list
empty_list = []
print(empty_list)


# 3. ACCESSING LIST ELEMENTS

numbers = [10, 20, 30, 40, 50]

print(numbers[0])       # First element
print(numbers[2])       # Third element
print(numbers[-1])      # Last element
print(numbers[-2])      # Second last element


# 4. MODIFYING LIST ELEMENTS

numbers = [10, 20, 30, 40, 50]

numbers[0] = 100
print(numbers)

numbers[2] = 300
print(numbers)


# 5. LIST METHODS

numbers = [10, 20, 30, 40]

# Add element
numbers.append(50)
print(numbers)

# Add at a specific position
numbers.insert(1, 15)
print(numbers)

# Remove a value
numbers.remove(30)
print(numbers)

# Remove last element
numbers.pop()
print(numbers)

# Find length
print(len(numbers))

# Sort
numbers.sort()
print(numbers)

# Reverse
numbers.reverse()
print(numbers)

# Count an element
print(numbers.count(10))

# Find position
print(numbers.index(20))


# 6. SLICING LISTS

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:3])     # 10, 20, 30
print(numbers[2:5])     # 30, 40, 50
print(numbers[:3])      # First 3
print(numbers[3:])      # From index 3
print(numbers[:])       # Complete list
print(numbers[::-1])    # Reverse list


# 7. ITERATING OVER LISTS

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# Using index

for i in range(len(numbers)):
    print(numbers[i])


# 8. LIST COMPREHENSIONS

numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)


# Even numbers

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)


# 9. NESTED LISTS

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

# Access elements
print(matrix[0])
print(matrix[0][1])
print(matrix[2][2])


# Loop through nested list

for row in matrix:
    for value in row:
        print(value)


# 10. PRACTICAL EXAMPLE

marks = [80, 75, 90, 85, 70]

print("Marks:", marks)
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))


# COMMON ERRORS

numbers = [10, 20, 30]

# IndexError happens when index does not exist
# print(numbers[5])

# ValueError happens when value does not exist
# numbers.remove(100)