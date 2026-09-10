"""The Module for plotting mathematical functions.
This module provides functionality to plot mathematical functions
over a specified domain with customizable sampling.
"""
import matplotlib.pyplot as plt


def plot_function(fun_str, domain, ns):
    """Plot a mathematical function using the given domain and samples."""

    # Get the minimum and maximum x values from the domain.
    xmin = domain[0]
    xmax = domain[1]

    # Calculate the distance between each sample point.
    step = (xmax - xmin) / (ns - 1)

    # Create an empty list to store x values.
    xs = []

    # Generate the x values using the number of samples.
    for i in range(ns):
        # Calculate the current x value.
        x_value = xmin + i * step

        # Add the x value to the list.
        xs.append(x_value)

    # Create an empty list to store y values.
    ys = []

    # Calculate a y value for every x value.
    for x in xs:
        # Evaluate the function using the current x value.
        y_value = eval(fun_str)

        # Add the y value to the list.
        ys.append(y_value)

    # Print the x and y values as a table.
    print(" x | y")
    print("--------|--------")

    # Display each x value with its matching y value.
    for x, y in zip(xs, ys):
        print(f"{x:8.1f} | {y:8.1f}")

    # Plot the x and y values.
    plt.plot(xs, ys)

    # Add labels to the x and y axes.
    plt.xlabel("x")
    plt.ylabel("y")

    # Add a title using the function entered by the user.
    plt.title(f"Graph of {fun_str}")

    # Add a grid to make the graph easier to read.
    plt.grid(True)

    # Display the graph.
    plt.show()


def main():
    """Main function to run the function plotter program."""

    # Display a welcome message.
    print("Welcome to the Function Plotter, dear manager bud!")
    print("///////////////////")

    # Ask the user to enter the mathematical function.
    fun_str = input("Please enter the function: ")

    # Ask the user for the minimum x value.
    xmin = float(input("Please enter minimum x: "))

    # Ask the user for the maximum x value.
    xmax = float(input("Please enter maximum x: "))

    # Ask the user how many sample points to use.
    ns = int(input("Please enter number of samples: "))

    # Store the minimum and maximum values as a domain.
    domain = (xmin, xmax)

    # Call plot_function() using the user's information.
    plot_function(fun_str, domain, ns)


# Run main() when this file is executed directly.
if __name__ == "__main__":
    main()

