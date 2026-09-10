"""Unit tests for the Caesar Cipher program."""

import unittest

from p5_Phan_MinhHy import caesar_cipher
from p5_Phan_MinhHy import caesar_decipher
from p5_Phan_MinhHy import letter_frequency


class TestCaesarCipher(unittest.TestCase):
    """Test the Caesar Cipher functions."""

    def test_cipher(self):
        """Test that encryption works correctly."""
        self.assertEqual(
            caesar_cipher("Hello World", 3),
            "Khoor Zruog"
        )

    def test_decipher(self):
        """Test that decryption returns the original message."""
        encrypted = caesar_cipher("Hello World", 3)

        self.assertEqual(
            caesar_decipher(encrypted, 3),
            "Hello World"
        )

    def test_spaces_and_case(self):
        """Test that spaces and letter casing are preserved."""
        self.assertEqual(
            caesar_cipher("Ab C", 1),
            "Bc D"
        )

    def test_frequency(self):
        """Test the letter frequency function."""
        frequency = letter_frequency("Hello!")

        self.assertEqual(frequency["h"], 1)
        self.assertEqual(frequency["e"], 1)
        self.assertEqual(frequency["l"], 2)
        self.assertEqual(frequency["o"], 1)
        self.assertEqual(frequency["a"], 0)


if __name__ == "__main__":
    unittest.main()

