# ==========================================
# CONTROL FLOW IN PYTHON
# If-Else, For Loop, While Loop,
# Break and Continue
# ==========================================


# 1. IF-ELSE

age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# IF-ELIF-ELSE

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# NESTED IF

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry not allowed")


# ==========================================
# 2. FOR LOOP
# ==========================================

# Print numbers 1 to 5

for i in range(1, 6):
    print(i)


# Loop through a list

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# Loop through a string

name = "Yogita"

for letter in name:
    print(letter)


# Print even numbers

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# ==========================================
# 3. WHILE LOOP
# ==========================================

i = 1

while i <= 5:
    print(i)
    i += 1


# While loop with condition

number = 10

while number > 0:
    print(number)
    number -= 2


# ==========================================
# 4. BREAK
# ==========================================

for i in range(1, 11):

    if i == 6:
        break

    print(i)


# ==========================================
# 5. CONTINUE
# ==========================================

for i in range(1, 11):

    if i == 5:
        continue

    print(i)


# ==========================================
# 6. BREAK + CONTINUE TOGETHER
# ==========================================

for i in range(1, 11):

    if i == 3:
        continue

    if i == 8:
        break

    print(i)