"""
Program Name: Geometry Calculator
Author: Arashid7868
Purpose: Provides a menu-driven geometry calculator that
         calculates circle and rectangle measurements using
         functions imported from separate modules.
Starter Code: None; developed for Chapter 8 Lab 1.
Date: September 19, 2026
"""

import circle as c
import rectangle as r


# Aliases are necessary because both modules contain a function
# named calc_area(), and the aliases identify which module's
# function should be called.


def get_positive_number(prompt):
    """Prompt the user until a positive numeric value is entered."""
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Please enter a valid number.")


def display_menu():
    """Display the Geometry Calculator menu."""
    print("\nGeometry Calculator")
    print("-------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")


def main():
    """Run the Geometry Calculator until the user chooses to exit."""
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("\nInvalid choice. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            radius = get_positive_number("Enter the radius of the circle: ")
            area = c.calc_area(radius)
            print(f"\nThe area of the circle is {area:.3f}.")
            input("\nPress Enter to continue...")

        elif choice == 2:
            radius = get_positive_number("Enter the radius of the circle: ")
            circumference = c.calc_circumference(radius)
            print(
                f"\nThe circumference of the circle is "
                f"{circumference:.3f}."
            )
            input("\nPress Enter to continue...")

        elif choice == 3:
            width = get_positive_number(
                "Enter the width of the rectangle: "
            )
            height = get_positive_number(
                "Enter the height of the rectangle: "
            )
            area = r.calc_area(width, height)
            print(f"\nThe area of the rectangle is {area:.3f}.")
            input("\nPress Enter to continue...")

        elif choice == 4:
            width = get_positive_number(
                "Enter the width of the rectangle: "
            )
            height = get_positive_number(
                "Enter the height of the rectangle: "
            )
            perimeter = r.calc_perimeter(width, height)
            print(f"\nThe perimeter of the rectangle is {perimeter:.3f}.")
            input("\nPress Enter to continue...")

        elif choice == 5:
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
