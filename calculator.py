def calculator():
    """
    A simple command-line calculator program.
    Users can input arithmetic expressions, and the program will evaluate them.
    """
    print("Welcome to Calculator!")
    print("Enter your calculations like (2+5)*8-4/6")

    while True:
        try:
            # Take input for the calculation
            expression = input("Enter your calculation: ")

            # Evaluate the expression safely
            try:
                result = eval(expression)  # Evaluate the expression
                print(f"The result is: {result}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
            except Exception:
                print("Error: Invalid input.")

            # Ask if the user wants to calculate again
            another = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another != "yes":
                print("Thank you for using the calculator. Goodbye!")
                break
        except Exception:
            print("Unexpected error occurred.")
            break


# Run the calculator program
if __name__ == "__main__":
    calculator()
