import turtle
import time
from testif import testif

#A)
def draw_branch(level: int, length: float, curved: bool = False,
                original_level: int = 0) -> None:
    """Draw recursive branches with separated main branches."""
    if level == 0:
        return

    start_pos = turtle.position()
    start_heading = turtle.heading()

    step = length * 0.48

    # Draw the first part of the stem
    if curved:
        for i in range(5):
            turtle.forward(step / 5)
            turtle.right(1)
    else:
        turtle.forward(step)

    pos = turtle.position()
    heading = turtle.heading()

    # Settings for the two biggest branches
    if level == original_level:
        side_angle = 70
        side_length = 0.48
        branch_position = 0.40
    else:
        side_angle = 42
        side_length = 0.58
        branch_position = 0.15

    turtle.penup()
    turtle.backward(length * branch_position)
    side_pos = turtle.position()
    turtle.pendown()

    # Left branch
    turtle.setheading(heading + side_angle)
    draw_branch(level - 1, length * side_length,
                curved, original_level)

    # Return to the branching position
    turtle.penup()
    turtle.setposition(side_pos)
    turtle.setheading(heading)
    turtle.pendown()

    # Right branch
    turtle.setheading(heading - side_angle)
    draw_branch(level - 1, length * side_length,
                curved, original_level)

    # Return to the top of the stem
    turtle.penup()
    turtle.setposition(pos)
    turtle.setheading(heading)
    turtle.pendown()

    # Continue the middle branch
    turtle.forward(length * 0.52)

    draw_branch(level - 1, length * 0.68,
                curved, original_level)

    # Return to the original starting position
    turtle.penup()
    turtle.setposition(start_pos)
    turtle.setheading(start_heading)
    turtle.pendown()

def draw_leaf_straight(level: int, length: float) -> None:
    """Draw a vertical recursive leaf using straight branches."""
    if level < 1 or length <= 0:
        raise ValueError("Level and length must be positive")

    turtle.clearscreen()
    turtle.tracer(0, 0)
    turtle.hideturtle()
    turtle.pensize(1)

    turtle.penup()
    turtle.goto(0, -length * 1.5)
    turtle.setheading(90)
    turtle.pendown()

    # Draw the main stem
    turtle.forward(length)

    # Draw the recursive branches
    draw_branch(level, length, False, level)

    turtle.update()

def draw_leaf_curved(level: int, length: float) -> None:
    """Draw a vertical recursive leaf with curved branches."""
    if level < 1 or length <= 0:
        raise ValueError("Level and length must be positive")

    turtle.clearscreen()
    turtle.tracer(0, 0)
    turtle.hideturtle()
    turtle.pensize(1)

    turtle.penup()
    turtle.goto(0, -length * 1.5)
    turtle.setheading(90)
    turtle.pendown()

    # Draw the curved main stem
    for i in range(20):
        turtle.forward(length / 20)
        turtle.right(0.5)

    # Draw the recursive curved branches
    draw_branch(level, length, True, level)
    turtle.update()

#B)
def strB(n: int, base: int = 10) -> str:
    """Convert a nonnegative integer to a string in the given base."""
    if n < 0:
        raise ValueError("n must be nonnegative")

    if base < 2 or base > 26:
        raise ValueError("Base must be between 2 and 26")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Base case
    if n < base:
        return digits[n]

    # Recursive case
    return strB(n // base, base) + digits[n % base]

def test_strB() -> None:
    print("\nTesting strB:")

    testif(strB(255, 16) == "FF", "Base 16")
    testif(strB(42, 2) == "101010", "Base 2")
    testif(strB(81, 3) == "10000", "Base 3")
    testif(strB(0, 26) == "0", "Zero")

#C)
def Cnk_m(n: int, k: int, memo: dict = None) -> int:
    """Calculate n-choose-k recursively using memoization."""
    if n < 0 or k < 0 or k > n:
        raise ValueError("Require 0 <= k <= n")

    if memo is None:
        memo = {}

    # Base cases
    if k == 0 or k == n:
        return 1

    # Return a previously calculated answer
    if (n, k) in memo:
        return memo[(n, k)]

    # Recursive formula
    result = Cnk_m(n - 1, k - 1, memo) + Cnk_m(n - 1, k, memo)

    # Store the result for future use
    memo[(n, k)] = result

    return result

def run_Cnk(n: int, k: int) -> None:
    """Display the binomial coefficient and execution time."""
    start = time.perf_counter()

    result = Cnk_m(n, k)

    elapsed = time.perf_counter() - start

    print(f"C({n}, {k}) = {result}")
    print(f"Execution time: {elapsed:.6f} seconds")

def test_Cnk_m() -> None:
    """Run four unit tests for Cnk_m."""
    print("\nTesting Cnk_m:")

    testif(Cnk_m(5, 2) == 10, "C(5,2)")
    testif(Cnk_m(10, 3) == 120, "C(10,3)")
    testif(Cnk_m(6, 0) == 1, "C(6,0)")
    testif(Cnk_m(8, 8) == 1, "C(8,8)")

# D)
def make_pairs(seq1: list, seq2: list,
               index: int = 0, result: list = None) -> list:
    """Recursively pair matching elements from two lists."""
    if result is None:
        result = []

    # Base case: stop at the end of the shorter list
    if index >= len(seq1) or index >= len(seq2):
        return result

    # Add the matching elements as a tuple
    result.append((seq1[index], seq2[index]))

    # Recursive call
    return make_pairs(seq1, seq2, index + 1, result)


def test_make_pairs() -> None:
    """Run five unit tests for make_pairs."""
    print("\nTesting make_pairs:")

    testif(
        make_pairs([1, 2, 3], [4, 5, 6]) ==
        [(1, 4), (2, 5), (3, 6)],
        "Equal lists"
    )

    testif(
        make_pairs([1, 2, 3], [4, 5]) ==
        [(1, 4), (2, 5)],
        "Shorter second list"
    )

    testif(
        make_pairs([1, 2], [4, 5, 6]) ==
        [(1, 4), (2, 5)],
        "Shorter first list"
    )

    testif(
        make_pairs([], [4, 5, 6]) == [],
        "Empty first list"
    )

    testif(
        make_pairs([1, 2, 3], []) == [],
        "Empty second list"
    )

def main() -> None:
    # Part B: Test base conversion
    test_strB()
    # Part C: Test binomial coefficient
    test_Cnk_m()
    # Part D: Test making pairs
    test_make_pairs()

    #Part B
    print("\nBase conversion examples:")
    print("strB(255, 16) =", strB(255, 16))
    print("strB(42, 2) =", strB(42, 2))
    print("strB(500, 8) =", strB(500, 8))

    #Part C
    print("\nBinomial coefficient example:")
    run_Cnk(30, 15)

    #Part D
    print("\nMaking pairs example:")
    print(make_pairs(["A", "B", "C"], [10, 20, 30]))

    draw_leaf_straight(6, 120)
    turtle.done()

if __name__ == "__main__":
    main()
