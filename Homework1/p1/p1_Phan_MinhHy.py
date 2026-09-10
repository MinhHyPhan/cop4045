"""Solve and graph quadratic equations.

This module calculates the real roots of a quadratic equation
using the quadratic formula and displays the equation as a graph.
"""

import matplotlib.pyplot as plt
import numpy as np


def quad_solver(a, b, c):
    """Find the real roots of ax² + bx + c = 0.

    The discriminant determines how many real solutions exist.
    A negative discriminant means there are no real roots.
    A zero discriminant means there is one repeated root.
    A positive discriminant means there are two different roots.

    Returns:
        A tuple containing the real roots. If there are no real
        roots, both values in the tuple are None.
    """
    # Calculate the discriminant to determine the number of real roots.
    discriminant = b ** 2 - 4 * a * c

    # A negative discriminant means the equation has no real roots.
    if discriminant < 0:
        return None, None

    # A zero discriminant means the equation has one repeated root.
    if discriminant == 0:
        root = -b / (2 * a)
        return root, root

    # A positive discriminant means the equation has two real roots.
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)

    return root1, root2


def plot_func(a, b, c, x1, x2):
    """Graph the quadratic function and display its real roots.

    The graph uses a black background with white labels and axes.
    The quadratic function is shown in red, and real roots are
    marked with yellow points.
    """
    # Choose a graph range based on the location of the roots.
    if x1 is None:
        x_range = 12
    else:
        largest_root = max(abs(x1), abs(x2))
        x_range = largest_root + 6

    # Create x-values and calculate the corresponding y-values.
    x = np.linspace(-x_range, x_range, 600)
    y = a * x * x + b * x + c

    # Create the graph.
    fig, ax = plt.subplots(figsize=(11, 6))

    # Set the background color to black.
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    # Draw the quadratic function in red.
    ax.plot(x, y, color="red", linewidth=3)

    # Draw the x-axis and y-axis in white.
    ax.axhline(0, color="white", linewidth=0.67)
    ax.axvline(0, color="white", linewidth=0.67)

    # Add a white grid with some transparency.
    ax.grid(True, color="white", alpha=0.3)

    # Make the labels and title white.
    ax.set_xlabel("x", color="white")
    ax.set_ylabel("y", color="white")
    ax.set_title(
        f"y = {a}x² + {b}x + {c}",
        color="white"
    )

    # Make the numbers on the axes white.
    ax.tick_params(axis="both", colors="white")

    # Make the graph border white.
    for spine in ax.spines.values():
        spine.set_color("white")

    # Mark the real roots with yellow points.
    if x1 is not None:
        ax.plot(
            [x1, x2],
            [0, 0],
            "o",
            color="yellow",
            markersize=11
        )

    # Display the graph.
    plt.show()


def main():
    """Run the quadratic solver and graph each equation."""
    print("Welcome to the Quadratic Solver, manager bud!")
    print("Please enter a, b, c for ax² + bx + c = 0")
    print("To exit,please press Enter!\n")

    while True:
        # Ask the user for the first coefficient.
        a_input = input("Please enter a: ")

        # Stop the program when the user presses Enter without input.
        if a_input.strip() == "":
            print("Goodbye! See you tomorrow!")
            break

        # Convert the user's input into a number.
        a = float(a_input)

        # Ask for the remaining coefficients.
        b = float(input("Please enter b: "))
        c = float(input("Please enter c: "))

        # Calculate the real roots.
        x1, x2 = quad_solver(a, b, c)

        # Display the number of real solutions.
        if x1 is None:
            print("No real solutions")
        elif x1 == x2:
            print(f"One solution: {x1}")
        else:
            print(f"Two solutions: {x1} and {x2}")

        # Display the quadratic function and its roots.
        plot_func(a, b, c, x1, x2)


if __name__ == "__main__":
    main()

