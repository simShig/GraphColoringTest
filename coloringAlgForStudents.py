from Point import Point

maxCol = 0
points = []
isOnlineAlg = False      #if RectangleAlg: =False
STUDENTS_ID="123456789_987654321"   #change IDs

def onlineColoringAlg(value):
    """
    students' algorithm for "online coloring"
    methodology - iterative call for method.
    use a point (given by x-value), give it a color(according to "points" list expanding each time).
    :param value: numeric value of the point (x-coordinate)
    :return: color_num
    """
    global maxCol
    p = Point(value)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # your ALG here...

    color_num = maxCol

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    p.col_num = color_num
    points.append(p)
    print(f"current max col is:{maxCol}")
    return color_num


def rectangleColoringAlg():
    """
    students' algorithm for "rectangle coloring"
    methodology - one-time call for method.
    use a given "points" list, color all points.
    :param: no arguments (method called once)
    :return: nothing
    """
    global isOnlineAlg
    isOnlineAlg = False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # your ALG here...


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print(f"current max col is:{maxCol}")
    print(f"finished running rectangleColoringAlg...")
    return