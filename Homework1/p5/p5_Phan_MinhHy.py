"""Interactive Caesar Cipher program.

This program can encrypt and decrypt messages and
count the frequency of letters in a message.
"""


def caesar_cipher(text, shift):
    """Encrypt text using a Caesar cipher."""
    result = ""

    # Go through every character in the message.
    for char in text:

        # Check if the character is an uppercase letter.
        if "A" <= char <= "Z":
            # Convert the letter to a number from 0 to 25.
            position = ord(char) - ord("A")

            # Apply the shift and wrap around the alphabet.
            new_position = (position + shift) % 26

            # Convert the number back into a letter.
            result += chr(new_position + ord("A"))

        # Check if the character is a lowercase letter.
        elif "a" <= char <= "z":
            position = ord(char) - ord("a")
            new_position = (position + shift) % 26
            result += chr(new_position + ord("a"))

        else:
            # Keep spaces and other characters unchanged.
            result += char

    return result


def caesar_decipher(cyphertext, shift):
    """Decrypt a Caesar-encrypted string."""
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
    """Count how many times each letter appears in the text."""
    frequency = {}

    # Create an entry for every letter of the alphabet.
    for i in range(26):
        letter = chr(ord("a") + i)
        frequency[letter] = 0

    # Count each alphabetic character.
    for char in text.lower():
        if "a" <= char <= "z":
            frequency[char] += 1

    return frequency


def main():
    """Run the interactive Caesar Cipher program."""
    print("Welcome to the Caesar Cipher, Manager Esquire!")
    print("////////////////////////////")

    # Get a message from the user.
    text = input("Enter your message: ")

    # Get the shift amount.
    shift = int(input("Enter the shift value: "))

    while True:
        print("\nMenu:")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Show letter frequency")
        print("4. Show all")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            encrypted = caesar_cipher(text, shift)
            print(f"Ciphered text: {encrypted}")

        elif choice == "2":
            decrypted = caesar_decipher(text, shift)
            print(f"Deciphered text: {decrypted}")

        elif choice == "3":
            frequency = letter_frequency(text)

            print("Letter frequency:")
            for letter, count in frequency.items():
                print(f"{letter}: {count}")

        elif choice == "4":
            encrypted = caesar_cipher(text, shift)
            decrypted = caesar_decipher(encrypted, shift)
            frequency = letter_frequency(text)

            print(f"Ciphered text: {encrypted}")
            print("Letter frequency:")

            for letter, count in frequency.items():
                print(f"{letter}: {count}")

            print(f"Deciphered text: {decrypted}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()

