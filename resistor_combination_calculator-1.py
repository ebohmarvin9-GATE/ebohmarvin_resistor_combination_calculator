# Resistor Combination Calculator
# CTE213 Python Mini Project
# This program calculates resistance in series and parallel and
# includes an extra feature: a 4-band resistor colour-code decoder.

# Colour-code values for the first two bands (significant digits).
DIGIT_COLOURS = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "grey": 8, "gray": 8,
    "white": 9
}

# Multiplier values for the third band.
MULTIPLIER_COLOURS = {
    "black": 1, "brown": 10, "red": 100, "orange": 1_000,
    "yellow": 10_000, "green": 100_000, "blue": 1_000_000,
    "violet": 10_000_000, "grey": 100_000_000,
    "gray": 100_000_000, "white": 1_000_000_000,
    "gold": 0.1, "silver": 0.01
}

# Tolerance values for the fourth band.
TOLERANCE_COLOURS = {
    "brown": 1, "red": 2, "green": 0.5, "blue": 0.25,
    "violet": 0.1, "grey": 0.05, "gray": 0.05,
    "gold": 5, "silver": 10, "none": 20
}


def get_positive_number(prompt):
    """Ask for a positive number and keep asking until it is valid."""
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number, for example 100 or 2.2.")


def get_resistor_values():
    """Collect the resistance values and return them in a list."""
    while True:
        try:
            count = int(input("How many resistors do you have? "))
            if count > 0:
                break
            print("Enter at least 1 resistor.")
        except ValueError:
            print("Invalid input. Enter a whole number, such as 3.")

    resistors = []
    for index in range(count):
        value = get_positive_number(f"Enter the value of resistor {index + 1} in ohms: ")
        resistors.append(value)

    return resistors


def calculate_series(resistors):
    """Return total resistance when all resistors are connected in series."""
    return sum(resistors)


def calculate_parallel(resistors):
    """Return total resistance when all resistors are connected in parallel."""
    reciprocal_sum = 0
    for resistance in resistors:
        reciprocal_sum += 1 / resistance
    return 1 / reciprocal_sum


def decode_colour_code():
    """Decode a four-band resistor colour code."""
    print("\nAvailable digit colours: black, brown, red, orange, yellow,")
    print("green, blue, violet, grey, white.")
    print("Multiplier also accepts gold and silver.")
    print("Tolerance accepts brown, red, green, blue, violet, grey,")
    print("gold, silver, or none.")

    while True:
        first = input("First band (first digit): ").strip().lower()
        second = input("Second band (second digit): ").strip().lower()
        third = input("Third band (multiplier): ").strip().lower()
        fourth = input("Fourth band (tolerance): ").strip().lower()

        if (first in DIGIT_COLOURS and second in DIGIT_COLOURS
                and third in MULTIPLIER_COLOURS
                and fourth in TOLERANCE_COLOURS):
            break

        print("One or more colours are not valid. Please enter the colours again.")

    first_two_digits = DIGIT_COLOURS[first] * 10 + DIGIT_COLOURS[second]
    resistance = first_two_digits * MULTIPLIER_COLOURS[third]
    tolerance = TOLERANCE_COLOURS[fourth]

    print(f"Decoded resistance: {resistance:g} ohms")
    print(f"Tolerance: ±{tolerance:g}%")
    return resistance


def main():
    """Display the menu and run the option selected by the user."""
    while True:
        print("\n===== RESISTOR CALCULATOR =====")
        print("1. Calculate series and parallel resistance")
        print("2. Decode a 4-band resistor colour code")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            resistor_values = get_resistor_values()
            series_total = calculate_series(resistor_values)
            parallel_total = calculate_parallel(resistor_values)

            print("\n--- CALCULATION RESULTS ---")
            print(f"Series resistance: {series_total:g} ohms")
            print(f"Parallel resistance: {parallel_total:g} ohms")

        elif choice == "2":
            decode_colour_code()

        elif choice == "3":
            print("Thank you for using the Resistor Calculator. Goodbye!")
            break

        else:
            print("Invalid menu choice. Please select 1, 2, or 3.")


# This line starts the program when the file is run.
if __name__ == "__main__":
    main()
