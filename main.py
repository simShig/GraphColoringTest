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

def plotPoints(segment = None):

    import matplotlib.pyplot as plt
    # Extracting values and color numbers for plotting
    values = [point.value for point in points]
    col_nums = [point.col_num for point in points]

    plt.figure(figsize=(12, 6))
    plt.bar(values, col_nums, color='blue')
    if segment:
        plt.axvspan(segment[0].value, segment[-1].value, color='yellow', alpha=0.3)
    plt.xlabel('Point Value')
    plt.ylabel('Color Number')
    plt.title('Column Plot with Point Values on X-axis and Color Numbers on Y-axis')
    plt.grid(True, axis='y')
    plt.show()


def has_unique_color_in_every_segment(points):
    points = sorted(points, key=lambda point: point.value)
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            # Extracting the segment between points[i] and points[j]
            segment = points[i:j+1]

            # Counting the occurrences of each color in this segment
            color_counts = {}
            for point in segment:
                color_counts[point.col_num] = color_counts.get(point.col_num, 0) + 1

            # Checking if there's exactly one color that appears once
            unique_colors = [color for color, count in color_counts.items() if count == 1]
            if not (any(unique_colors) == 1):
                return False, segment  # Found a segment without a unique color

    return True,None  # All segments have a unique color

# Test the function with your points
result = has_unique_color_in_every_segment(points)
if result[0]:
    print (f"all segments has unique color in them, max color is {maxCol}")
else:
    print (f"test failed, there is no unique color in the segment p{result[1][0]}~p{result[1][-1]}")
    print("segment:")
    for point in result[1]:
        print(point)

    plotPoints(result[1])
