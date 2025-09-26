
try:
    num = float(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    # Check if the number is positive, negative, or zero
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")