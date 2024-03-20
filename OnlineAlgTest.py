from Point import Point
from coloringAlgForStudents import onlineColoringAlg, points, maxCol, isOnlineAlg
import random
import math


def getValues(n):
    #Generate random values:
    # valuesList = [random.random() * 100 for _ in range(n)]

    #Generate ardesh sequences (of \sqrt(n) descending blocks):
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

    # print(valuesList)

    return valuesList


def runTest(n):
    # Generate a list of 100 random values
    corFlag = None
    random_values = getValues(n)
    # print(random_values[:5])  # Display the first 5 values for a quick check
    if isOnlineAlg:
        print("asserted colors:")
        for val in random_values:
            cn = onlineColoringAlg(val)
            print(f"{cn}, " ,end='' )
            corFlag = checkCorrectness(val)
            if(not corFlag): return        ##unmark if you want to check correctness every step
    else:
        print ("'isOnlineAlg' set to 'False', probably its not an OnlineAlg")
        print("\n\tQUITTING PROGRAM")
        return

    # print("\n\tpoint list:\n\t-----------")
    # for p in points:
    #     print(p)

    if(corFlag):
        plotPoints()
        print(f"\n\t\t\t~~~~TEST PASSED!~~~\n\t\t\t~~~~maxCol is {findMaxCol()}~~~")
    else: print("\n\t\t\t~~~~TEST FAILED!~~~")




def checkCorrectness(lastPointX = None):
    # Test the function with your points
    result = None
    if lastPointX:
        result = has_unique_color_in_every_segment(points,lastPointX)
    else:
        result = has_unique_color_in_every_segment(points)
    print("\n\tcorrectness:\n\t-----------")
    if result[0]:
        from coloringAlgForStudents import maxCol
        print(f"all segments has unique color in them, max color is {findMaxCol()}")
        # plotPoints()
        return True
    else:
        print(f"test failed, there is no unique color in the segment:"
              f"\np{result[1][0]}"
              f"\n~"
              f"\np{result[1][-1]}")
        print("\n \tsegment:")
        for point in result[1]:
            print(point)
        plotPoints(result[1])
        return False
         




def plotPoints(segment=None):
    import matplotlib.pyplot as plt
    try:
        # Extracting values and color numbers for plotting
        values = [point.valueX for point in points]
        col_nums = [point.col_num for point in points]

        plt.figure(figsize=(12, 6))
        plt.bar(values, col_nums, color='blue')
        if segment:
            plt.axvspan(segment[0].valueX, segment[-1].valueX, color='red', alpha=0.3)
        plt.xlabel('Point Value')
        plt.ylabel('Color Number')
        plt.title('Column Plot with Point Values on X-axis and Color Numbers on Y-axis')
        plt.grid(True, axis='y')
        plt.show()
    except TypeError as e:
        print(f"No point colors,therefore error in plotting:\n"
              f"({e})")


def has_unique_color_in_every_segment(points,lastPointX=None):
    points = sorted(points, key=lambda point: point.valueX)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            PiX = (points[i]).valueX
            PjX = (points[j]).valueX
            if lastPointX:
                if(not PiX<=lastPointX<=PjX):
                    continue
            print (f"for X= {lastPointX}, now checking segment: (x={PiX})~(x={PjX})")
            # Extracting the segment between points[i] and points[j]
            segment = points[i:j + 1]

            # Counting the occurrences of each color in this segment
            color_counts = {}
            for point in segment:
                color_counts[point.col_num] = color_counts.get(point.col_num, 0) + 1

            # Checking if there's exactly one color that appears once
            unique_colors = [color for color, count in color_counts.items() if count == 1]
            if not (any(unique_colors) == 1):
                return False, segment  # Found a segment without a unique color

    return True, None  # All segments have a unique color


def findMaxCol():
    maxPoint = sorted(points, key=lambda point: point.col_num)[-1]
    maxColor = maxPoint.col_num
    return maxColor



if __name__ == "__main__":
    runTest(500)