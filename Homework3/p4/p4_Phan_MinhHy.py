import os
import tempfile

def ed_read(filename: str, from_pos: int = 0, to: int = -1) -> str:
    if not isinstance(from_pos, int) or not isinstance(to, int):
        raise TypeError("File positions must be integers")
    if from_pos < 0:
        raise ValueError("Starting position cannot be negative")
    if to != -1 and to < from_pos:
        raise ValueError("Ending position must be after starting position")
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    if to > len(content):
        raise IndexError("Ending position exceeds file length")
    if to == -1:
        return content[from_pos:]
    return content[from_pos:to]

def ed_find(filename: str, search_str: str) -> list[int]:
    if not isinstance(search_str, str):
        raise TypeError("Search value must be a string")
    if search_str == "":
        raise ValueError("Search string cannot be empty")
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    positions = []
    start = 0

    while True:
        index = content.find(search_str, start)
        if index == -1:
            break

        positions.append(index)
        start = index + len(search_str)
    return positions

def ed_replace(filename: str, search_str: str,
               replace_with: str, occurrence: int = -1) -> int:
    if not isinstance(search_str, str) or not isinstance(replace_with, str):
        raise TypeError("Search and replacement values must be strings")
    if search_str == "":
        raise ValueError("Search string cannot be empty")
    if not isinstance(occurrence, int):
        raise TypeError("Occurrence must be an integer")
    if occurrence < -1:
        raise ValueError("Occurrence must be -1 or greater")
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    positions = []
    start = 0

    while True:
        index = content.find(search_str, start)
        if index == -1:
            break
        positions.append(index)
        start = index + len(search_str)

    if occurrence == -1:
        count = len(positions)
        if count == 0:
            return 0
        new_content = content.replace(search_str, replace_with)

    else:
        if occurrence >= len(positions):
            return 0
        index = positions[occurrence]
        new_content = (content[:index] + replace_with +
                       content[index + len(search_str):])
        count = 1

    with open(filename, "w", encoding="utf-8") as file:
        file.write(new_content)
    return count

def ed_append(filename: str, string: str) -> int:
    if not isinstance(string, str):
        raise TypeError("Appended content must be a string")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(string)
    return len(string)

def testif(condition: bool, success: str, failure: str) -> None:
    print(success if condition else failure)

def test_ed_find(filename: str) -> None:
    print("\nTesting ed_find:")
    testif(ed_find(filename, "345") == [3, 13], "PASS: Find repeated string", "FAIL: Find repeated string")
    testif(ed_find(filename, "356") == [], "PASS: String not found", "FAIL: String not found")
    testif(ed_find(filename, "012") == [0, 10], "PASS: Find beginning string", "FAIL: Find beginning string")
    testif(ed_find(filename, "789") == [7, 17], "PASS: Find ending string", "FAIL: Find ending string")
    testif(ed_find(filename, "999") == [], "PASS: Missing string", "FAIL: Missing string")

def test_ed_replace(filename: str) -> None:
    print("\nTesting ed_replace:")
    original = "01234567890123456789"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(original)

    count = ed_replace(filename, "345", "ABCDE", 1)
    testif(count == 1, "PASS: Replace second occurrence count", "FAIL: Replace second occurrence count")
    testif(ed_read(filename) == "0123456789012ABCDE6789", "PASS: Replace second occurrence content", "FAIL: Replace second occurrence content")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(original)

    count = ed_replace(filename, "345", "ABCDE")
    testif(count == 2, "PASS: Replace all count", "FAIL: Replace all count")
    testif(ed_read(filename) == "012ABCDE6789012ABCDE6789", "PASS: Replace all content", "FAIL: Replace all content")
    count = ed_replace(filename, "XYZ", "ABC")
    testif(count == 0, "PASS: Replace missing string", "FAIL: Replace missing string")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(original)

    count = ed_replace(filename, "345", "ABCDE", 5)
    testif(count == 0, "PASS: Out of range occurrence", "FAIL: Out of range occurrence")
    testif(ed_read(filename) == original, "PASS: File unchanged", "FAIL: File unchanged")

def main() -> None:
    with tempfile.TemporaryDirectory() as folder:
        filename = os.path.join(folder, "file1.txt")
        print("Non-Interactive Text Editor")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Appending text:")
        print("Characters written:", ed_append(filename, "0123456789"))
        print("Characters written:", ed_append(filename, "0123456789"))
        print("File content:", ed_read(filename))
        print("Reading text:")
        print("Read from 3 to 9:", ed_read(filename, 3, 9))
        print("Read from 3 to end:", ed_read(filename, 3))
        print("Finding text:")
        print("Find '345':", ed_find(filename, "345"))
        print("Find '356':", ed_find(filename, "356"))
        print("Replacing text:")
        print("Replacements:", ed_replace(filename, "345", "ABCDE", 1))
        print("File content:", ed_read(filename))

        with open(filename, "w", encoding="utf-8") as file:
            file.write("01234567890123456789")
        print("Replace all:", ed_replace(filename, "345", "ABCDE"))
        print("File content:", ed_read(filename))

        with open(filename, "w", encoding="utf-8") as file:
            file.write("01234567890123456789")
        test_ed_find(filename)
        test_ed_replace(filename)
    print("Name: Minh Hy Phan")
    print("Student ID: Z23766758")

if __name__ == "__main__":
    main()
