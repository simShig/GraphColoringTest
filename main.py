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
    # Extracting values and color numbers for plotting
    values = [point.value for point in points]
    col_nums = [point.col_num for point in points]

    plt.figure(figsize=(12, 6))
    plt.bar(values, col_nums, color='blue')
    plt.xlabel('Point Value')
    plt.ylabel('Color Number')
    plt.title('Column Plot with Point Values on X-axis and Color Numbers on Y-axis')
    plt.grid(True, axis='y')
    plt.show()


