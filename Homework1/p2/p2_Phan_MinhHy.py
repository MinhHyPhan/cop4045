"""The module for finding Pythagorean triples. It finds all Pythagorean
triples (x, y, z) where x² + y² = z² within a specified range that will
be entered by the user.
"""


def find_pythagorean(n):
    """Find all Pythagorean triples up to a given maximum value.

    This function finds all triples where all three numbers
    are less than or equal to n.
    """
    # Create an empty list to store the triples that are found.
    triples = []

    # Loop through possible values for x.
    for x in range(1, n + 1):

        # Start y at x so that the same combinations are not repeated.
        for y in range(x, n + 1):

            # Start z at y to keep the numbers in ascending order.
            for z in range(y, n + 1):

                # Check if x² + y² is equal to z².
                if x * x + y * y == z * z:

                    # Add the valid Pythagorean triple to the list.
                    triples.append((x, y, z))

    # Return the complete list of triples.
    return triples


def main():
    """Main function to run the Pythagorean triples finder program."""
    print("Welcome to the Pythagorean Triples Finder, dear manager bud!")
    print("Please enter a positive integer n, this will be the largest"
          " number in the list")
    print("To exit, press Enter!\n")

    # Continue asking the user for values until they press Enter.
    while True:

        # Ask the user to enter the maximum number.
        n_input = input("Enter n: ")

        # If the user presses Enter without entering a number,
        # end the program.
        if n_input.strip() == "":
            print("Goodbye! Catch you later!")
            break

        # Convert the user's input from a string to an integer.
        n = int(n_input)

        # Find all Pythagorean triples up to the value of n.
        triples = find_pythagorean(n)

        # Check whether any triples were found.
        if len(triples) == 0:
            print("No Pythagorean triples found")

        else:
            # Display the maximum value used for the search.
            print(f"\nPythagorean triples where 0 < x, y, z <= {n}:")

            # Go through each triple in the list and display it.
            for x, y, z in triples:
                print(f"({x}, {y}, {z}) -> {x}² + {y}² = {z}²")

            # Display the total number of triples that were found.
            print(f"There are {len(triples)} triple numbers found!\n")


# Run the main function when this file is executed directly.
if __name__ == "__main__":
    main()
    