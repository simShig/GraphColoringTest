class Point:
    # Class variable to keep track of the total number of points created
    _total_points = 0

    def __init__(self, value):
        # Increment the total points counter and assign it as the serial number
        Point._total_points += 1
        self.serial_num = Point._total_points

        # Initialize other instance variables
        self.value = value
        self.col_num = None

    def __repr__(self):
        return f"Point(serial_num={self.serial_num}, value={self.value}, col_num={self.col_num})"
