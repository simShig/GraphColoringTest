import coloringAlgForStudents
from Point import Point
from coloringAlgForStudents import onlineColoringAlg, rectangleColoringAlg, points, maxCol, isOnlineAlg
import random


def runValues(n):
    # Generate a list of 100 random values
    random_values = [random.random() * 100 for _ in range(n)]
    # print(random_values[:5])  # Display the first 5 values for a quick check
    if isOnlineAlg:
        for val in random_values:
            onlineColoringAlg(val)

    else:
        # i=0
        for index, val in enumerate(random_values):
            p = Point(val, random_values[(index + 1) % len(random_values)])
            p.col_num = 0
            # p.col_num = i
            # i+=1
            points.append(p)
        rectangleColoringAlg()

    print("\n\tpoint list:\n\t-----------")
    for p in points:
        print(p)
    checkCorrectness()


def has_unique_color_in_every_segment(points):
    points = sorted(points, key=lambda point: point.valueX)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
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


def checkCorrectness():
    # Test the function with your points
    result = has_unique_color_in_every_segment(points)
    print("\n\tcorrectness:\n\t-----------")
    if result[0]:
        from coloringAlgForStudents import maxCol
        print(f"all segments has unique color in them, max color is {findMaxCol()}")
    else:
        print(f"test failed, there is no unique color in the segment:"
              f"\np{result[1][0]}"
              f"\n~"
              f"\np{result[1][-1]}")
        print("\n\tpoints at segment:")
        for point in result[1]:
            print(point)


##-----TEST DOWN HERE -\/----

print(f"Starting test for students {coloringAlgForStudents.STUDENTS_ID} :")
num_of_points = 100
runValues(num_of_points)

##-----TEST UP HERE --/\----
