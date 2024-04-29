# ADDA_LAB (consider renaming to snake_case)

def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle (float).
        width: The width of the rectangle (float).

    Returns:
        The area of the rectangle (float).
    """

    return length * width

TOTAL_AREA = calculate_area(5.0, 3.0)  # Use explicit type conversion if needed

# Consider adding functionality to proper.py

# error.py (consider renaming to descriptive name)
def print_message(message):  # Define a function to print the message
    """Prints a formatted message.

    Args:
        message: The message to be printed (str).
    """

    print(f"The total area is: {TOTAL_AREA:.2f} square units")  # F-string formatting

# Call the defined function
print_message("This message comes from a function!")
