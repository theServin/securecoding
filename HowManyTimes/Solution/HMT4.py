# How Many Times 4 Arrays (Lists)

def is_numeric(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

addition = 0
counter = 0
valid_numbers = []
invalid_numbers = []

while True:
    numbers = input("Enter a whole number ('exit' to quit): ")
    if numbers.lower() == 'exit':
        break
    if is_numeric(numbers):
        num = int(numbers)
        addition += num
        counter += 1
        valid_numbers.append(num)
    else:
        print(f"'{numbers}' is invalid. Enter a whole number")
        invalid_numbers.append(numbers)

if valid_numbers:
    print("Valid numbers that were entered: ", end="")
    for i, num in enumerate(valid_numbers):
        if i > 0:
            print(", ", end="")
        print(num, end="")
    print()
    average = addition / counter
    print(f"Addition: {addition}")
    print(f"Average: {average:.1f}")
else:
    print("No valid numbers were entered.")

if invalid_numbers:
    print("Invalid numbers that were entered: ", end="")
    for i, num in enumerate(invalid_numbers):
        if i > 0:
            print(", ", end="")
        print(num, end="")
    print()