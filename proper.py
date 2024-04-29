def calculate_area(length, width):
  """Calculates the area of a rectangle.

  Args:
      length (float): The length of the rectangle.
      width (float): The width of the rectangle.

  Returns:
      float: The area of the rectangle (length * width).
  """


  return length * width

total_area = calculate_area(5, 3)


message = "The total area is: {} square units".format(total_area)
print(message)
