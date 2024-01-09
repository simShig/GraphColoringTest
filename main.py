from Point import Point
from coloringAlg import points, maxCol, coloringAlg
import random

# Generate a list of 100 random values
random_values = [random.random()*100 for _ in range(100)]
print(random_values[:5])  # Display the first 5 values for a quick check

for val in random_values:
    coloringAlg(val)

for point in points:
    print(point)

def plotPoints():

    import matplotlib.pyplot as plt
    pointZ = points
    # # Sample data
    # points = [
    #     {"serial_num": 1, "value": 75.10485700270301, "col_num": 11},
    #     {"serial_num": 2, "value": 1.4553844722133058, "col_num": 11},
    #     {"serial_num": 3, "value": 96.52729756134998, "col_num": 11},
    #     {"serial_num": 4, "value": 56.03362801814217, "col_num": 11},
    #     {"serial_num": 5, "value": 42.41522959545483, "col_num": 11},
    #     {"serial_num": 6, "value": 63.9981027411161, "col_num": 11},
    #     {"serial_num": 7, "value": 76.67888729826187, "col_num": 11},
    #     {"serial_num": 8, "value": 50.36114298797455, "col_num": 11},
    #     {"serial_num": 9, "value": 80.50116523235471, "col_num": 11},
    #     {"serial_num": 10, "value": 98.38377563162734, "col_num": 11},
    #     {"serial_num": 11, "value": 41.134349473892094, "col_num": 11},
    #     {"serial_num": 12, "value": 63.18333430853319, "col_num": 11},
    #     {"serial_num": 13, "value": 80.47927848845306, "col_num": 11},
    #     {"serial_num": 14, "value": 0.9537555127870134, "col_num": 11},
    #     {"serial_num": 15, "value": 88.97610622528552, "col_num": 11}
    # ]

    # Extracting values and color numbers for plotting
    values = [point.value for point in pointZ]
    col_nums = [point.col_num for point in pointZ]

    plt.figure(figsize=(12, 6))
    plt.bar(range(len(values)), values, color='blue')
    plt.xlabel('Point Number')
    plt.ylabel('Value')
    plt.title('Column Plot of Points with Values')
    plt.xticks(range(len(values)), [f"Point {point.serial_num}" for point in points])
    plt.grid(True, axis='y')
    plt.show()


