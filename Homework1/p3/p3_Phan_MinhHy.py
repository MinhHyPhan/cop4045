"""The module for finding duplicate substrings.
This module finds duplicate substrings within a given string,
either of a specific length or the longest possible depending on the user.
"""


def find_dup_str(s, n):
    """This function is to find the first duplicated substring of a given
    length.
    """
    if n <= 0 or n > len(s) // 2:
        return ""

    for i in range(len(s) - n + 1):
        substring = s[i:i+n]

        for j in range(i + n, len(s) - n + 1):
            if s[j:j+n] == substring:
                return substring

    return ""


def find_max_dup(s):
    """This function is to find the longest duplicated substring in a string.
    It uses find_dup_str to check lengths from longest to shortest.
    """
    max_length = len(s) // 2

    for length in range(max_length, 0, -1):
        result = find_dup_str(s, length)

        if result != "":
            return result

    return ""


def main():
    """Main function to run the duplicate substring finder program."""
    print("Welcome to the duplicate substring Finder, Manager Esquire!")
    print("Please select an option of which function you want to use!")
    print("Press 'a' to find the first duplicate substring!")
    print("Press 'b' to find the longest duplicate substring!")
    print("////////////")

    choice = input("Type 'a' or 'b' : ")

    if choice == "a":
        print("You have selected a!")
        s = input("Please enter the string: ")
        n = int(input("Please enter the length of the substring: "))

        result = find_dup_str(s, n)

        if result != "":
            print(f"Result: '{result}'")
        else:
            print("Result: No duplicate substring of that length found")

    elif choice == "b":
        print("You have selected b!")
        s = input("Please enter a string: ")

        result = find_max_dup(s)

        if result != "":
            print(f"Result: '{result}'")
        else:
            print("Result: No duplicate substring found")

    else:
        print("Invalid choice! Please run the program again and enter"
              " a or b.")


if __name__ == "__main__":
    main()
