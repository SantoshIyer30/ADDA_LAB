"""This module contains functions for performing proper calculations.

(Consider adding a more descriptive explanation of the calculations performed)
"""


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
print(f"The total area is: {TOTAL_AREA:.2f} square units")  # F-string formatting

# Call the defined function
print("This message comes from a function!")
