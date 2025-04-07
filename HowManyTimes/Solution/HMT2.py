# How Many Times 2 Loops

addition = 0
average = 0
counter = 0

while True:
    numbers = input("Enter a whole number ('exit' to quit): ")
    if numbers.lower() == "exit":
        break
    
    try: 
        numbers = int(numbers)
        addition += numbers
        counter += 1
        average = addition / counter
    
    except ValueError:
        print(f"'{numbers}' is invalid. Enter a whole number")

try:
    print(f"Addition: {addition}")
    print(f"Average: {average:.1f}")
    
except ValueError:
    print("Invalid numbers were entered")

"""
Step 1: Basic Loop for Repeated Input
# Step 1: Basic loop for repeated input
while True:
    numbers = input("Enter a whole number ('exit' to quit): ")
    if numbers.lower() == "exit":
        break
    print(f"You entered: {numbers}")  # Just to verify input for now

"""