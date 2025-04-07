# How Many Times 3 Functions

def is_numeric(number):
    try:
        int(number)
        return True
    
    except ValueError:
        return False

addition = 0
counter = 0 

while True:
    numbers = input("Enter a whole number ('exit' to quit): ")
    if numbers.lower() == 'exit':
        break
    if is_numeric(numbers):
        addition += int(numbers)
        counter += 1
    else:
        print(f"'{numbers}' is invalid. Enter a whole number")

try:
    average = addition / counter
    print(f"Addition: {addition}")
    print(f"Average: {average}")

except ValueError:
    print("Invalid numbers were entered")