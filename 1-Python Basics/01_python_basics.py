# ==========================================
# PYTHON BASICS
# Variables, Data Types, Input/Output,
# Operators, Type Casting
# ==========================================


# 1. VARIABLES
name = "Yogita"
age = 20
cgpa = 8.5
is_student = True

print(name)
print(age)
print(cgpa)
print(is_student)


# 2. DATA TYPES
name = "Yogita"       # String
age = 20              # Integer
cgpa = 8.5            # Float
is_student = True     # Boolean

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))


# 3. INPUT / OUTPUT
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name)
print("Your age is", age)


# 4. OPERATORS
a = 10
b = 3

# Arithmetic Operators
print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor Division
print(a % b)    # Modulus
print(a ** b)   # Power


# Comparison Operators
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# Logical Operators
print(a > 5 and b < 5)
print(a > 5 or b > 5)
print(not(a > 5))


# 5. TYPE CASTING

# String to Integer
x = "100"
x = int(x)
print(x)
print(type(x))

# Integer to Float
y = 10
y = float(y)
print(y)
print(type(y))

# Integer to String
z = 50
z = str(z)
print(z)
print(type(z))

# Float to Integer
price = 99.99
price = int(price)
print(price)
print(type(price))