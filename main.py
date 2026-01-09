"""
main.py

Entry point for the py_calculator application.
"""

from py_calculator.calculator import Calculator

def main() :

    """
    Main entry point for the calculator application.

    Prompts the user for an operation and two numbers,
    performs the calculation, and prints the result.
    """

    calculator = Calculator()

    print("\nWelcome to the Python Calculator!")
    print("\nSelect an operation: ")
    print("\n1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")

    input_choice = input("\nEnter your choice (1/2/3/4/5): ")

    try :
        param01 = float(input("\nEnter first number: "))
        param02 = float(input("Enter second number: "))

        if input_choice == '1' :
            result = calculator.addition(param01, param02)
            print(f"\nSum of {param01} and {param02} is: {result}")
        elif input_choice == '2' :
            difference = calculator.subtraction(param01, param02)
            print(f"\nDifference between {param01} and {param02} is: {difference}")
        elif input_choice == '3' :
            product = calculator.multiplication(param01, param02)
            print(f"\nProduct of {param01} and {param02} is: {product}")
        elif input_choice == '4' :
            quotient = calculator.division(param01, param02)
            print(f"\nQuotient of {param01} divided by {param02} is: {quotient}")
        elif input_choice == '5' :
            modulus = calculator.modulus(param01, param02)
            print(f"\nModulus of {param01} and {param02} is: {modulus}")
        else :
            print("\nInvalid input! Please select a valid operation.")
    except ValueError as error:
        print(f"\nError: {error}")

if __name__ == "__main__" :
    main()
