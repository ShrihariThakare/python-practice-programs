try:
    num = int(input("Enter an integer number: "))
    print("You entered:", num)

except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")

else:
    print("Input accepted successfully.")

finally:
    print("Program execution completed.")
