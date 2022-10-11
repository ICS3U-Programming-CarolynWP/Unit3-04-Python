#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/11
# Asks the user to enter an integer.
# Uses IF statements to display text
# Based on whether the integer is
# Positive, negative, or zero.


def main():

    # title of the program
    print("Integers")

    # input for the integer
    integer = int(input("Enter an integer (whole number) here: "))

    # if statement if the integer is positive
    if integer > 0:
        print("The integer {} is positive!".format(integer))

    # else if the integer is negative
    elif integer < 0:
        print("The integer {} is negative!".format(integer))

    # else statement if the integer is zero
    else:
        print("The integer {} is zero.".format(integer))


if __name__ == "__main__":
    main()
