class Room:
  """Represents a room with length and width attributes."""

  def __init__(self, length, width):
    """Initializes a Room object with the given length and width."""
    self.length = length
    self.width = width

  def calculate_area(self):
    """Calculates the area of the room."""
    area = self.length * self.width
    return area

# Get user input for length and width
length = float(input("Enter the length of the room: "))
width = float(input("Enter the width of the room: "))

# Create a Room object
my_room = Room(length, width)

# Calculate and print the area
area = my_room.calculate_area()
print("The area of the room is:", area, "square units")