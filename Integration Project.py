# William Mollaymeri
# This program is a calculator with different functions.
# This line requests an input from the user
import math  # Importing functions from the math library.


# Defining the function that calculates the area of a square.
def square_area(a): # function that accepts parameters
    area = pow(a, 2)
    print("The area of the square is: ", format(area, '.2f'))


# Defining the function that calculates the area of a rectangle.
def rectangle_area(a, b): # function that accepts parameters
    area = a * b
    print("The area of the rectangle is: ", format(area, '.2f'))


# Defining the function that calculates the area of a circle.
def circle_area(r): # function that accepts parameters
    area = math.pi * r * r
    print("The area of the circle is: ", format(area, '.2f'))


# Defining the main function.
def main():
    greetings_number = input(
        "Choose and enter a number to start the program: ")
    print("Greetings!" * int(
        greetings_number))  # This line prints the word Greetings greetings_number times.
    name = input("Enter your name: ")  # Input for the name of the user
    print(
        "Hello " + name + "!" + " This program is a calculator with different functions." + " These functions are: ")
    # List of the operations
    print("1-Addition")
    print("2-Subtraction")
    print("3-Product")
    print("4-Division")
    print("5-Exponentiation")
    print("6-Numbers Comparison")
    print("7-Area")
    print("8-List Generator")
    print("0-Quit")
    while True:  # Creates a loop to make the code below run over and over again unless 0 is entered as an input.
        chosen_function = input(
            "Type a number to choose a function from the list: ")
        if chosen_function == '1' or chosen_function == '2' or chosen_function \
                == '3' or chosen_function == '4' or chosen_function == '5' or \
                chosen_function == '6' or chosen_function == '7' or chosen_function == '8':
            # If the chosen function is a value from the list the program prints Integration Project.
            print("Integration Project")
            math_is_boring = False  # making math_is_boring False
            if not math_is_boring: # using operator not.
                print("Math is FUN!")
        # Addition
        if chosen_function == '1':  # Assigning number 1 to the addition function using conditionals.
            total = 0  # Total is 0 at the beginning of this program.
            number = float(input("Enter a number: "))
            total += number  # This adds the input from user to the total.
            while number > 0:
                number = float(
                    input(
                        "Add another number. If you want to stop enter 0.--> "))
                if number == 0:
                    break
                total += int(
                    number)  # This adds the input from user to the total.
            print("The total is ", format(total, '.2f'))  # Printing the result .
        # Subtraction
        elif chosen_function == '2':  # Assigning number 2 to the subtraction function using conditionals.
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("The result is ", num1 - num2)
            # Multiplication
        elif chosen_function == '3':  # Assigning number 3 to the multiplication function using conditionals.
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("The product is ", num1 * num2)
            # Division
        elif chosen_function == '4':  # Assigning number 4 to the division function using conditionals.
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 != 0:  # Allows the operation to happen only if the divisor is different from 0 skipping math errors.
                print("The result is ", num1 / num2)
                print("The quotient is ", int(num1 // num2),
                      " and the remainder is ", num1 % num2)
            # % is called modulus operator and calculates the remainder of dividing two values.
            # // is called floor division operator and it rounds the result of division down to the nearest whole number.
            else:
                print("MATH ERROR. The divisor should be different from 0.")

            # Exponentiation
        elif chosen_function == '5':  # Assigning number 5 to the exponentiation function using conditionals.
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(num1, "in the", num2, "power equals", num1 ** num2,
                  sep=' ')
            # Numbers Comparison
        elif chosen_function == '6':  # Assigning number 6 to the numbers comparison function using conditionals.
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num1 > num2:
                print(num1, " is greater than ", num2)
            elif num1 < num2:
                print(num2, " is greater than ", num1)
            else:
                print(num2, " is equal to ", num1)
        elif chosen_function == '7':
            print("Area calculator.")
            print("1- Square")
            print("2- Rectangle")
            print("3- Circle")
            shape = input("Choose a shape: ")
            if shape == '1':
                a = float(input("Enter the length of square side: "))
                square_area(a)  # Calling the function
            elif shape == '2':
                a = float(input("Enter the width: "))
                b = float(input("Enter the height: "))
                rectangle_area(a, b)  # Calling the function
            elif shape == '3':
                r = float(input("Enter the radius: "))
                circle_area(r)  # Calling the function
            elif shape != '1' and shape != '2' and shape != '3':
                # if the user choose a number different from the ones listed the
                # following message will be received.
                print("You did not choose a shape from the list.")
        # Generating Lists
        elif chosen_function == '8':
            a = int(input("Enter the starting value: "))
            b = int(input("Enter the ending value: "))
            c = int(input("Enter the increment value: "))
            for x in range(a, b + 1, c):
                print(x, end=' ')
        elif chosen_function == '0':  # If the user inputs 0 the loop will stop.
            break
        else:  # If the number chosen in the beginning was not from 1-6 it
            # directs user to choose a number from the list.
            print("Please choose a number from the list", end='. ')


main()
# References: https://www.w3schools.com, https://www.geeksforgeeks.org/
