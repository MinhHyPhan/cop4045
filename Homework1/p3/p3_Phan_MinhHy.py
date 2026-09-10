"""The module for finding duplicate substrings.
This module finds duplicate substrings within a given string,
either of a specific length or the longest possible depending on the user.
"""


def find_dup_str(s, n):
    """Find the first duplicated substring of a given length."""

    # Make sure the requested length is valid.
    # A duplicate needs to appear at least twice in the string.
    if n <= 0 or n > len(s) // 2:
        return ""

    # Check every possible starting position for the substring.
    for i in range(len(s) - n + 1):

        # Get the substring starting at position i.
        substring = s[i:i+n]

        # Look at the rest of the string for the same substring.
        # Start at i + n so we do not compare the substring with itself.
        for j in range(i + n, len(s) - n + 1):

            # If another copy of the substring is found, return it.
            if s[j:j+n] == substring:
                return substring

    # Return an empty string if no duplicate was found.
    return ""


def find_max_dup(s):
    """Find the longest duplicated substring in a string."""

    # A duplicated substring can be at most half the length of the string.
    max_length = len(s) // 2

    # Start with the longest possible length and work downward.
    for length in range(max_length, 0, -1):

        # Check if there is a duplicate substring of this length.
        result = find_dup_str(s, length)

        # If one is found, return it immediately.
        # Since we started with the longest length, this is the longest one.
        if result != "":
            return result

    # Return an empty string if there are no duplicates.
    return ""


def main():
    """Main function to run the duplicate substring finder program."""

    # Display the welcome message and instructions.
    print("Welcome to the duplicate substring Finder, Manager Esquire!")
    print("Please select an option of which function you want to use!")
    print("Press 'a' to find the first duplicate substring!")
    print("Press 'b' to find the longest duplicate substring!")
    print("////////////")

    # Ask the user which function they want to use.
    choice = input("Type 'a' or 'b' : ")

    # Option A finds a duplicate of a specific length.
    if choice == "a":
        print("You have selected a!")

        # Ask the user for the string to search.
        s = input("Please enter the string: ")

        # Ask how long the duplicate substring should be.
        n = int(input("Please enter the length of the substring: "))

        # Search for the duplicate substring.
        result = find_dup_str(s, n)

        # Display the result if a duplicate was found.
        if result != "":
            print(f"Result: '{result}'")
        else:
            print("Result: No duplicate substring of that length found")

    # Option B finds the longest duplicate substring.
    elif choice == "b":
        print("You have selected b!")

        # Ask the user for the string to search.
        s = input("Please enter a string: ")

        # Search for the longest duplicate substring.
        result = find_max_dup(s)

        # Display the result if a duplicate was found.
        if result != "":
            print(f"Result: '{result}'")
        else:
            print("Result: No duplicate substring found")

    # Handle any choice other than a or b.
    else:
        print("Invalid choice! Please run the program again and enter"
              " a or b.")


# Start the program by calling main().
if __name__ == "__main__":
    main()

