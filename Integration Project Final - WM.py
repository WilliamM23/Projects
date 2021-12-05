"""Integration Project."""
import math  # import math is a built-in module that provides access to

# a list of mathematical functions.

__author__ = "William Mollaymeri"
"""This program is a calculator with different functions."""


def square_area(side):  # function that accepts parameters
    """
    The purpose of this function is to calculate the area of a square using
     the side of the square and the power function from the math library.
     Parameter:
     side - floating-point number, side of the square.

     """
    area = pow(side, 2)  # pow is the power function
    print("The area of the square is: ", format(area, '.2f'))


# Defining the function that calculates the area of a rectangle.
def rectangle_area(length, width):  # function that accepts parameters
    """
    The purpose of this function is to calculate the area of a rectangle
     using the formula that requires the length and the width.
     Parameters:
     length - floating-point number, the length of the rectangle.
     width - floating-point number, the width of the rectangle.

     """
    area = length * width
    print("The area of the rectangle is: ", format(area, '.2f'))


# Defining the function that calculates the area of a circle.
def circle_area(r):  # function that accepts parameters
    """
    The purpose of this function is to calculate the area of a circle using
     its mathematical formula that requires the radius and uses pi from the
      math library.
      Parameter:
     r - floating-point number, radius of the circle.

     """
    area = math.pi * r * r
    print("The area of the circle is: ", format(area, '.2f'))


# Defining the main function.
def main():
    """This is the main function of a calculator with different functions."""
    greetings_number = 0
    invalid_input = True  # This code tests if the input is valid in
    # order for the program not to crash.
    while invalid_input:
        try:  # Tries if the input is valid.
            greetings_number = int(input(
                "Choose and enter a number to start the program: "))
            invalid_input = False  # When the input is valid it stops the
            # loop and proceeds.
        except ValueError:  # When the input is invalid it shows the following
            # message and requests a valid input to proceed.
            print("Error. Please enter a whole number.")
    print("Greetings!" *
          greetings_number)  # This line prints the word Greetings greetings_
    # number times.
    name = input("Enter your name: ")  # Input for the name of the user
    print(
        "Hello " + name + "!" + " This program is a calculator with different"
                                "functions." + " These functions are: ")
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
    while True:  # Creates a loop to make the code below run over and over
        # again unless 0 is entered as an input.
        chosen_function = input(
            "Type a number to choose a function from the list: ")
        if chosen_function == '1' or chosen_function == '2' \
                or chosen_function \
                == '3' or chosen_function == '4' or chosen_function == '5' \
                or chosen_function == '6' or chosen_function == '7' or \
                chosen_function == '8':
            # If the chosen function is a value from the list the program
            # prints Integration Project.
            print("Integration Project")
            math_is_boring = False  # making math_is_boring False
            if not math_is_boring:  # using operator not.
                print("Math is FUN!")
        # Addition
        if chosen_function == '1':  # Assigning number 1 to the addition
            # function using conditionals.
            total = 0  # Total is 0 at the beginning of this program.
            invalid_input = True
            while invalid_input:  # This code tests if the input is valid in
                # order for the program not to crash.
                try:  # Tries if the input is valid.
                    number = float(input("Enter a number: "))
                    total += number  # This adds the input from user to the
                    # total.
                    while number > 0:
                        invalid_input = True
                        while invalid_input:
                            try:
                                number = float(input(
                                    "Add another number. If you want to stop"
                                    " enter 0.-->"" "))
                                invalid_input = False  # When the input is
                                # valid it stops the loop and proceeds.
                            except ValueError:  # When the input is invalid it
                                # shows the following message and requests a
                                # valid input to proceed.
                                print("Error. Please enter a number.")
                        if number == 0:
                            break
                        total += int(
                            number)  # This adds the input from user to the
                        # total.
                    print("The total is",
                          format(total, '.2f'))  # Printing the result.
                    invalid_input = False  # When the input is valid it stops
                # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")
        # Subtraction
        elif chosen_function == '2':  # Assigning number 2 to the subtraction
            # function using conditionals.
            num1 = 0
            invalid_input = True
            while invalid_input:  # This code tests if the input is valid in
                # order for the program not to crash.
                try:  # Tries if the input is valid.
                    num1 = float(input("Enter the first number: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")
            num2 = 0
            invalid_input = True
            while invalid_input:  # This code tests if the input is valid in
                # order for the program not to crash.
                try:  # Tries if the input is valid.
                    num2 = float(input("Enter the second number: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")
            print("The result is ", num1 - num2)
            # Multiplication
        elif chosen_function == '3':  # Assigning number 3 to the
            # multiplication function using conditionals.
            num1 = 0
            invalid_input = True
            while invalid_input:  # This code tests if the input is valid in
                # order for the program not to crash.
                try:  # Tries if the input is valid.
                    num1 = float(input("Enter the first number: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")
            num2 = 0
            invalid_input = True
            while invalid_input:  # This code tests if the input is valid in
                # order for the program not to crash.
                try:  # Tries if the input is valid.
                    num2 = float(input("Enter the second number: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")
            print("The product is ", num1 * num2)
            # Division
        elif chosen_function == '4':  # Assigning number 4 to the division
            # function using conditionals.
            num1 = 0
            invalid_input = True  # This code tests if the input is valid in
            # order for the program not to crash.
            while invalid_input:
                try:  # Tries if the input is valid.
                    num1 = float(input("Enter the first number: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")
            num2 = 1
            invalid_input = True
            while invalid_input:  # This code tests if the input is valid in
                # order for the program not to crash.
                try:  # Tries if the input is valid.
                    num2 = float(input("Enter the second number: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")

            if num2 != 0:  # Allows the operation to happen only if the
                # divisor is different from 0 skipping math errors.
                print("The result is ", num1 / num2)
                print("The quotient is ", int(num1 // num2),
                      " and the remainder is ", num1 % num2)
            # % is called modulus operator and calculates the remainder of
            # dividing two values.
            # // is called floor division operator and it rounds the result
            # of division down to the nearest whole number.
            else:
                print("MATH ERROR. The divisor should be different from 0.")

            # Exponentiation
        elif chosen_function == '5':  # Assigning number 5 to the
            # exponentiation function using conditionals.
            num1 = 0
            invalid_input = True
            while invalid_input:  # This code tests if the input is valid in
                # order for the program not to crash.
                try:  # Tries if the input is valid.
                    num1 = float(input("Enter the first number: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")
            num2 = 0
            invalid_input = True
            while invalid_input:  # This code tests if the input is valid in
                # order for the program not to crash.
                try:  # Tries if the input is valid.
                    num2 = float(input("Enter the second number: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")
            print(num1, "in the", num2, "power equals", num1 ** num2,
                  sep='  ')
            # Numbers Comparison
        elif chosen_function == '6':  # Assigning number 6 to the numbers
            # comparison function using conditionals.
            num1 = 0
            invalid_input = True
            while invalid_input:  # This code tests if the input is valid in
                # order for the program not to crash.
                try:  # Tries if the input is valid.
                    num1 = float(input("Enter the first number: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")
            num2 = 0
            invalid_input = True
            while invalid_input:  # This code tests if the input is valid in
                # order for the program not to crash.
                try:  # Tries if the input is valid.
                    num2 = float(input("Enter the second number: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a number.")
            print(num1, "in the", num2, "power equals", num1 ** num2,
                  sep='  ')
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
                side = 0
                invalid_input = True
                while invalid_input:  # This code tests if the input is valid
                    # in order for the program not to crash.
                    try:  # Tries if the input is valid.
                        side = float(
                            input("Enter the length of square side: "))
                        invalid_input = False  # When the input is valid it
                        # stops the loop and proceeds.
                    except ValueError:  # When the input is invalid it shows
                        # the following message and requests a valid input
                        # to proceed.
                        print("Error. Please enter a number.")
                square_area(side)  # Calling the function
            elif shape == '2':
                length = 0
                invalid_input = True
                while invalid_input:  # This code tests if the input is valid
                    # in order for the program not to crash.
                    try:  # Tries if the input is valid.
                        length = float(input("Enter the length: "))
                        invalid_input = False  # When the input is valid it
                        # stops the loop and proceeds.
                    except ValueError:  # When the input is invalid it shows
                        # the following message and requests a valid input
                        # to proceed.
                        print("Error. Please enter a number.")
                width = 0
                invalid_input = True
                while invalid_input:  # This code tests if the input is valid
                    # in order for the program not to crash.
                    try:  # Tries if the input is valid.
                        width = float(input("Enter the width: "))
                        invalid_input = False  # When the input is valid it
                        # stops the loop and proceeds.
                    except ValueError:  # When the input is invalid it shows
                        # the following message and requests a valid input
                        # to proceed.
                        print("Error. Please enter a number.")
                rectangle_area(length, width)  # Calling the function
            elif shape == '3':
                r = 0
                invalid_input = True
                while invalid_input:
                    try:  # Tries if the input is valid.
                        r = float(input("Enter the radius: "))
                        invalid_input = False  # When the input is valid it
                        # stops the loop and proceeds.
                    except ValueError:  # When the input is invalid it shows
                        # the following message and requests a valid input
                        # to proceed.
                        print("Error. Please enter a number.")
                circle_area(r)  # Calling the function
            elif shape != '1' and shape != '2' and shape != '3':
                # if the user choose a number different from the ones listed
                # the following message will be received.
                print("You did not choose a shape from the list.")
        # Generating Lists
        elif chosen_function == '8':
            start = 0
            invalid_input = True
            while invalid_input:
                try:  # Tries if the input is valid.
                    start = int(input("Enter the starting value: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a whole number.")
            ending = 0
            invalid_input = True
            while invalid_input:
                try:  # Tries if the input is valid.
                    ending = int(input("Enter the ending value: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a whole number.")
            inc = 0
            invalid_input = True
            while invalid_input:
                try:  # Tries if the input is valid.
                    inc = int(input("Enter the increment value: "))
                    invalid_input = False  # When the input is valid it stops
                    # the loop and proceeds.
                except ValueError:  # When the input is invalid it shows the
                    # following message and requests a valid input to proceed.
                    print("Error. Please enter a whole number.")
            for x in range(start, ending + 1, inc):
                print(x, end=' ')
        elif chosen_function == '0':  # If the user inputs 0 the loop
            # will stop.
            break
        else:  # If the number chosen in the beginning was not from 1-6 it
            # directs user to choose a number from the list.
            print("Please choose a number from the list", end='. ')


if __name__ == '__main__':
    main()
# References: https://www.w3schools.com, https://www.geeksforgeeks.org/
