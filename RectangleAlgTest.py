from Point import Point
import math
from coloringAlgForStudents import rectangleColoringAlg, points, maxCol, isOnlineAlg
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def getValues(n):
    # Generate random values:
    # valuesList = [random.random() * 100 for _ in range(n)]

    # Generate ardesh sequences (of \sqrt(n) descending blocks):
    block_size = int(math.sqrt(n))

    # Initialize an empty list to store the result
    valuesList = []

    # Generate values for each block
    for i in range(0, n, block_size):
        # Calculate the start and end of the current block
        start = i + 1
        end = i + block_size
        # Generate the numbers for the block in descending order and append to the list
        block = list(range(end, start - 1, -1))
        valuesList.extend(block)

    print(valuesList)

    return valuesList


def createPointList(n):
    yVals = getValues(n)
    xVals = sorted(yVals.copy())
    # create point list with tuples of (x,y) values from xVals,yVals accordinagly:
    pointsList = []
    for i in range(n):
        p = Point(xVals[i], yVals[i])
        pointsList.append(p)
    print(pointsList)
    return pointsList


def plotPoints2D(points, segment=None):
    # Extracting X and Y values for plotting
    valuesX = [point.valueX for point in points]
    valuesY = [point.valueY for point in points]

    plt.figure(figsize=(12, 6))

    # Scatter plot for all points
    plt.scatter(valuesX, valuesY, color='blue', label='Points')

    # If a segment is provided, draw a rectangle around it
    if segment:
        # Calculate the bounds of the rectangle
        minX = min(point.valueX for point in segment)
        maxX = max(point.valueX for point in segment)
        minY = min(point.valueY for point in segment)
        maxY = max(point.valueY for point in segment)

        # Create the rectangle from the bounds
        rect = Rectangle((minX, minY), maxX - minX, maxY - minY, linewidth=1, edgecolor='r', facecolor='none',
                         label='Segment')

        # Add the rectangle to the plot
        plt.gca().add_patch(rect)

    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.title('Scatter Plot with Points in 2D Space and Segment Rectangle')
    plt.legend()
    plt.grid(True)
    plt.show()


def runTest(n):
    # Generate a list of 100 random values
    random_values = getValues(n)
    random_values = [random.random() * 100 for _ in range(n)]
    # print(random_values[:5])  # Display the first 5 values for a quick check
    if isOnlineAlg:
        for val in random_values:
            cn = onlineColoringAlg(val)
            print("color is: ", cn)
            checkCorrectness()
    else:
        print("'isOnlineAlg' set to 'False', probably its not an OnlineAlg")

    print("\n\tpoint list:\n\t-----------")
    for p in points:
        print(p)
    # checkCorrectness()



if __name__ == "__main__":
    # getValues(10000)
    points = createPointList(100)
    segment = points[18],points[80]
    plotPoints2D(points,segment)