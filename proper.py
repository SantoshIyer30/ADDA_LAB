def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle (float).
        width: The width of the rectangle (float).

    Returns:
        The area of the rectangle (float).
    """

    return length * width

total_area = calculate_area(5.0, 3.0)  # Use explicit type conversion if needed

message = f"The total area is: {total_area:.2f} square units"  # F-string formatting
print(message)
