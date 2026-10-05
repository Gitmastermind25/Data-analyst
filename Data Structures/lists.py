# ==========================================
# LISTS IN PYTHON
# ==========================================

# Creating a list
numbers = [10, 20, 30, 40, 50]

print(numbers)


# Accessing elements
print(numbers[0])
print(numbers[2])
print(numbers[-1])


# Changing an element
numbers[0] = 100
print(numbers)


# Adding an element
numbers.append(60)
print(numbers)


# Adding at a specific position
numbers.insert(1, 15)
print(numbers)


# Removing an element
numbers.remove(30)
print(numbers)


# Removing the last element
numbers.pop()
print(numbers)


# Length of list
print(len(numbers))


# Check if element exists
print(20 in numbers)


# Loop through list
for number in numbers:
    print(number)


# Sorting
numbers.sort()
print(numbers)


# Reversing
numbers.reverse()
print(numbers)