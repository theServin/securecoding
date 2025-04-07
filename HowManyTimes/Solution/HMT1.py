# How Many Times 1 Exception Handling

try:
    number1 = int(input("Enter a whole number: "))
    number2 = int(input("Enter a whole number: "))
    addition = number1 + number2
    average = addition / 2
    print(f"Addition: {addition}")
    print(f"Average: {average:.1f}")

except ValueError:
    print("Invalid input. Only whole numbers")

finally:
    print("Terminating...")

"""
Basic Input and Output
# Step 1: Get two numbers from the user and perform calculations
number1 = int(input("Enter a whole number: "))
number2 = int(input("Enter a whole number: "))

addition = number1 + number2
average = addition / 2

print(f"Addition: {addition}")
print(f"Average: {average:.1f}")

##########

Handling Invalid Input (ValueError Exception)
# Step 2: Add basic exception handling for invalid inputs
try:
    number1 = int(input("Enter a whole number: "))
    number2 = int(input("Enter a whole number: "))

    addition = number1 + number2
    average = addition / 2

    print(f"Addition: {addition}")
    print(f"Average: {average:.1f}")

except ValueError:
    print("Invalid input. Only whole numbers are allowed.")

##########
Use finally for Cleanup Messages
# Step 3: Add 'finally' to ensure cleanup message is always displayed
try:
    number1 = int(input("Enter a whole number: "))
    number2 = int(input("Enter a whole number: "))

    addition = number1 + number2
    average = addition / 2

    print(f"Addition: {addition}")
    print(f"Average: {average:.1f}")

except ValueError:
    print("Invalid input. Only whole numbers are allowed.")

finally:
    print("Terminating...")
"""